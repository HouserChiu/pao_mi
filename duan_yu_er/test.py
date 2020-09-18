# import time
# import pymysql
# import requests
# import json
# import datetime
# import re
# import urllib3
# from head import get_headers, get_d1, get_d2, get_d3, get_d4, get_d5
# from cate import get_label
#
# # headers = {
# #     'accept': 'application/json, text/plain, */*',
# #     'accept-encoding': 'gzip, deflate, br',
# #     'accept-language': 'zh-CN,zh;q=0.9',
# #     'content-length': '11',
# #     'content-type': 'application/x-www-form-urlencoded',
# #     'd1': '%s' % get_d1(),
# #     'd2': '%s' % get_d2(),
# #     'd3': '%s' % get_d3(),
# #     'd4': '%s' % get_d4(),
# #     'd5': '%s' % get_d5(),
# #     'origin': 'https://www.duanyuer.com',
# #     'referer': 'https://www.duanyuer.com/user/00049h3u',
# #     'sec-fetch-dest': 'empty',
# #     'sec-fetch-mode': 'cors',
# #     'sec-fetch-site': 'cross-site',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
# # }
# # headers.pop('content-length')
# # headers.pop('content-type')
# # url1 = 'https://xcx.meizhuahuyu.com/douyin/user/web/userfans'
# # params1 = {
# #     'token': '11fbd2336ca6848d064eca2a80d0fde8',
# #     'toPageCode': '18',
# #     'dyuserId': '00qBjrKO'
# # }
# # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# #
# # res1 = json.loads(requests.get(url1, params=params1, headers=headers, verify=False).text)
#
#
# # for key, temp in zip(eval(res1['result']['provinceDist']).keys(), eval(res1['result']['provinceDist']).values()):
# #     province_infos = {}
# #     # province_infos['userid'] = id
# #     province_infos['province'] = key
# #     province_infos['percentage'] = round(temp / sum(eval(res1['result']['provinceDist']).values()) * 100, 2)
# #     print(province_infos)
# # result = sum(res1['result']['data']['gender'])
# # for province, rate in zip(res1['result']['province_x'], res1['result']['data']['area']):
# #     province_infos = {}
# #     province_infos['province'] = province
# #     province_infos['rate'] = round(rate / result * 100, 2)
# #     print(province_infos)
# #
# # print(result)
#
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'content-length': '11',
#     'content-type': 'application/x-www-form-urlencoded',
#     'd1': '%s' % get_d1(),
#     'd2': '%s' % get_d2(),
#     'd3': '%s' % get_d3(),
#     'd4': '%s' % get_d4(),
#     'd5': '%s' % get_d5(),
#     'origin': 'https://www.duanyuer.com',
#     'referer': 'https://www.duanyuer.com/user/00049h3u',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'cross-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
# }
# url = 'https://xcx.meizhuahuyu.com/douyin/user/getUserDetail'
# params = {
#     'token': '972f5ec2c383ad0d85823648b2ad68a2',
#     'toPageCode': '18',
# }
# data = {
#     'id': '00WUzQKK',
# }
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# res = json.loads(requests.post(url, params=params, data=data, headers=headers, verify=False).text)
# user_info = {}
# user_info['platform'] = '9'
# user_info['avatar'] = res['result']['avatar']
# user_info['userid'] = id
# user_info['name'] = res['result']['douyinName']
# user_info['url'] = res['result']['qrcodeUrl']
# user_info['location'] = res['result']['city']
# user_info['account'] = res['result']['douyinShortId']
# if res['result']['gender'] == 1:
#     user_info['sex'] = '2'
# elif res['result']['gender'] == 2:
#     user_info['sex'] = ''
# else:
#     user_info['sex'] = '1'
# if res['result']['constellation'] == '未知':
#     user_info['stars'] = ''
# else:
#     user_info['stars'] = res['result']['constellation']
# user_info['personal_profile'] = res['result']['constellation']
# if res['result']['tagList'] == []:
#     user_info['label'] = ''
# else:
#     user_info['label'] = get_label()[res['result']['tagList'][0]]
#
# if res['result']['birthday'] == '':
#     user_info['age'] = ''
# else:
#     now_year = datetime.datetime.today().year
#     birthday = datetime.datetime.strptime(res['result']['birthday'], '%Y-%m-%d').year
#     age = now_year - birthday
#     user_info['age'] = age
#
# if res['result']['mcnName'] == 'null':
#     user_info['mcn'] = ''
# else:
#     user_info['mcn'] = res['result']['mcnName']
#
# if res['result']['tagList'] == []:
#     user_info['categoryid'] = ''
# else:
#     user_info['categoryid'] = get_label()[res['result']['tagList'][0]]
# user_info['fans'] = res['result']['fansNumber']
# user_info['likes'] = res['result']['likeNumber']
# user_info['production'] = res['result']['videoNumber']
# print(user_info)
#
# url1 = 'https://xcx.meizhuahuyu.com/douyin/user/web/userfans'
# params1 = {
#     'token': '972f5ec2c383ad0d85823648b2ad68a2',
#     'toPageCode': '18',
#     'dyuserId': '00WUzQKK',
# }
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# headers.pop('content-length')
# headers.pop('content-type')
# ll = requests.get(url1, params=params1, headers=headers, verify=False)
#
#
# res1 = json.loads(ll.text)
#
# if res1['result']['data'] != None:
#     # 获取省份信息
#     result = sum(res1['result']['data']['gender'])
#     for province_list, percentage_list in zip(res1['result']['province_x'], res1['result']['data']['area']):
#         province_infos_list = {}
#         province_infos_list['userid'] = id
#         province_infos_list['province'] = province_list
#         province_infos_list['percentage'] = round(percentage_list / result * 100, 2)
#         print(province_infos_list)
#
#     # 获取星座信息
#     for star_list, star_rate_list in zip(res1['result']['constellation_x'],
#                                          res1['result']['data']['constellation']):
#         stars_infos = {}
#         stars_infos['userid'] = id
#         stars_infos['stars_name'] = star_list
#         stars_infos['percentage'] = round(star_rate_list / result * 100, 2)
#         print(stars_infos)
#
#     # 获取年龄信息
#     for age_list, age_rate_list in zip(res1['result']['constellation_x'],
#                                        res1['result']['data']['constellation']):
#         age_infos_list = {}
#         age_infos_list['userid'] = id
#         age_infos_list['age'] = age_list
#         age_infos_list['percentage'] = round(age_rate_list / result * 100, 2)
#         print(age_infos_list)
#
#     # 获取性别信息
#     sex_infos_list = {}
#     sex_infos_list['userid'] = id
#     sex_infos_list['female_rate'] = round(
#         res1['result']['data']['gender'][1] / result, 2)
#     sex_infos_list['male_rate'] = round(
#         res1['result']['data']['gender'][0] / result, 2)
#     print(sex_infos_list)
#
#
#
# else:
#     # 获得省份信息
#     for province_key, province_value in zip(eval(res1['result']['provinceDist']).keys(),
#                                             eval(res1['result']['provinceDist']).values()):
#         province_infos = {}
#         province_infos['userid'] = id
#         province_infos['province'] = province_key
#         province_infos['percentage'] = round(
#             province_value / sum(eval(res1['result']['provinceDist']).values()) * 100, 2)
#         print(province_infos)
#
#     # 获得年龄信息
#     for age_key, age_value in zip(eval(res1['result']['ageDist']).keys(),
#                                   eval(res1['result']['ageDist']).values()):
#         age_infos = {}
#         age_infos['userid'] = id
#         age_infos['age'] = age_key
#         age_infos['percentage'] = round(age_value / sum(eval(res1['result']['ageDist']).values()) * 100, 2)
#         print(age_infos)
#
#     # 获得性别信息
#     sex_infos = {}
#     sex_infos['userid'] = id
#     sex_infos['female_rate'] = round(
#         eval(res1['result']['sexDist'])['female'] / sum(eval(res1['result']['ageDist']).values()), 2)
#     sex_infos['male_rate'] = round(
#         eval(res1['result']['sexDist'])['male'] / sum(eval(res1['result']['ageDist']).values()), 2)
#     print(sex_infos)

from android_header import get_headers
import requests
import json

def get_detail():
    url = 'https://xcx.meizhuahuyu.com/douyin/xcx/userfans/data/157235?token=e026301d9868594388d384d3ca9f2084&toPageCode=54&date=2'

    res = json.loads(requests.get(url, headers=get_headers(), verify=False).text)
    print(res['result'])
get_detail()