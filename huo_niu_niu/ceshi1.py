# coding: utf-8
import pymysql
import requests
import json
import pprint
import urllib3

def get_cityId():
    cityId_list = ['5', '9', '27', '28', '21', '7', '26', '24', '18', '19', '30']
    return cityId_list
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Content-Length': '9',
#         'Host': 'hnnapi.huoniuniu.com',
#         'Connection': 'Keep-Alive',
#         'Accept-Encoding': 'gzip',
#         'Cookie': 'CXSESSID=046be14a846f87976c43bb8a0d626cea',
#         'User-Agent': 'okhttp/3.10.0',
#     }
#     url = "https://hnnapi.huoniuniu.com/HNNCity"
#     data = {
#         'version': '1'
#     }
#     res = json.loads(requests.post(url, headers=headers, verify=False, data=data).text)
#     city_id_list = []
#     for temp in res['data']:
#         for eve in temp['list']:
#             city_id = eve['cityId']
#             city_id_list.append(city_id)
#     print(city_id_list)
# get_cityId()

def one_page():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '80',
        'Host': 'hnnapi.huoniuniu.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Cookie': 'CXSESSID=046be14a846f87976c43bb8a0d626cea',
        'User-Agent': 'okhttp/3.10.0',
    }
    url = "https://hnnapi.huoniuniu.com/HNNShop"
    for page in range(1, 101):
        data = {
            'version': '0',
            'pageSize': '30',
            'keyword': '',
            'currentPage': '%s' % page,
            'floorId': '',
            'marketId': '6',
            'type': '3',
            'cityId': '5',
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.post(url, headers=headers, verify=False, data=data).text)
        # pprint.pprint(res)
        for shopIds in res['data']:
            yield shopIds['shopId']


def two_page(shopId):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '59',
        'Host': 'hnnapi.huoniuniu.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Cookie': 'CXSESSID=046be14a846f87976c43bb8a0d626cea',
        'User-Agent': 'okhttp/3.10.0',
    }
    url = "https://hnnapi.huoniuniu.com/HNNShopDetails"
    data = {
        'shopId': '%s' % shopId,
        'uid': 'oAwZ1e9wLWJRo6yAWOXLTA%3D%3D%0A',
        'version': '0',
    }
    res = json.loads(requests.post(url, headers=headers, data=data, verify=False).text)
    store_info_dict = {}
    store_info_dict['shopName'] = res['shopName']
    store_info_dict['mobile'] = res['mobile']
    store_info_dict['weixin'] = res['weixin']
    store_info_dict['category'] = res['category']
    pprint.pprint(store_info_dict)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                           database="gong_xiang_hy",
                           charset="utf8mb4")
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO huo_niu_niu (shopName, mobile, weixin, category) VALUE ('%s','%s','%s','%s')"
        base = (
            store_info_dict['shopName'], store_info_dict['mobile'], store_info_dict['weixin'], store_info_dict['category'])
        cursor.execute(sql % base)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

# def main():
#     shopId_list = one_page()
#     for shopId in shopId_list:
#         two_page(shopId)
#
# if __name__ == '__main__':
#     one_page()
