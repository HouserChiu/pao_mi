'''
直播收入榜，粉丝排行榜，土豪打赏榜，创作达人榜
更新cookie
修改两处url
'''
import time
import requests
import json
import datetime
import pymysql


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=3bb57c6b-679d-454c-9c06-2683109e4889; 8e22d1b16f393571_gr_session_id=e52bfbad-f70d-4932-baec-4ab97168577f; __51cke__=; 8e22d1b16f393571_gr_session_id_e52bfbad-f70d-4932-baec-4ab97168577f=true; grwng_uid=95502437-1e8d-40ac-9116-e3f492e799c8; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592961783; __tins__20450359=%7B%22sid%22%3A%201592961782377%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201592963671868%7D; __51laig__=3; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592961872; JSESSIONID=A4CDA2CF2A363F5C7021EF126324B7A6',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers


def get_cate():
    url = 'http://www.huo1818.com/live-api/selector/tags'
    res = json.loads(requests.get(url, headers=get_headers()).text)
    cate_list = []
    for cate in res['result']:
        cate_list.append(cate['tag'])
    return cate_list


def get_params():
    cates = get_cate()
    cate_list = []
    for cate in cates:
        params = [
            {'tag': '%s' % cate, 'type': '6', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '7', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },



        ]
        cate_list.append(params)
    return cate_list
    # print(cate_list)

# get_params()


def get_one():
    temp = get_params()
    Id_lists = []
    for eve in temp:
        for params in eve:
            url = 'http://www.huo1818.com/live-api/v1_2/ranking-list/live-ranking-list'
            res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
            Id_list = []
            for id in res['result']['resultList']:
                Id_list.append(id['streamerId'])
            Id_lists.append(Id_list)
    return Id_lists


def get_detail():
    idss = get_one()
    # user_list = []
    for ids in idss:
        for id in ids:
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
                conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129", database="test",
                                       charset="utf8mb4")
                cursor = conn.cursor()
                try:
                    sql = "INSERT INTO t_from_user_info (platform, avatar, userid, name, url, location, account, sex, stars, personal_profile, label, production, age, mcn, categoryid, fans, likes) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    base = (user_info['platform'], user_info['avatar'], user_info['userid'], user_info['name'], user_info['url'], user_info['location'], user_info['account'], user_info['sex'], user_info['stars'], user_info['personal_profile'], user_info['label'], user_info['production'], user_info['age'], user_info['mcn'], user_info['categoryid'], user_info['fans'], user_info['likes'])
                    cursor.execute(sql % base)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()

                # user_info.pop("_id")
                # user_list.append(user_info)
    # return user_list
        time.sleep(2)

# get_detail()


