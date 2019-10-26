import requests
import json
from config import *
from time import *
import wxpusher
import hashlib


def today_act():
    # 只请求第一页的内容，我想应该也没人一天签到10次吧。。。
    data = {
        'pageNum': 1,
        'pageSize': 10,
        'type': '-1',
    }
    try:
        r = requests.post(config_url['today_act'],data = json.dumps(data), headers = config_header_post)
    except:
        print('请求今日活动数据失败！')
        exit(0)
    return json.loads(r.text)


def get_act_gps_info(act):
    data = {
        'activityId': act,
    }
    r = requests.get(config_url['act_gps_info'],params = data, headers = config_header_get)
    return json.loads(r.text)


def show_gps_info(act):
    str_show = str(act['data']['signStatus']) + '\t'
    str_show += str(act['data']['position']) + '\t'
    str_show += str(act['data']['distance']) + '\t'
    print(str_show)


def show_today_act(act_list):
    list = act_list['data']['items']
    for i in list:
        str_show = str(i['id']) + '\t' + i['name']
        if i['signStatus'] == 5:
            str_show += '\t'+ '已请假'
        elif i['signStatus'] == 4:
            str_show += '\t' + '二次签到'
        elif i['signStatus'] == 3:
            str_show += '\t' + '一次签到'
        elif i['signStatus'] == 2:
            str_show += '\t' + '定位签到'
        elif i['signStatus'] == 1:
            str_show += '\t' + '未开始'
        else:
            str_show += '\t' + '错误情况'
        print(str_show)


def get_act_list():
    data = {
        'pageNum': 1,
        'pageSize': 100,
        'topic': False,
        'topicId': 300320,
    }
    r = requests.post(config_url['act_list'],data = json.dumps(data), headers=config_header_post)
    return json.loads(r.text)


def show_act_list_info(act_list):
    list = act_list['data']['items']
    for i in list:
        str_show =str(i['id']) + '\t' + i['name']+'\t'+ str(i['registerPeopleNumber']) + '/' + str(i['limitPeopleNumber'])
        if i['registerStatus'] == 2:
            str_show += '\t'+ '已报名'
        elif i['registerStatus'] == 1 or i['registerStatus'] == 3 or i['registerPeopleNumber']==i['limitPeopleNumber']:
            str_show += '\t' + '已满员'
        elif i['registerStatus'] == 5:
            str_show += '\t' + '报名截止'
        elif i['registerStatus'] == 6:
            str_show += '\t' + '进行中'
        elif i['registerStatus'] == 7:
            str_show += '\t' + '已结束'
        else:
            str_show += '\t'  + '可报名'
        print(str_show)


def sign_act(act_id, flag):
    list = act_id.split(',')
    if flag:
        try_time = 100000
    else:
        try_time = 1
    while try_time!= 0:
        for i in list:
            data = {
                'activityId': int(i),
            }
            try:
                r = requests.post(config_url['act_register'],data = json.dumps(data), headers = config_header_post)
                r_dic = json.loads(r.text)
                if 'code' in r_dic:
                    if r_dic['code'] == 0:
                        print('活动：'+ i +' 报名成功！')
                        # 发送信息
                        wxpusher.send('活动：'+ i +' 报名成功！')
                        return
                str_show = strftime('%Y-%m-%d %H:%M:%S', localtime(time())) + '\t' + i + '\t报名失败！'
                if 'message' in r_dic:
                    str_show += r_dic['message']
                print(str_show)
            except:
                print('报名时发生网络错误！')
        try_time -= 1
        sleep(config_timedelay)


def gen_sign(act,timestamp):
    str_sign = timestamp
    str_sign = timestamp[0:6] + act + timestamp[6:]
    hl = hashlib.md5()
    hl.update(str_sign.encode("utf-8"))
    str_sign = hl.hexdigest()
    str_sign = str_sign[3:15].lower()
    hl = hashlib.md5()
    hl.update(str_sign.encode("utf-8"))
    str_sign = hl.hexdigest()
    return str_sign


def act_sign_gps(act,flag):
    list = act.split(',')
    if flag:
        try_time = 100000
    else:
        try_time = 1
    while try_time != 0:
        for i in list:
            gps_info = get_act_gps_info(int(i))
            if gps_info['data']['position'] == None:
                print(strftime('%Y-%m-%d %H:%M:%S ', localtime(time())) + i + ' GPS定位参数暂未开放！')
                continue
            latitude = gps_info['data']['position']['latitude']
            longitude = gps_info['data']['position']['longitude']
            timestamp = int(round(time() * 1000))
            # 计算sign
            sign = gen_sign(str(i),str(timestamp))
            data = {
                'activityId': int(i),
                'deviceId': config_UUID,
                'location': {
                    'latitude': latitude,
                    'longitude': longitude,
                },
                'sign': sign,
                'timestamp': timestamp,
            }
            r = requests.post(config_url['act_sign'],data = json.dumps(data), headers = config_header_post)
            r_return = json.loads(r.text)
            if r_return['code'] == 0:
                print(strftime('%Y-%m-%d %H:%M:%S ', localtime(time())) + i + ' 签到成功！')
            else:
                print(strftime('%Y-%m-%d %H:%M:%S ', localtime(time())) + i + ' 签到失败！' + str(r_return['message']))
