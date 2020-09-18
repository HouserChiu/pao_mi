import json
import requests
from fans_gender import mongo_info_gender
from fans_total import mongo_info_total
from fans_range import mongo_info_range
from fans_age import mongo_info_age

fans_info_url = "https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/followerAna"
headers = {
    'Host': 'xd.newrank.cn',
    'Connection': 'keep-alive',
    'Content-Length': '21',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
    'charset': 'utf-8',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx55778a0d7b3048c4/14/page-frame.html',
}
formdata = {
    "uid": "63075266947"
}
response = requests.post(url=fans_info_url, headers=headers, data=json.dumps(formdata))
fans_info_dict = json.loads(response.text)

for follower_age in fans_info_dict['data']['follower_age']:
    age_dict = {}
    age_dict['range'] = follower_age['key']
    age_dict['range_rate'] = follower_age['rate']
    print(age_dict)
    mongo_info_age.insert_item(age_dict)

for follower_gender in fans_info_dict['data']['follower_gender']:
    gender_dict = {}
    gender_dict['gender'] = follower_gender['key']
    gender_dict['gender_rate'] = follower_gender['rate']
    print(gender_dict)
    mongo_info_gender.insert_item(gender_dict)

for follower_province in fans_info_dict['data']['follower_province']:
    range_dict = {}
    range_dict['province'] = follower_province['key']
    range_dict['province_rate'] = follower_province['rate']
    print(range_dict)
    mongo_info_range.insert_item(range_dict)

total_dict = {}
total_dict['most_follower_age'] = fans_info_dict['data']['most_follower_age']['key']
total_dict['most_follower_age_rate'] = fans_info_dict['data']['most_follower_age']['rate']
total_dict['most_follower_gender'] = fans_info_dict['data']['most_follower_gender']['key']
total_dict['most_follower_gender_rate'] = fans_info_dict['data']['most_follower_gender']['rate']
total_dict['most_follower_province'] = fans_info_dict['data']['most_follower_province']['key']
total_dict['most_follower_province_rate'] = fans_info_dict['data']['most_follower_province']['rate']
print(total_dict)
mongo_info_total.insert_item(total_dict)
