import requests
import config
import json
def send(msg):
    msg = '乐健体育自动化程序\n\n' + msg
    data = {
        'appToken': config.config_wxpusher['APP_TOKEN'],
        'content': msg,
        'contentType': 1,
        'uids' : [config.config_wxpusher['userIds']],
    }
    try:
        r = requests.post('http://wxpusher.zjiecode.com/api/send/message',data=json.dumps(data),headers = {'Content-Type':'application/json'})
        r_data = json.loads(r.text)
        print('微信推送程序：'+r_data['msg'])
        return True
    except:
        return False