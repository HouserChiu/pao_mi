import json
import requests
from trend_mongo import mongo_info

user_trend_url = "https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/trend"
headers = {
    'Host':'xd.newrank.cn',
    'Connection':'keep-alive',
    'Content-Length':'21',
    'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
    'charset':'utf-8',
    'Accept-Encoding':'gzip,compress,br,deflate',
    'content-type':'application/json',
    'Referer':'https://servicewechat.com/wx55778a0d7b3048c4/14/page-frame.html',
}
formdata = {
    "uid":"63075266947"
}
response = requests.post(url=user_trend_url,headers=headers,data=json.dumps(formdata))
user_trend_dict = json.loads(response.text)
user_trends = user_trend_dict['data']
for user_trend in user_trends:
    trend = {}
    trend['follower_count'] = user_trend['follower_count']
    trend['add_follower_count'] = user_trend['add_follower_count']
    trend['total_favorited'] = user_trend['total_favorited']
    trend['add_total_favorited'] = user_trend['add_total_favorited']
    trend['aweme_count'] = user_trend['aweme_count']
    trend['works_count'] = user_trend['works_count']
    trend['rank_date'] = user_trend['rank_date']
    print(trend)
    mongo_info.insert_item(trend)