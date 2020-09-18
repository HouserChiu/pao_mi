# coding: utf-8

import pprint
import pymysql
import requests
import json
import time
import hashlib
import urllib3

def get_userId():
    ori_str = "7iIpa1FBzNP2rczAugpPDrEa"
    timestamp = str(int(round(time.time() * 1000)))
    encrypt_str = timestamp + ori_str
    signature = hashlib.md5(encrypt_str.encode('utf-8')).hexdigest()
    headers = {
        'X-LC-Prod': '1',
        'X-LC-Id': 'npYeswjbL2eFP7nJ0MzSR9mq-9Nh9j0Va',
        'X-LC-Sign': '%s' % signature + ',' + '%s' % timestamp,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'LeanCloud-Java-SDK/6.5.0',
        'X-LC-Session': 'zak1msijnzyd7n96wjjk50lzy',
        'Host': 'east.awsyt.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    userId_url = "https://east.awsyt.com/1.1/classes/Home_shopList?order=-createdAt&include=shopList&limit=100"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.get(userId_url, headers=headers, verify=False).text)
    for Id_temp in res['results']:
        yield Id_temp['userID']


def get_result(userID):
    ori_str = "7iIpa1FBzNP2rczAugpPDrEa"
    timestamp = str(int(round(time.time() * 1000)))
    encrypt_str = timestamp + ori_str
    signature = hashlib.md5(encrypt_str.encode('utf-8')).hexdigest()
    headers = {
        'X-LC-Prod': '1',
        'X-LC-Id': 'npYeswjbL2eFP7nJ0MzSR9mq-9Nh9j0Va',
        'X-LC-Sign': '%s' % signature + ',' + '%s' % timestamp,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'LeanCloud-Java-SDK/6.5.0',
        'X-LC-Session': 'zak1msijnzyd7n96wjjk50lzy',
        'Host': 'east.awsyt.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    detail_url = "https://east.awsyt.com/1.1/classes/_User/" + "%s" % userID
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    store_info = json.loads(requests.get(detail_url, headers=headers, verify=False).text)
    store_info_dict = {}
    store_info_dict['nickName'] = store_info['nickName']
    store_info_dict['wechatNumber'] = store_info['wechatNumber']
    store_info_dict['phoneNumber'] = store_info['phoneNumber']
    pprint.pprint(store_info_dict)

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                           database="gong_xiang_hy",
                           charset="utf8mb4")
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO ws_yuantou (nickName, wechatNumber, phoneNumber) VALUE ('%s','%s','%s')"
        base = (store_info_dict['nickName'], store_info_dict['wechatNumber'], store_info_dict['phoneNumber'])
        cursor.execute(sql % base)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def main():
    userID_list = get_userId()
    for userID in userID_list:
        get_result(userID)

if __name__ == '__main__':
    main()
