import requests
import json
from config import *
import random


def getd(a,b,c,d):
    url = 'https://restapi.amap.com/v3/direction/walking?key=%s&origin=%s,%s&destination=%s,%s' % (config_amap, a, b, c, d)
    r = requests.get(url)
    r_json = json.loads(r.text)
    path = r_json['route']['paths']
    road = ""
    for i in path:
        step = i['steps']
        for j in step:
            road += j['polyline'] + ';'
    return road


def getrouad(start_text):
    start_s = json.loads(start_text)
    requireLatitude = start_s['data']['randomCircuit']['requireLatitude']
    requireLongitude = start_s['data']['randomCircuit']['requireLongitude']
    requireLatitude.append(30.7663030000 + (random.randint(-20000000000, 200000000000) / 10000000000000000))
    requireLongitude.append(103.9799940000 + (random.randint(-20000000000, 200000000000) / 10000000000000000))

    road = ""
    for i in range(0,4):
        road += getd(requireLongitude[i-1],requireLatitude[i-1],requireLongitude[i],requireLatitude[i])
    return road