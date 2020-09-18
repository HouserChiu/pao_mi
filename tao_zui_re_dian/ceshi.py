# coding: utf-8
import json
import requests
import time
import base64
import hashlib
import pprint
from f_rpc import js_code


def get_data():
    eve_str = js_code()
    current_time = int(time.time())
    timestamp = str(current_time)
    pre_enc = 'android_id=5e5e2620622f1cac&app_ver=67&channel=tencent&device_id=5b6d40a46894881ee2d54ec17720c1c0&device_udid=8a4084ca6129765f674f02ad8f314a4a&first_time=1600048819&from=app&last_time=1600048098&limit=8&mac=74:AC:5F:CA:D6:47&nonce={}&os_ver_code=25&system=1&timestamp={}&video_first_time=1600048803&video_last_time=1600045205&with_super=0&with_video=1'.format(
        eve_str, timestamp) + 'b2qKgtaW4,9z9D`Fmst?K5JZbLYOY]NP6ssGf2U~;zk9oCNgoytV!}wW7ia+`w9g'
    temp_sign = base64.b64encode(pre_enc.encode('utf-8')).decode()
    eve_sign = hashlib.sha1(str(temp_sign).encode('utf-8')).hexdigest()
    hot_news_url = 'https://api.news.taozuiredian.com/api/v1/news/hot'
    params = {
        'android_id': '5e5e2620622f1cac',
        'app_ver': '67',
        'channel': 'tencent',
        'device_id': '5b6d40a46894881ee2d54ec17720c1c0',
        'device_udid': '8a4084ca6129765f674f02ad8f314a4a',
        'first_time': '1600048819',
        'from': 'app',
        'last_time': '1600048098',
        'limit': '8',
        'mac': '74:AC:5F:CA:D6:47',
        'nonce': '%s' % eve_str,
        'os_ver_code': '25',
        'sign': '%s' % eve_sign,
        'system': '1',
        'timestamp': '%s' % timestamp,
        'video_first_time': '1600048803',
        'video_last_time': '1600045205',
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
