'''
带货达人榜
更新cookie
'''
import time
import pymysql
import requests
import json
import datetime


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': '__51cke__=; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1593755904; gr_user_id=98d82053-e510-436a-91e5-7cda231b3cea; 8e22d1b16f393571_gr_session_id=74db60cd-124c-491c-9792-585069d82095; 8e22d1b16f393571_gr_session_id_74db60cd-124c-491c-9792-585069d82095=true; grwng_uid=d887999d-238b-43e9-8459-b664352cbddb; JSESSIONID=E06062B1B8F8CFB93A1A824AB74C7431; __tins__20450359=%7B%22sid%22%3A%201593755903583%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201593757754077%7D; __51laig__=3; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1593755955',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def get_cate():
    url = 'http://www.huo1818.com/live-api/selector/live-category'
    res = json.loads(requests.get(url, headers=get_headers()).text)
    return res['result']


def get_params(cate):
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

    yield params


def get_one(params):
    url = 'http://www.huo1818.com/live-api/v1_2_5/goods/streamer-ranking-list'
    res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
    for id in res['result']['resultList']:
        yield id['streamerId']

# get_one()
    # return Id_lists


def get_detail(id):
    url = 'http://www.huo1818.com/live-api/streamer/info?streamerId={}'.format(id)
    res = json.loads(requests.get(url, headers=get_headers()).text)
    if res['success'] == True:
        user_info = {}
        user_info['platform'] = '2'

        user_info['avatar'] = res['result']['avatar']
        # 第三方ID
        user_info['userid'] = res['result']['streamerId']
        user_info['name'] = res['result']['userName']
        # 快手主页
        user_info['url'] = res['result']['link']
        user_info['location'] = res['result']['city']
        # 快手号
        user_info['account'] = res['result']['kwaiId']
        # 男为0，女为1
        if res['result']['gender'] == 2:
            user_info['sex'] = '2'
        else:
            user_info['sex'] = '1'
        # 星座
        user_info['stars'] = res['result']['horoscope']
        # 直播地址
        # user_info['liveLink'] = res['result']['liveLink']
        # 个人简介
        user_info['personal_profile'] = res['result']['brief']
        # 主营
        # user_info['mainCategoryName'] = res['result']['mainCategoryName']
        # 标签
        user_info['label'] = res['result']['tag']
        # 更新时间
        # user_info['updatedAt'] = res['result']['updatedAt']
        # 收录时间
        # user_info['createdAt'] = res['result']['createdAt']
        # 作品数
        user_info['production'] = res['result']['productNum']
        user_info['age'] = ''
        user_info['mcn'] = ''
        user_info['categoryid'] = ''
        user_info['fans'] = res['result']['fansNum']

        # 直播观众峰值
        # user_info['maxWatchNum'] = res['result']['maxWatchNum']
        user_info['likes'] = res['result']['maxLikeCount']
        # user_info['maxViewCount'] = res['result']['maxViewCount']
        # 打赏次数
        # user_info['rewardNumOut'] = res['result']['rewardNumOut']
        print(user_info)
                # mongo_info.insert_item(user_info)
        #         conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
        #                                database="test",
        #                                charset="utf8mb4")
        #         cursor = conn.cursor()
        #         try:
        #             sql = "INSERT INTO t_from_user_info (platform, avatar, userid, name, url, location, account, sex, stars, personal_profile, label, production, age, mcn, categoryid, fans, likes) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        #             base = (user_info['platform'], user_info['avatar'], user_info['userid'], user_info['name'],
        #                     user_info['url'], user_info['location'], user_info['account'], user_info['sex'],
        #                     user_info['stars'], user_info['personal_profile'], user_info['label'],
        #                     user_info['production'], user_info['age'], user_info['mcn'], user_info['categoryid'],
        #                     user_info['fans'], user_info['likes'])
        #             cursor.execute(sql % base)
        #             conn.commit()
        #         except:
        #             conn.rollback()
        #         conn.close()
        # time.sleep(2)

# get_detail()
def main(cate):
    params_lists = get_params(cate)
    for params_list in params_lists:
        for params in params_list:
            # print(params)
            ids = get_one(params)
            for id in ids:
                get_detail(id)


if __name__ == '__main__':
    cates = get_cate()
    for cate in cates:
        main(cate)


