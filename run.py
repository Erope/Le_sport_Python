import requests
import json
from config import *
from time import *
import wxpusher
import hashlib
import random


def getrunningrule():
    r = requests.get(config_url['home_page'],headers=config_header_get)
    json_r = json.loads(r.text)
    return json_r['data']['runningRule']


def start():
    data = {
        "campusId": 22,
        "latitude": 30.76218407685636,
        "longitude": 103.98201672761103,
        "type": 1,
    }
    r = requests.post(config_url['run_start'], headers=config_header_post, data=json.dumps(data))
    return r.text


def end(start_text):
    start_s = json.loads(start_text)
    circuitString = {
        "randomCircuit": {
            "length": start_s['data']['randomCircuit']['length'],
            "ordered": start_s['data']['randomCircuit']['ordered'],
            "requireLatitude": start_s['data']['randomCircuit']['requireLatitude'],
            "requireLongitude": start_s['data']['randomCircuit']['requireLongitude'],
        },
        "runningRule": getrunningrule(),
        "time": start_s['data']['time'],
    }
    latitude = []
    longitude = []
    speed = []
    for i in range(1,210):
        tmp = 30.762 + (random.randint(1000000000000,5000000000000)/1000000000000000)
        latitude.append(tmp)
    for i in range(1,210):
        tmp = 103.979 + (random.randint(1000000000000,3000000000000)/1000000000000000)
        longitude.append(tmp)
    for i in range(1,210):
        tmp = random.randint(100,200)
        speed.append(tmp)
    timestamp = int(round(time() * 1000))
    passTime = [
        random.randint(timestamp - 500000, timestamp),
        random.randint(timestamp - 500000, timestamp),
        random.randint(timestamp - 500000, timestamp)
    ]
    distance = random.randint(3100, 3300)
    totalTime = random.randint(700, 750)
    startTime = timestamp - 700000
    endTime = timestamp
    phone = config_Phone
    s_md5 = "EndRunningInfo{{a='{}', b={}, c={}, d={}, e={}, f={}, g='{}'}}".format("", str(totalTime), str(distance),
                                                                                    "1", str(startTime), str(endTime),
                                                                                    str(phone))
    hl = hashlib.md5()
    hl.update(s_md5.encode("utf-8"))
    md5 = hl.hexdigest()
    data = {
        "calories": random.randint(200, 330),
        "circuitInfo": {
            "circuitString": json.dumps(circuitString),
            "latitude": [
                latitude,
            ],
            "longitude": [
                longitude,
            ],
            "passTime": passTime,
            "randomLatitude": start_s['data']['randomCircuit']['requireLatitude'],
            "randomLongitude": start_s['data']['randomCircuit']['requireLongitude'],
            "segment": [
                [
                    random.randint(timestamp - 650000, timestamp - 610000),
                    random.randint(timestamp - 1000, timestamp),
                ],
            ],
            "speed": speed,
        },
        "distance": distance,
        "endTime": timestamp,
        "id": 1,
        "md5": md5,
        "phone": phone,
        "platform": 1,
        "startTime": timestamp - 700000,
        "stepRate": random.randint(90, 120),
        "totalTime": totalTime,
        "type": 1,
        "valid": 1,
        "validDistance": distance,
        "version": "V 2.4.4",
    }
    r = requests.post(config_url['run_end'], headers=config_header_post, data=json.dumps(data))
    json_r = json.loads(r.text)
    if json_r['data']['valid'] == 1:
        print('跑步完成！')
        wxpusher.send('您的跑步已经完成并成功提交')
    else:
        print('跑步失败！原因：'+json_r['data']['invalidReason'])
        wxpusher.send('跑步失败！原因：'+json_r['data']['invalidReason'])
