# coding: utf-8
'''
行业榜
'''
import time
import pymysql
import requests
import json
import urllib3



def get_headers():
    headers = {
        'Host': 'miniapi.feigua.cn',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A32) Process/appbrand1 NetType/WIFI Language/zh_CN ABI/arm64',
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx56218e7b5d180c6d/45/page-frame.html',
    }
    return headers


def get_params():
    # tags = ['美女', '帅哥', '搞笑', '情感', '剧情', '美食', '美妆', '种草', '穿搭', '明星', '影视', '游戏', '宠物', '音乐', '舞蹈', '萌娃', '生活',
    #         '健康', '体育', '旅行', '动漫', '创意', '时尚', '母婴', '教育', '职场', '汽车', '家居', '科技', '摄影', '政务', '知识资讯', '办公', '文学',
    #         '手工手绘', '户外']
    tags = ['办公', '文学', '手工手绘', '户外']
    params_list = []
    for tag in tags:
        params = [
            {'sessionId': '42687328977748de9f01d3ff0530271c', 'page': '1', 'tag': '%s' % tag, 'period': 'day',
             '__keyPath': '%7B%22tag%22%3Atrue%7D', },
            {'sessionId': '42687328977748de9f01d3ff0530271c', 'page': '2', 'tag': '%s' % tag, 'period': 'day',
             '__keyPath': '%7B%22tag%22%3Atrue%7D', },
            {'sessionId': '42687328977748de9f01d3ff0530271c', 'page': '3', 'tag': '%s' % tag, 'period': 'day',
             '__keyPath': '%7B%22tag%22%3Atrue%7D', },
        ]
        params_list.append(params)
    return params_list

def get_one():
    params_listss = get_params()
    Id_lists = []
    Sign_lists = []
    for params_lists in params_listss:
        for params in params_lists:
            url = 'https://miniapi.feigua.cn/api/v1/rank/grow'
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
            Id_list = []
            Sign_list = []
            for eve in res['Data']['listData']:
                Id = eve['Id']
                Sign = eve['Sign']
                Id_list.append(Id)
                Sign_list.append(Sign)
            Id_lists.append(Id_list)
            Sign_lists.append(Sign_list)
            time.sleep(3)
    return Id_lists, Sign_lists

def get_detail():
    idss = get_one()[0]
    signss = get_one()[1]
    for ids, signs in zip(idss, signss):
        for id, sign in zip(ids, signs):
            url = 'https://miniapi.feigua.cn/api/v1/blogger/detail'
            params = {
                'sessionId': '42687328977748de9f01d3ff0530271c',
                'id': '%s' % id,
                'sign': '%s' % sign,
            }
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
            user_info = {}
            user_info['platform'] = '10'
            user_info['avatar'] = res['Data']['BloggerInfo']['Avatar']
            user_info['userid'] = id
            user_info['name'] = res['Data']['BloggerInfo']['NickName']
            user_info['url'] = ''

            if res['Data']['BloggerInfo']['Location'] == '未知':
                user_info['location'] = ''
            else:
                user_info['location'] = res['Data']['BloggerInfo']['Location']

            user_info['account'] = res['Data']['BloggerInfo']['UniqueId']
            if res['Data']['BloggerInfo']['Gender'] == '男':
                user_info['sex'] = '1'
            elif res['Data']['BloggerInfo']['Gender'] == '女':
                user_info['sex'] = '2'
            else:
                user_info['sex'] = ''
            if res['Data']['BloggerInfo']['Constellation'] == '未知':
                user_info['stars'] = ''
            else:
                user_info['stars'] = res['Data']['BloggerInfo']['Constellation']
            user_info['personal_profile'] = res['Data']['BloggerInfo']['Signature']
            user_info['label'] = res['Data']['BloggerInfo']['Tags']

            if res['Data']['BloggerInfo']['Age'] == '未知':
                user_info['age'] = ''
            else:
                user_info['age'] = res['Data']['BloggerInfo']['Age']

            user_info['mcn'] = ''
            user_info['categoryid'] = user_info['label']
            fans = float(res['Data']['BloggerInfo']['MPlatform_Fans'].split('w')[0])
            user_info['fans'] = int(fans * 10000)
            if 'w' in res['Data']['BloggerInfo']['LikeCount']:
                likes = float(res['Data']['BloggerInfo']['LikeCount'].split('w')[0])
                user_info['likes'] = int(likes * 10000)
            else:
                likes1 = float(res['Data']['BloggerInfo']['LikeCount'].split('亿')[0])
                user_info['likes'] = int(likes1 * 100000000)
            user_info['production'] = res['Data']['BloggerInfo']['Awemes']
            print(user_info)

            conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
                                   database="test",
                                   charset="utf8mb4")
            cursor = conn.cursor()
            try:
                sql = "INSERT INTO t_from_user_info (platform, avatar, userid, name, url, location, account, sex, stars, personal_profile, label, production, age, mcn, categoryid, fans, likes) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                base = (user_info['platform'], user_info['avatar'], user_info['userid'], user_info['name'],
                        user_info['url'], user_info['location'], user_info['account'], user_info['sex'],
                        user_info['stars'], user_info['personal_profile'], user_info['label'],
                        user_info['production'], user_info['age'], user_info['mcn'], user_info['categoryid'],
                        user_info['fans'], user_info['likes'])
                cursor.execute(sql % base)
                conn.commit()
            except:
                conn.rollback()

            # 获得省份信息
            if res['Data']['Persona'] != None and res['Data']['Persona']['Province'] != []:
                for province_info in res['Data']['Persona']['Province']:
                    province_infos = {}
                    province_infos['userid'] = id
                    province_infos['province'] = province_info['Name']
                    province_infos['percentage'] = float(str(province_info['Ratio']).split('%')[0])
                    print(province_infos)

                    try:
                        sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                        base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
                        cursor.execute(sql2 % base2)
                        conn.commit()
                    except:
                        conn.rollback()

            # 获取城市信息
            if res['Data']['Persona'] != None and res['Data']['Persona']['City'] != []:
                for city_info in res['Data']['Persona']['City']:
                    city_infos = {}
                    city_infos['userid'] = id
                    city_infos['city'] = city_info['Name']
                    city_infos['percentage'] = float(str(city_info['Ratio']).split('%')[0])
                    print(city_infos)

                    try:
                        sql3 = "INSERT INTO t_from_user_city (userid, city, percentage) VALUE ('%s','%s','%s')"
                        base3 = (city_infos['userid'], city_infos['city'], city_infos['percentage'])
                        cursor.execute(sql3 % base3)
                        conn.commit()
                    except:
                        conn.rollback()

            # 获取年龄信息
            if res['Data']['Persona'] != None and res['Data']['Persona']['Age'] != []:
                fans_list = []
                for temp in res['Data']['Persona']['Age']:
                    fans_list.append(temp['value'])
                eve = sum(fans_list)

                for age_info in res['Data']['Persona']['Age']:
                    age_infos = {}
                    age_infos['userid'] = id
                    age_infos['age'] = age_info['name']
                    age_infos['percentage'] = round(age_info['value'] / eve * 100, 2)
                    print(age_infos)

                    try:
                        sql4 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
                        base4 = (age_infos['userid'], age_infos['age'], age_infos['percentage'])
                        cursor.execute(sql4 % base4)
                        conn.commit()
                    except:
                        conn.rollback()

            # 获取星座信息
            if res['Data']['Persona'] != None and res['Data']['Persona']['Constellation'] != []:
                for stars_info in res['Data']['Persona']['Constellation']:
                    stars_infos = {}
                    stars_infos['userid'] = id
                    stars_infos['stars_name'] = stars_info['Name']
                    stars_infos['percentage'] = float(str(stars_info['Ratio']).split('%')[0])
                    print(stars_infos)

                    try:
                        sql5 = "INSERT INTO t_from_user_stars (userid, stars_name, percentage) VALUE ('%s','%s','%s')"
                        base5 = (stars_infos['userid'], stars_infos['stars_name'], stars_infos['percentage'])
                        cursor.execute(sql5 % base5)
                        conn.commit()
                    except:
                        conn.rollback()

            # 获得性别信息
            if res['Data']['Persona'] != None and res['Data']['Persona']['Gender'] != []:
                sex_infos = {}
                sex_infos['userid'] = id
                sex_infos['female_rate'] = float(str(res['Data']['Persona']['Gender'][1]).split('%')[0])
                sex_infos['male_rate'] = float(str(res['Data']['Persona']['Gender'][0]).split('%')[0])
                print(sex_infos)

                try:
                    sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                    base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                    cursor.execute(sql6 % base6)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()
            time.sleep(3)
get_detail()






