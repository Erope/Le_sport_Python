import requests
import config
import json

def login():
    try:
        r = requests.post(config.config_url['login'],data = json.dumps(config.config_login), headers = config.config_header_post)
        info = json.loads(r.text)
    except:
        print('网络无法连接！请确认联网或乐健体育服务器在线！')
        exit(0)
    if 'message' in info:
        if info['message'] != None:
            print(info['message'])
    if 'code' in info:
        if info['code'] != 0:
            print('登陆失败！')
            exit(0)
    else:
        print('登陆失败！')
        exit(0)
    return info


def self_info():
    try:
        r = requests.get(config.config_url['self_info'], headers = config.config_header_get)
        info = json.loads(r.text)
    except:
        print('网络无法连接！请确认联网或乐健体育服务器在线！')
        exit(0)
    if 'message' in info:
        if info['message'] != None:
            print(info['message'])
    if 'code' in info:
        if info['code'] != 0:
            print('获取个人信息失败！')
            exit(0)
    else:
        print('获取个人信息失败！')
        exit(0)
    return info