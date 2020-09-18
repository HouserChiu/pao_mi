'''
热度榜
headers中的cookie和deviceId需要改
data中的s_fdStartTime需要更改，平时提前1天，周末提前2天，否则会提示请购买相关权限

'''
import time
import pymysql
import requests
import json
import urllib3
import datetime
from requests_toolbelt import MultipartEncoder
from lw_headers import get_headers2


def get_cate():
    '''
    直接设置一个请求头拿到cate之后写死
    :return:
    '''
    # url = 'https://www.luonet.com/api/douyinLabel/listAll'
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # res = json.loads(requests.get(url, headers=get_headers1(), verify=False).text)
    # cate_list = []
    # for cate in res:
    #     cate_list.append(cate['fdName'])
    # print(cate_list)
    cate_list = ['财经投资', '二次元', '三农', '园艺']
    return cate_list
# get_cate()

def get_params():
    '''
    获得data参数，请求头中采用multipart/form-data编码，需要用MultipartEncoder方法
    :return:
    '''
    cate_list = get_cate()
    params_list = []
    for cate in cate_list:
        params = {
            # 's_fdStartTime': '%s 00:00:00' % ((datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')),
            's_fdStartTime': '2020-06-08 00:00:00',
            's_fdType': '1',
            's_Like_fdArea': '',
            's_MATCH_fdLabels': '%s' % cate,
            's_fdGrade': '',
            'pageIndex': '1',
            'reLoad': 'false',
            'limit': '30',
        }
        params_list.append(params)
    return params_list


def get_one():
    '''
    通过一级页面获得uid，headers需要传到2级页面，两次请求保持一致
    调用get_headers2()函数后，获得列表中的两个请求头，这里使用第一个请求头
    :return:
    '''
    params_list = get_params()
    headers_lists = []
    id_lists = []
    for data in params_list:
        url = 'https://www.luonet.com/dcapi/api/douyinUserReport/list'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            m = MultipartEncoder(data)
            headers_temp = get_headers2()
            headers = headers_temp[0]
            headers['Content-Type'] = m.content_type
            res = json.loads(requests.post(url, headers=headers, data=m, verify=False, timeout=10).text)
            id_list = []
            headers_list = []
            for id in res['rows']:
                id_list.append(id['fdUid'])
                headers_list.append(headers_temp)
            id_lists.append(id_list)
            headers_lists.append(headers_list)
        except KeyError:
            pass
    return id_lists, headers_lists


def get_two():
    '''
    两次循环之后得到列表中包含列表中的两个请求头，这里用第2个
    :return:
    '''
    idss = get_one()[0]
    headersss = get_one()[1]
    for ids, headerss in zip(idss, headersss):
        for id, headers in zip(ids, headerss):
            # 获得用户基本信息
            url = 'https://www.luonet.com/api/douyinUserInfo/fdUid/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, headers=headers[1], verify=False).text)
            user_info = {}
            user_info['platform'] = '7'
            user_info['avatar'] = res['fdAvatar']
            user_info['userid'] = id
            user_info['name'] = res['fdName']
            user_info['url'] = res['fdLink']
            user_info['location'] = res['fdArea']
            user_info['account'] = res['fdCode']
            if res['fdSex'] == 1:
                user_info['sex'] = '1'
            elif res['fdSex'] == 2:
                user_info['sex'] = '2'
            else:
                user_info['sex'] = ''
            if res['fdConstellation'] == '未知星座':
                user_info['stars'] = ''
            else:
                user_info['stars'] = res['fdConstellation']
            user_info['personal_profile'] = res['fdSignature']
            user_info['label'] = res['fdLabels']

            if res['fdBirthday'] == 'null' or res['fdBirthday'] == None:
                user_info['age'] = ''
            else:
                now_year = datetime.datetime.today().year
                birthday = datetime.datetime.strptime(res['fdBirthday'], '%Y-%m-%d %H:%M:%S').year
                age = now_year - birthday
                user_info['age'] = age

            user_info['mcn'] = res['fdMcnName']
            user_info['categoryid'] = res['fdLabels']
            user_info['fans'] = res['fdFansNum']
            user_info['likes'] = res['fdLikeNum']
            url1 = 'https://www.luonet.com/api/douyinUserReport/getDataConclude/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res1 = json.loads(requests.get(url1, headers=headers[1], verify=False).text)
            user_info['production'] = res1['fdPublishTotal']
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
            url2 = 'https://www.luonet.com/api/douyinUserFansReport/getProvinceData/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res2 = json.loads(requests.get(url2, headers=headers[1], verify=False).text)
            for province_info in res2:
                try:
                    province_infos = {}
                    province_infos['userid'] = id
                    province_infos['province'] = province_info['name']
                    province_infos['percentage'] = float(float(province_info['value']) * 100)
                    print(province_infos)
                except TypeError and KeyError:
                    pass
                try:
                    sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                    base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
                    cursor.execute(sql2 % base2)
                    conn.commit()
                except:
                    conn.rollback()

            # 获得城市信息
            url3 = 'https://www.luonet.com/api/douyinUserFansReport/getCityData/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res3 = json.loads(requests.get(url3, headers=headers[1], verify=False).text)
            for city_info in res3:
                try:
                    city_infos = {}
                    city_infos['userid'] = id
                    city_infos['city'] = city_info['name']
                    city_infos['percentage'] = float(float(city_info['value']) * 100)
                    print(city_infos)
                except TypeError and KeyError:
                    pass
                try:
                    sql3 = "INSERT INTO t_from_user_city (userid, city, percentage) VALUE ('%s','%s','%s')"
                    base3 = (city_infos['userid'], city_infos['city'], city_infos['percentage'])
                    cursor.execute(sql3 % base3)
                    conn.commit()
                except:
                    conn.rollback()

            # 获得年龄信息
            url4 = 'https://www.luonet.com/api/douyinUserFansReport/getAgeData/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res4 = json.loads(requests.get(url4, headers=headers[1], verify=False).text)
            for age_info in res4:
                try:
                    age_infos = {}
                    age_infos['userid'] = id
                    age_infos['age'] = age_info['name']
                    age_infos['percentage'] = float(float(age_info['value']) * 100)
                    print(age_infos)
                except TypeError and KeyError:
                    pass

                try:
                    sql4 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
                    base4 = (age_infos['userid'], age_infos['age'], age_infos['percentage'])
                    cursor.execute(sql4 % base4)
                    conn.commit()
                except:
                    conn.rollback()

            # 获得星座信息
            url5 = 'https://www.luonet.com/api/douyinUserFansReport/getConstellationData/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res5 = json.loads(requests.get(url5, headers=headers[1], verify=False).text)
            for stars_info in res5:
                try:
                    stars_infos = {}
                    stars_infos['userid'] = id
                    stars_infos['stars_name'] = stars_info['name']
                    stars_infos['percentage'] = float(float(stars_info['value']) * 100)
                    print(stars_infos)
                except TypeError and KeyError:
                    pass
                try:
                    sql5 = "INSERT INTO t_from_user_stars (userid, stars_name, percentage) VALUE ('%s','%s','%s')"
                    base5 = (stars_infos['userid'], stars_infos['stars_name'], stars_infos['percentage'])
                    cursor.execute(sql5 % base5)
                    conn.commit()
                except:
                    conn.rollback()

            # 获得性别信息
            url6 = 'https://www.luonet.com/api/douyinUserFansReport/getSexData/' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            try:
                res6 = json.loads(requests.get(url6, headers=headers[1], verify=False).text)
                sex_infos = {}
                sex_infos['userid'] = id
                sex_infos['female_rate'] = float(float(res6[0]['value']) * 100)
                sex_infos['male_rate'] = float(float(res6[1]['value']) * 100)
                print(sex_infos)
            except IndexError and TypeError and KeyError:
                pass
            try:
                sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                cursor.execute(sql6 % base6)
                conn.commit()
            except:
                conn.rollback()
            conn.close()
# get_two()

