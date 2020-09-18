import datetime
from spider.age_mongo import mongo_info_age
from spider.city_mongo import mongo_info_city
from spider.province_mongo import mongo_info_province
from spider.sex_mongo import mongo_info_sex

import requests
import json
from spider.headers import get_headers

def get_cmm_kind():
    url = "https://api-service.chanmama.com/v1/common/category"
    res = requests.get(url, headers=get_headers()).text
    response = json.loads(res)
    kind_list = []
    for cate in response['data']:
        kind_list.append(cate['category'])
    return kind_list

def get_params():
    kind_list = get_cmm_kind()
    params_list = []
    for kind in kind_list:
        params = {
            'category': '%s'%kind,
            'day_type': 'day',
            'day': '2020-05-08',
            'page': '1',
            'size': '50',
            'is_commerce': '0',
            'province': ''
        }
        params_list.append(params)
    return params_list


def get_id():
    params_list = get_params()
    id_lists = []
    for params in params_list:
        url = "https://api-service.chanmama.com/v1/home/author/rank/fans"
        response = json.loads(requests.get(url, headers=get_headers(), params=params).text)
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
            url_fda = 'https://api-service.chanmama.com/v1/author/fansDataAnalyse?author_id=' + str(id)
            fda_infos = json.loads(requests.get(url_fda,headers=get_headers()).text)

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
            sex_infos['user_id'] = id
            sex_infos['female_rate'] = fda_infos['data']['gender']['female']
            sex_infos['male_rate'] = fda_infos['data']['gender']['male']
            print(sex_infos)
            mongo_info_sex.insert_item(sex_infos)

get_detail_info()

