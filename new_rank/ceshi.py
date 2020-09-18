import json
import requests
from nr_spider import get_headers
import urllib3
# url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/followerAna'
# data = '{"uid":"4366902061964508"}'
# res = json.loads(requests.post(url,data=data,headers=get_headers()).text)
# print(res['data']['follower_gender'])

# def integers_1():
#     for i in range(4):
#         yield i + 1
#
# def integers_2():
#     for i in range(4):
#         value = yield i + 1
#
# for n in integers_1():
#     print(n)
import datetime


def one_page():
    url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/rank/hotAccountAllRankList'
    datas = '{"type":"娱乐","date_type":"days","date":"2020-07-01","start":1,"size":20}'
    data = datas.encode('utf-8')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(url, data=data, headers=get_headers(), verify=False, allow_redirects=False).text)
    print(res)
one_page()