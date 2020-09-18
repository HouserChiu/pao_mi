import json
import time

import requests
from handle_mongo import handle_get_task
from douyin_info_mongo import mongo_info

user_info_url = "https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/accountInfoAll"
headers = {
    'Host': 'xd.newrank.cn',
    'Connection': 'keep-alive',
    'Content-Length': '21',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
    'charset': 'utf-8',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx55778a0d7b3048c4/11/page-frame.html',
}


def get_formdata(task):
    formdata = {
        "uid": "%s" % task['share_id']
    }
    return formdata


while True:
    task = handle_get_task()
    get_formdata(task)
    time.sleep(1)
    response = requests.post(url=user_info_url, headers=headers, data=json.dumps(get_formdata(task)))
    user_info_dict = json.loads(response.text)
    user_info = {}
    try:
        user_info['avatar'] = user_info_dict['data']['avatar']
    except:
        user_info['avatar'] = ""
    user_info['nickname'] = user_info_dict['data']['nickname']
    user_info['account'] = user_info_dict['data']['account']
    user_info['verify'] = user_info_dict['data']['custom_verify']
    user_info['follower_count'] = user_info_dict['data']['follower_count']
    user_info['likes'] = user_info_dict['data']['total_favorited']
    user_info['aweme_count'] = user_info_dict['data']['aweme_count']
    user_info['gender_rate'] = user_info_dict['data']['gender_rate']
    user_info['favorited_follower_rate'] = user_info_dict['data']['favorited_follower_rate']
    user_info['age'] = user_info_dict['data']['age']
    user_info['city'] = user_info_dict['data']['city']
    user_info['constellation_name'] = user_info_dict['data']['constellation_name']
    user_info['content_tags'] = user_info_dict['data']['content_tags']
    mongo_info.insert_item(user_info)
