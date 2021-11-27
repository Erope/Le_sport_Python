config_login = {
    'orgId': 418,  #校区ID
    'username': 'xxxxxxx',  #账户
    'password': 'xxxxxxx',  #密码
}
#POST头
config_header_post = {
    'Host': 'upes.legym.cn',
    'content-type': 'application/json;; charset=utf-8',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.10.0',
}
#GET头
config_header_get = {
    'Host': 'upes.legym.cn',
    'content-type': 'application/json;; charset=utf-8',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.10.0',
}
#URL表
config_url = {
    'login': 'https://upes.legym.cn/health/api/v1/login',
    'self_info': 'https://upes.legym.cn/health/api/v1/user/self',
    'today_act': 'https://upes.legym.cn/health/api/v1/me/today/activities',
    'act_list': 'https://upes.legym.cn/health/api/v1/activities/list',
    'act_register': 'https://upes.legym.cn/health/api/v1/register/single',
    'act_gps_info': 'https://upes.legym.cn/health/api/v1/attendance/gps/status',
    'act_sign': 'https://upes.legym.cn/health/api/v1/attendance/gps/sign',
    'run_start': 'https://upes.legym.cn/running/api/v1/running/start',
    'run_end': 'https://upes.legym.cn/running/api/v1/running/end3',
    'home_page': 'https://upes.legym.cn/health/api/v1/homePage/user',
}
#多次请求的延时
config_timedelay = 0
#硬盘UUID 建议修改
config_UUID = 'ffffffff-xxxx-xxxx-0000-0000xxxxxxxx'
#多少秒后发送跑步结束包
config_Rundelay = 900
#手机型号
config_Phone = 'Xiaomi Xiaomi MI 6'
#WXPUSHER 配置
config_wxpusher = {
    'APP_TOKEN': 'xxxxxxxxxx',
    'userIds': 'xxxxxxxxxxxxxx',
}
#高德SDK的key
config_amap = 'xxxxxxxxxx'
#跑步开始时的起始点
config_start_latitude = 30.7663030000
config_start_longitude = 103.9799940000
