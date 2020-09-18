# coding: utf-8

import requests
import time
import pprint
import hashlib
import json

def get_headers():
    headers = {
        'lang': 'zh-cn',
        'timezone': '+08:00',
        'uuid': '93ebb886-4240-3a6d-ae01-62e64d835f34',
        'version': '3.0.8',
        'packetBit': 'android_bishijie',
        'currency': 'CNY',
        'gid': 'e9632c255bdb11405092c3cede9e68bb',
        'Host': 'iapi.bishijie.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0',
    }
    return headers

def get_data():
    md = hashlib.md5()
    digest_str = str(int(time.time())) + 'FADB33D3A9DE315B397D4D1246E739BA' + 'client=android&size=20&timestamp={}'.format(int(time.time())) + 'C4nnxlBjuCOYbdVGyCdAK6' + str(int(time.time()))
    print(digest_str)
    digest_bytes = digest_str.encode('utf-8')
    md.update(digest_bytes)
    params = {
        'client': 'android',
        'timestamp': '%s' % int(time.time()),
        'size': '20',
        'ts': '%s' % int(time.time()),
        'signature': '%s' % md.hexdigest(),
        'nonce': 'C4nnxlBjuCOYbdVGyCdAK6' + str(int(time.time())),

    }
    res = requests.get('https://iapi.bishijie.com/v3/newsFlash', headers=get_headers(), params=params, verify=False).text
    pprint.pprint(json.loads(res))
get_data()