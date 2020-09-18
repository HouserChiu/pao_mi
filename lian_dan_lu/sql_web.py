'''
带货达人榜
'''
import time

import requests
import json
# from mongo_web import mongo_info
import datetime
import pymysql


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=6990664e-dc36-4fb0-bfae-4bf0aeaae26b; grwng_uid=1b3fd648-ec78-4698-9bcc-6aeb3e11d41d; __51cke__=; 8e22d1b16f393571_gr_session_id=a3d9e1d4-05c8-40f9-8ba8-fa5086b47d9f; 8e22d1b16f393571_gr_session_id_a3d9e1d4-05c8-40f9-8ba8-fa5086b47d9f=true; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1590045505,1590048761,1590109894; __tins__20450359=%7B%22sid%22%3A%201590112101203%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201590115027606%7D; __51laig__=55; JSESSIONID=82E3F97705528453AB8E656AC231F810; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=' + '%s' % str(int(time.time())),
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers

# 请求分类信息
def get_cate():
    url = 'http://www.huo1818.com/live-api/selector/live-category'
    res = json.loads(requests.get(url, headers=get_headers()).text)
    return res['result']


def get_params():
    cates = get_cate()
    cate_list = []
    for cate in cates:
        params = [
            {'tag': '', 'type': '1', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '%s' % cate, 'pageSize': '40', 'pageNo': '1', },
            {'tag': '', 'type': '2', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '%s' % cate, 'pageSize': '40', 'pageNo': '1', },
            {'tag': '', 'type': '5', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '%s' % cate, 'pageSize': '40', 'pageNo': '1', },
            {'tag': '', 'type': '6', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '%s' % cate, 'pageSize': '40', 'pageNo': '1', },
        ]
        cate_list.append(params)
    return cate_list


def get_one():
    temp = get_params()
    for eve in temp:
        for params in eve:
            url = 'http://www.huo1818.com/live-api/v1_2_5/goods/streamer-ranking-list'
            res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
            for result in res['result']['resultList']:
                # user_info = {}
                # user_info['avatar'] = id['avatar']
                # user_info['userName'] = id['userName']
                # user_info['city'] = id['city']
                # user_info['tag'] = id['tag']
                # user_info['gender'] = id['gender']
                # user_info['fansNum'] = id['fansNum']
                avatar = result['avatar']
                username = result['userName']
                city = result['city']
                tag = result['tag']
                gender = result['gender']
                fansnum = result['fansNum']
                print(username)
                conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="test",
                                       charset="utf8mb4")
                cursor = conn.cursor()
                try:
                    sql = "INSERT INTO test_info (avatar, username, city, tag, fansnum, gender) VALUES ('%s','%s','%s','%s','%s','%s')"
                    base = (avatar, username, city, tag, fansnum, gender)
                    cursor.execute(sql % base)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()


# get_one()
