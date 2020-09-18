# coding: utf-8
'''
网页版抖音红人榜，20条/天。会员200条/天
'''
import time
import pymysql
import requests
import json
import datetime
import re
import urllib3
from head import get_headers, get_d1, get_d2, get_d3, get_d4, get_d5
from cate import get_label


'''
使用eval函数不能将正则表达式匹配的结果转化为列表，
所以使用逗号进行分割转化为列表，
切片过滤干扰项，再对每一项使用正则拿到分类id
'''
def get_cat():
#     url = 'https://www.duanyuer.com/rank/celebrity/total'
#     params = {
#         'page': '1',
#         'date': '%s' % datetime.datetime.now().strftime('%Y - %m - %d'),
#         'category': '',
#     }
#     res = requests.get(url, params=params, headers=get_headers()).text
#     eve = re.search('navs.*?\[(.*?)\]', res, re.S).group(1).split(',')[2:]
#     id_list = []
#     for temp in eve:
#         if 'id' in temp:
#             id = re.search('id.*?(\d+)', temp, re.S).group(1)
#             id_list.append(id)
#     print(id_list)
#
# get_cat()
    cateId = ['10117', '10126', '10124', '10127', '10118', '10132', '10125', '10130', '10137', '10135', '10129', '10131', '10139', '10136', '10144', '10154', '10138', '10142', '10151', '10128', '10133', '10134', '10146', '10147', '10148', '10149', '10153', '10155']
    return cateId

def get_params():
    cate_list = get_cat()
    params_list = []
    for cate in cate_list:
        params = [
            {'page': '1', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '2', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '3', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '4', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '5', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '6', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '7', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '8', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '9', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
            {'page': '10', 'date': '%s' % datetime.datetime.now().strftime('%Y-%m-%d'), 'category': '%s' % cate, },
        ]
        params_list.append(params)
    # print(params_list)
    return params_list

def get_one():
    params_lists = get_params()
    id_lists = []
    for params_list in params_lists:
        for params in params_list:
            url = 'https://www.duanyuer.com/rank/celebrity/total'
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = requests.get(url, params=params, headers=get_headers(), verify=False).text
            eve = re.search('userList.*?\[(.*?)\]', res, re.S).group(1).split(',')
            id_list = []
            for temp in eve:
                if 'dyuserId' in temp:
                    id = re.search('dyuserId.*?\"(.*?)\"', temp, re.S).group(1)
                    id_list.append(id)
            id_lists.append(id_list)
            time.sleep(10)
    return id_lists

def get_two():
    idss = get_one()
    for ids in idss:
        for id in ids:
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'content-length': '11',
                'content-type': 'application/x-www-form-urlencoded',
                'd1': '%s' % get_d1(),
                'd2': '%s' % get_d2(),
                'd3': '%s' % get_d3(),
                'd4': '%s' % get_d4(),
                'd5': '%s' % get_d5(),
                'origin': 'https://www.duanyuer.com',
                'referer': 'https://www.duanyuer.com/user/00049h3u',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
            }
            url = 'https://xcx.meizhuahuyu.com/douyin/user/getUserDetail'
            params = {
                'token': '972f5ec2c383ad0d85823648b2ad68a2',
                'toPageCode': '18',
            }
            data = {
                'id': '%s' % id,
            }
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.post(url, params=params, data=data, headers=headers, verify=False).text)
            user_info = {}
            user_info['platform'] = '9'
            user_info['avatar'] = res['result']['avatar']
            user_info['userid'] = id
            user_info['name'] = res['result']['douyinName']
            user_info['url'] = res['result']['qrcodeUrl']
            user_info['location'] = res['result']['city']
            user_info['account'] = res['result']['douyinShortId']
            if res['result']['gender'] == 1:
                user_info['sex'] = '2'
            elif res['result']['gender'] == 2:
                user_info['sex'] = ''
            else:
                user_info['sex'] = '1'
            if res['result']['constellation'] == '未知':
                user_info['stars'] = ''
            else:
                user_info['stars'] = res['result']['constellation']
            user_info['personal_profile'] = res['result']['constellation']
            if res['result']['tagList'] == []:
                user_info['label'] = ''
            else:
                user_info['label'] = get_label()[res['result']['tagList'][0]]

            if res['result']['birthday'] == '':
                user_info['age'] = ''
            else:
                now_year = datetime.datetime.today().year
                birthday = datetime.datetime.strptime(res['result']['birthday'], '%Y-%m-%d').year
                age = now_year - birthday
                user_info['age'] = age

            if res['result']['mcnName'] == 'null':
                user_info['mcn'] = ''
            else:
                user_info['mcn'] = res['result']['mcnName']

            if res['result']['tagList'] == []:
                user_info['categoryid'] = ''
            else:
                user_info['categoryid'] = get_label()[res['result']['tagList'][0]]
            user_info['fans'] = res['result']['fansNumber']
            user_info['likes'] = res['result']['likeNumber']
            user_info['production'] = res['result']['videoNumber']
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

            url1 = 'https://xcx.meizhuahuyu.com/douyin/user/web/userfans'
            params1 = {
                'token': '972f5ec2c383ad0d85823648b2ad68a2',
                'toPageCode': '18',
                'dyuserId': '%s' % id
            }
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            headers.pop('content-length')
            headers.pop('content-type')
            res1 = json.loads(requests.get(url1, params=params1, headers=headers, verify=False).text)

            if res1['msg'] != 'succ':
                pass
            else:
                if res1['result']['data'] != None:
                    # 获取省份信息
                    result = sum(res1['result']['data']['gender'])
                    for province_list, percentage_list in zip(res1['result']['province_x'], res1['result']['data']['area']):
                        province_infos_list = {}
                        province_infos_list['userid'] = id
                        province_infos_list['province'] = province_list
                        province_infos_list['percentage'] = round(percentage_list / result * 100, 2)
                        print(province_infos_list)
                        try:
                            sql1 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                            base1 = (
                            province_infos_list['userid'], province_infos_list['province'], province_infos_list['percentage'])
                            cursor.execute(sql1 % base1)
                            conn.commit()
                        except:
                            conn.rollback()

                    # 获取星座信息
                    for star_list, star_rate_list in zip(res1['result']['constellation_x'],
                                                         res1['result']['data']['constellation']):
                        stars_infos = {}
                        stars_infos['userid'] = id
                        stars_infos['stars_name'] = star_list
                        stars_infos['percentage'] = round(star_rate_list / result * 100, 2)
                        print(stars_infos)
                        try:
                            sql5 = "INSERT INTO t_from_user_stars (userid, stars_name, percentage) VALUE ('%s','%s','%s')"
                            base5 = (stars_infos['userid'], stars_infos['stars_name'], stars_infos['percentage'])
                            cursor.execute(sql5 % base5)
                            conn.commit()
                        except:
                            conn.rollback()

                    # 获取年龄信息
                    for age_list, age_rate_list in zip(res1['result']['constellation_x'],
                                                       res1['result']['data']['constellation']):
                        age_infos_list = {}
                        age_infos_list['userid'] = id
                        age_infos_list['age'] = age_list
                        age_infos_list['percentage'] = round(age_rate_list / result * 100, 2)
                        print(age_infos_list)
                        try:
                            sql3 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
                            base3 = (age_infos_list['userid'], age_infos_list['age'], age_infos_list['percentage'])
                            cursor.execute(sql3 % base3)
                            conn.commit()
                        except:
                            conn.rollback()

                    # 获取性别信息
                    sex_infos_list = {}
                    sex_infos_list['userid'] = id
                    sex_infos_list['female_rate'] = round(
                        res1['result']['data']['gender'][1] / result, 2)
                    sex_infos_list['male_rate'] = round(
                        res1['result']['data']['gender'][0] / result, 2)
                    print(sex_infos_list)
                    try:
                        sql7 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                        base7 = (sex_infos_list['userid'], sex_infos_list['female_rate'], sex_infos_list['male_rate'])
                        cursor.execute(sql7 % base7)
                        conn.commit()
                    except:
                        conn.rollback()

                else:
                    # 获得省份信息
                    for province_key, province_value in zip(eval(res1['result']['provinceDist']).keys(),
                                                            eval(res1['result']['provinceDist']).values()):
                        province_infos = {}
                        province_infos['userid'] = id
                        province_infos['province'] = province_key
                        province_infos['percentage'] = round(
                            province_value / sum(eval(res1['result']['provinceDist']).values()) * 100, 2)
                        print(province_infos)

                        try:
                            sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                            base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
                            cursor.execute(sql2 % base2)
                            conn.commit()
                        except:
                            conn.rollback()

                    # 获得年龄信息
                    for age_key, age_value in zip(eval(res1['result']['ageDist']).keys(),
                                                  eval(res1['result']['ageDist']).values()):
                        age_infos = {}
                        age_infos['userid'] = id
                        age_infos['age'] = age_key
                        age_infos['percentage'] = round(age_value / sum(eval(res1['result']['ageDist']).values()) * 100, 2)
                        print(age_infos)

                        try:
                            sql4 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
                            base4 = (age_infos['userid'], age_infos['age'], age_infos['percentage'])
                            cursor.execute(sql4 % base4)
                            conn.commit()
                        except:
                            conn.rollback()

                    # 获得性别信息
                    sex_infos = {}
                    sex_infos['userid'] = id
                    sex_infos['female_rate'] = round(
                        eval(res1['result']['sexDist'])['female'] / sum(eval(res1['result']['ageDist']).values()), 2)
                    sex_infos['male_rate'] = round(
                        eval(res1['result']['sexDist'])['male'] / sum(eval(res1['result']['ageDist']).values()), 2)
                    print(sex_infos)

                    try:
                        sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                        base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                        cursor.execute(sql6 % base6)
                        conn.commit()
                    except:
                        conn.rollback()
                    conn.close()
            time.sleep(10)
# get_two()
























