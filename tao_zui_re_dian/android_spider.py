# coding: utf-8
import json
import requests
import time
import random
import base64
import hashlib
import pprint


def get_nonce():
    origin_str = "abcdefghijklmnopqrstuvwxyz0123456789"
    temp_str_list = []
    for i in range(6):
        temp_str = random.choice(origin_str)
        temp_str_list.append(temp_str)
    eve_str = ''.join(temp_str_list) + str(int(round(time.time() * 1000)))
    print(eve_str)
    return eve_str
    # print(''.join(temp_str_list))


# get_nonce()
def get_sign():
    timestamp = str(int(time.time()))
    pre_enc = (
                "android_id=4a51cc0f8b8effd0&app_ver=70&channel=tencent&device_id=5b6d40a46894881ee2d54ec17720c1c0&device_udid=8a4084ca6129765f674f02ad8f314a4a&first_time={}&from=app&last_time={}&limit=8&mac=74:AC:5F:CA:D6:47&nonce={}&os_ver_code=25&system=1&timestamp={}&video_first_time={}&video_last_time={}&with_super=0&with_video=1".format(
                    timestamp, timestamp, get_nonce(), timestamp, timestamp,
                    timestamp) + 'b2qKgtaW4,9z9D`Fmst?K5JZbLYOY]NP6ssGf2U~;zk9oCNgoytV!}wW7ia+`w9g').encode("utf-8")
    temp_sign = base64.b64encode(pre_enc)
    eve_sign = hashlib.sha1(str(temp_sign).encode('utf-8')).hexdigest()
    # print(eve_sign)
    return eve_sign, timestamp


def get_data():

    hot_news_url = 'https://api.news.taozuiredian.com/api/v1/news/hot'
    timestamp = get_sign()[1]
    sign = get_sign()[0]
    params = {
        'android_id': '4a51cc0f8b8effd0',
        'app_ver': '71',
        'channel': 'tencent',
        'device_id': '5b6d40a46894881ee2d54ec17720c1c0',
        'device_udid': '8a4084ca6129765f674f02ad8f314a4a',
        'first_time': '%s' % timestamp,
        'from': 'app',
        'last_time': '%s' % timestamp,
        'limit': '8',
        'mac': '74:AC:5F:CA:D6:47',
        'nonce': '%s' % get_nonce(),
        'os_ver_code': '25',
        'sign': '%s' % sign,
        'system': '1',
        'timestamp': '%s' % timestamp,
        'video_first_time': '%s' % timestamp,
        'video_last_time': '%s' % timestamp,
        'with_super': '0',
        'with_video': '1',
    }
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; 1605-A01 Build/NMF26F)',
        'Host': 'api.news.taozuiredian.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    res = json.loads(requests.get(hot_news_url, headers=headers, params=params, verify=False).text)
    pprint.pprint(res)


get_data()
