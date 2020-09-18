'''
行业榜信息
authorization需要更新
接口2分钟限制40次
'''
import datetime
import json
import time
import requests
import urllib3
# from mongo_info import mongo_info_xhs
# from province_mongo import mongo_info_province
# from sex_mongo import mongo_info_sex
import pymysql



def get_headers():
    headers = {
        'Host': 'openapi.qian-gua.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A32) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
        'charset': 'utf-8',
        'authorization': 'bearer dCtthlyzERRi3KoDCZtn4vN-64AzBJa1Vt7dCV2xX69jPFBzbt8KebvYyJ_BJCZUH3LhWlH7V1PS0Ov24-SEP5CpsO9O-ZvIzr3aClMh4GCkh6oyYTVzlmiYBcbF9ZEMDq-TP7RpyMj-NH1hLWx5hwM-lqSEXZmyVurSqVf0XvkjDIpL0AV2ycgKVJEHFHhQcNXOmg',
        'Accept-Encoding': 'gzip',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wxa81fd06044ad80da/8/page-frame.html',
    }
    return headers


def get_tagid():
#     url = 'https://openapi.qian-gua.com/v1/rank/GetBloggerRankTags'
#     params = {
#         'isContainsAll': 'true',
#         '_': '%s' % int(round(time.time() * 1000)),
#     }
#     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#     res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
#     tagid_list = []
#     for tagid in res['Data']:
#         tagid_list.append(tagid['Id'])
#     print(tagid_list)
#     return tagid_list
# get_tagid()
    tagid_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    return tagid_list
#     url = 'https://openapi.qian-gua.com//v1/rank/AreaRankOptions'
#     params = {
#         'provinceId': '0',
#         '_': '%s' % int(round(time.time() * 1000)),
#     }
#     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#     res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
#     tagid_list = []
#     for tagid in res['Data']:
#         tagid_list.append(tagid['ID'])
#     print(tagid_list)
    # return tagid_list
# get_tagid()


def get_params():
    tagids = get_tagid()
    params_list = []
    for tagid in tagids:
        params = {
            'rankType': '10',  # 行业榜为11，地区榜为10，品牌号榜为13
            'period': '1',
            'datecode': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d'),
            'pageIndex': '1',
            'pageSize': '30',
            'tagId': '%s' % tagid,
            '_': '%s' % int(round(time.time() * 1000)),
        }
        params_list.append(params)
    # print(params_list)
    return params_list
# get_params()


def one_page():
    params_list = get_params()
    BloggerId_lists = []
    for params in params_list:
        url = 'https://openapi.qian-gua.com/v1/rank/BloggerRankData'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
        BloggerId_list = []
        for Id in res['Data']['ItemList']:

            BloggerId_list.append(Id['BloggerId'])
        BloggerId_lists.append(BloggerId_list)
    # print(BloggerId_lists)
    return BloggerId_lists
# one_page()

def get_detail():
    BloggerIdss = one_page()
    for BloggerIds in BloggerIdss:
        for BloggerId in BloggerIds:
            url = 'https://openapi.qian-gua.com/v1/Blogger/GetDetail'
            params = {
                'bloggerId': '%s' % BloggerId,
                'dateCode': '%s' % (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d'),
                '_': '%s' % int(round(time.time() * 1000)),
            }
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
            if res['Code'] == 200:
                user_info = {}
                user_info['platform'] = '5'

                # 千瓜指数
                # user_info['BloggerIndex'] = res['Data']['BloggerIndex']
                # 属性
                # user_info['BloggerProp'] = res['Data']['BloggerProp']
                # 等级
                # user_info['LevelName'] = res['Data']['LevelName']
                # 昵称
                user_info['name'] = res['Data']['NickName']
                user_info['account'] = res['Data']['RedId']
                user_info['location'] = res['Data']['Location']
                user_info['stars'] = ''
                user_info['categoryid'] = ''
                user_info['url'] = ''
                user_info['personal_profile'] = ''
                user_info['age'] = ''
                # id
                user_info['userid'] = BloggerId
                # 品牌合作人
                # if res['Data']['IsBrandPartner'] == 'False':
                #     user_info['IsBrandPartner'] = '0'
                # else:
                #     user_info['IsBrandPartner'] = '1'
                # 性别
                if res['Data']['Gender'] == 1:
                    user_info['sex'] = '2'
                else:
                    user_info['sex'] = '1'
                # 地区
                # user_info['city'] = res['Data']['Location']
                # 所属机构
                user_info['mcn'] = res['Data']['McnName']
                # 图文笔记
                # user_info['NoteNormalCount'] = res['Data']['NoteNormalCount']
                # 视频笔记
                user_info['production'] = res['Data']['NoteVideoCount']
                user_info['fans'] = res['Data']['Fans']
                user_info['likes'] = res['Data']['Liked']
                # user_info['Collected'] = res['Data']['Collected']
                # user_info['CommentNum'] = res['Data']['CommentNum']
                # 头像
                user_info['avatar'] = res['Data']['SmallAvatar']
                try:
                    user_info['label'] = res['Data']['TagList'][0]['TagName']
                except KeyError and IndexError:
                    user_info['label'] = ''
                # 粉丝地域分布

                # 粉丝关注焦点
                # user_info['FansFocus'] = res['Data']['BloggerFansInfo']['TagList']
                # 粉丝人群标签
                # user_info['FocusList'] = res['Data']['BloggerFansInfo']['FocusList']
                # 粉丝活跃度
                # user_info['FansActive'] = res['Data']['BloggerFansInfo']['FansActive']
                # user_info['Female'] = res['Data']['BloggerFansInfo']['Female']
                # user_info['Male'] = res['Data']['BloggerFansInfo']['Male']
                # 收藏趋势
                # user_info['CollectAddCount'] = res['Data']['CollectAddCount']
                # user_info['CommentAddCount'] = res['Data']['CommentAddCount']
                # user_info['FansAddCount'] = res['Data']['FansAddCount']
                # user_info['LikeAddCount'] = res['Data']['LikeAddCount']
                print(user_info)
                # mongo_info_xhs.insert_item(user_info)
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
                # conn.close()

                for province_info in res['Data']['BloggerFansInfo']['ProvinceList']:
                    if province_info == None:
                        pass
                    else:
                        province_infos = {}
                        province_infos['userid'] = BloggerId
                        province_infos['province'] = province_info['Name']
                        province_infos['percentage'] = province_info['Percent']
                        print(province_infos)
                    try:
                        sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                        base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
                        cursor.execute(sql2 % base2)
                        conn.commit()
                    except:
                        conn.rollback()
                    # conn.close()

                    # mongo_info_province.insert_item(province_infos)

                sex_infos = {}
                sex_infos['userid'] = BloggerId
                sex_infos['female_rate'] = res['Data']['BloggerFansInfo']['Female']
                sex_infos['male_rate'] = res['Data']['BloggerFansInfo']['Male']
                print(sex_infos)
                # mongo_info_sex.insert_item(sex_infos)
                try:
                    sql3 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                    base3 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                    cursor.execute(sql3 % base3)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()
                time.sleep(5)


get_detail()
