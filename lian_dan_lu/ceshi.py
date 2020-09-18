# import requests
# import json
# import datetime
# import urllib.parse
#
#
# def reg():
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/json;charset=utf-8',
#         'Cookie': 'gr_user_id=6990664e-dc36-4fb0-bfae-4bf0aeaae26b; grwng_uid=1b3fd648-ec78-4698-9bcc-6aeb3e11d41d; __51cke__=; 8e22d1b16f393571_gr_session_id=c0012ae8-fbc4-4fde-a5b4-01981532006b; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1590045505,1590048761,1590109894,1590135808; 8e22d1b16f393571_gr_session_id_c0012ae8-fbc4-4fde-a5b4-01981532006b=true; __tins__20450359=%7B%22sid%22%3A%201590135807427%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201590138164909%7D; __51laig__=5; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1590136365; JSESSIONID=1C6B938C2BA71007034930B4509CB7F1',
#         'Host': 'www.huo1818.com',
#         'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
#         'Referer': 'http://www.huo1818.com/ranking/goods',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     url = 'http://www.huo1818.com/live-api/v1_2_5/goods/streamer-ranking-list'
#     params = {'tag': '', 'type': '1', 'granularity': '1',
#               'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
#               'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
#               'goodsType': '', 'liveCategoryName': '美妆个护', 'pageSize': '40', 'pageNo': '1', }
#     res = json.loads(requests.get(url, headers=headers, params=params).text)
#     # for nickname in res['result']['resultList']:
#     #     user_info = {}
#     #     user_info['nickname'] = nickname['userName']
#     #     # print(json.dumps(user_info))
#     #     return user_info
#     city = res['result']['resultList'][0]['city']
#     print(city)
#     # print(type(city))
#     # return city
#
# reg()

# import datetime
#
# time = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
#
# print(time)

# import pymongo
# import web_spider
# from pymongo.collection import Collection


# def gender_female():
#     web_spider.get_detail()
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     mydb = myclient["ldl_info"]
#     mycol = mydb["ldl_info_data"]
#     # 删除_id字段
#     # mycol.update({}, {'$unset': {'_id': ''}}, False, True)
#     # 查询gender字段为1的数据，1代表女，并遍历
#     gender_woman = []
#     for temp in mycol.find({"gender": "1"}, {"_id": 0}):
#         # eve = str(temp['_id'])
#         gender_woman.append(temp)
#     print(gender_woman)
#
#
# gender_female()

# from flask import Flask, jsonify
# import requests
# app = Flask(__name__)
#
# @app.route('/index')
# def index():
#     return "123"
#
# @app.route('/index/cate')
# def cate():
#     res = requests.get("http://127.0.0.1:5000/index").text
#     print(res)
#     rr = res + "hhh"
#     return rr
#
# if __name__ == '__main__':
#     app.run()

# import datetime
# print(((datetime.datetime.now() + datetime.timedelta(days=-8)).strftime('%Y-%m-%d')))
# import pymysql
# import requests
# import json
# from online_retailers_analyse import get_headers
#
# url = 'http://www.huo1818.com/live-api/v1_2_1/streamer/goods-range-trend?streamerId=1057874280&startDate=2020-06-16&endDate=2020-06-22&liveCategoryName='
# res = json.loads(requests.get(url, headers=get_headers()).text)
# count_list = []
# for sum_temp in res['result']:
#     count_list.append(sum_temp['goodsNum'])
# count_temp = sum(count_list)
#
# for temp in res['result']:
#     goods_trend = {}
#     goods_trend['userid'] = '1111'
#     goods_trend['goods_num'] = temp['goodsNum']
#     if count_temp != 0:
#         goods_trend['goods_rate'] = round((temp['goodsNum'] / count_temp) * 100, 2)
#     else:
#         goods_trend['goods_rate'] = 0.00
#     goods_trend['goods_category'] = temp['liveCategoryName']
#     goods_trend['sell_count'] = temp['sellCount']
#     goods_trend['sell_amount'] = temp['sellAmount']
#     print(goods_trend)
import json

import requests
from web_spider import get_headers
# url = 'http://www.huo1818.com/live-api/v1_2/streamer/horoscope-portrait-v2?streamerId=1951804829'
# res = requests.get(url, headers=get_headers()).text
# print(res)

params = {'tag': '', 'type': '1', 'granularity': '1', 'startDate': '2020-07-02', 'endDate': '2020-07-02', 'goodsType': '', 'liveCategoryName': '美妆个护', 'pageSize': '40', 'pageNo': '1'}
url = 'http://www.huo1818.com/live-api/v1_2_5/goods/streamer-ranking-list'
res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
for id in res['result']['resultList']:
    print(id)
