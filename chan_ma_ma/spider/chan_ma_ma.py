'''
涨粉达人榜
'''
import datetime
from spider.douyin_info_mongo import mongo_info
import requests
import json
from spider.headers import get_headers
from spider.age_mongo import mongo_info_age
from spider.city_mongo import mongo_info_city
from spider.province_mongo import mongo_info_province
from spider.sex_mongo import mongo_info_sex
import urllib3


def get_cmm_kind():
    url = "https://api-service.chanmama.com/v1/common/category"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers(), verify=False).text
    response = json.loads(res)
    kind_list = []
    for cate in response['data']:
        kind_list.append(cate['category'])
    return kind_list


# def get_params():
#     kind_list = get_cmm_kind()
#     params_list = []
#     for kind in kind_list:
#         params = {
#             'category': '%s' % kind,
#             'day_type': 'day',
#             'day': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
#             'page': '1',
#             'size': '50',
#             'is_commerce': '0',
#             'province': ''
#         }
#         params_list.append(params)
#     return params_list

def get_params():
    kind_list = get_cmm_kind()
    params_list = []
    for kind in kind_list:
        params = {
            'date': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
            'page': '1',
            'size': '50',
            'share_type': '0',
            'category': '%s' % kind,
            'province': ''
        }
        params_list.append(params)
    return params_list

def get_id():
    params_list = get_params()
    id_lists = []
    for params in params_list:
        url = "https://api-service.chanmama.com/v1/authorRank/starDailyRank"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = json.loads(requests.get(url, headers=get_headers(), params=params, verify=False).text)
        ids = response['data']['list']
        id_list = []
        for id in ids:
            id_list.append(id['author_id'])
        id_lists.append(id_list)
    return id_lists


def get_detail_info():
    idss = get_id()
    for ids in idss:
        for id in ids:
            url = "https://api-service.chanmama.com/v1/home/author/info?author_id=" + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            user_infos = json.loads(requests.get(url, headers=get_headers(), verify=False).text)
            user_info = {}
            user_info['platform'] = '1'
            user_info['account'] = user_infos['data']['unique_id']
            user_info['name'] = user_infos['data']['nickname']
            user_info['avatar'] = user_infos['data']['avatar']
            # 性别，男为1，女为2
            if user_infos['data']['gender'] == 0:
                user_info['sex'] = '1'
            elif user_infos['data']['gender'] == 1:
                user_info['sex'] = '2'
            else:
                user_info['sex'] = ''
            # 星座
            user_info['stars'] = ''

            if user_infos['data']['birthday'] != '':
                now_year = datetime.datetime.today().year
                birthday = datetime.datetime.strptime(user_infos['data']['birthday'], '%Y-%m-%d').year
                age = now_year - birthday
                user_info['age'] = age
            else:
                user_info['age'] = ''
            user_info['location'] = user_infos['data']['province'] + user_infos['data']['city']
            # 个人简介
            user_info['personal_profile'] = user_infos['data']['signature']
            user_info['mcn'] = ''

            # user_info['total_share'] = user_infos['data']['total_share']
            # 标签
            user_info['label'] = user_infos['data']['verify_name']
            user_info['fans'] = user_infos['data']['follower_count']
            user_info['production'] = user_infos['data']['aweme_count']
            user_info['likes'] = user_infos['data']['total_favorited']
            user_info['url'] = user_infos['data']['url']
            # 所属分类
            user_info['categoryid'] = user_infos['data']['label']
            # 第三方平台id
            user_info['userid'] = id
            print(user_info)
            mongo_info.insert_item(user_info)

            # 获取粉丝年龄分布、地区分布、性别分布
            url_fda = 'https://api-service.chanmama.com/v1/author/fansDataAnalyse?author_id=' + str(id)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            fda_infos = json.loads(requests.get(url_fda, headers=get_headers(), verify=False).text)

            for age_info in fda_infos['data']['age']:
                age_infos = {}
                age_infos['userid'] = id
                age_infos['age'] = age_info['title']
                age_infos['percentage'] = age_info['rate']
                print(age_infos)
                mongo_info_age.insert_item(age_infos)

            for city_info in fda_infos['data']['city']:
                city_infos = {}
                city_infos['userid'] = id
                city_infos['city'] = city_info['title']
                city_infos['percentage'] = city_info['rate']
                print(city_infos)
                mongo_info_city.insert_item(city_infos)

            for province_info in fda_infos['data']['province']:
                province_infos = {}
                province_infos['userid'] = id
                province_infos['province'] = province_info['title']
                province_infos['percentage'] = province_info['rate']
                print(province_infos)
                mongo_info_province.insert_item(province_infos)

            sex_infos = {}
            sex_infos['userid'] = id
            sex_infos['female_rate'] = fda_infos['data']['gender']['female']
            sex_infos['male_rate'] = fda_infos['data']['gender']['male']
            print(sex_infos)
            mongo_info_sex.insert_item(sex_infos)


get_detail_info()
