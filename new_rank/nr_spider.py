'''
总榜
'''
import pymysql
import requests
import json
import datetime

import urllib3


def get_headers():
    headers = {
        'Host': 'xd.newrank.cn',
        'Connection': 'keep-alive',
        'Content-Length': '76',
        'cookie': '',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A32) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx55778a0d7b3048c4/27/page-frame.html',
    }
    return headers


def get_data():
    '''
    没有抓到分类数据包，手动添加所有分类
    start控制页码，第一页已经抓过，重新抓是添加第一页
    :return:
    '''
    # temp_list = ['娱乐', '才艺', '萌宠', '搞笑', '二次元', '游戏', '家居', '美食', '旅游', '健康', '企业', '体育', '教育', '科技', '汽车', '情感', '时尚',
    #              '文化', '社会', '时事']
    # temp_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
    #              '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '香港']
    temp_list = ['山东', '河南', '湖北',
                 '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '香港']
    data_list = []
    for temp in temp_list:
        data = [
            '{"type":"%s","date_type":"days","date":"%s","start":1,"size":20}' % (
                temp, (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')),
            '{"type":"%s","date_type":"days","date":"%s","start":2,"size":20}' % (
                temp, (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')),
            '{"type":"%s","date_type":"days","date":"%s","start":3,"size":20}' % (
                temp, (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')),
        ]

        data_list.append(data)
    # print(data_list)

    return data_list


# get_data()


def one_page(datas):
    '''
    请求一级页面得到uid，作为参数传到二级请求页面
    :return:
    '''
    url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/rank/hotAccountAllRankList'
    # url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/rank/hotAccountDistrictRankList'
    data = datas.encode('utf-8')
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(url, data=data, headers=get_headers(), verify=False, allow_redirects=False).text)
    uid_list = []
    for uids in res['data']['list']:
        yield (uids['uid'])
    #     uid_list.append(uids['uid'])
    # uid_lists.append(uid_list)
    # return uid_lists


def two_page(uid):
    '''
    请求二级页面获得详细信息
    :return:
    '''
    url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/accountInfoAll'
    data = '{"uid":"%s"}' % uid
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(url, data=data, headers=get_headers(), verify=False, allow_redirects=False).text)
    user_info = {}
    user_info['platform'] = '8'
    user_info['avatar'] = res['data']['avatar']
    user_info['userid'] = uid
    user_info['name'] = res['data']['nickname']
    user_info['url'] = ''
    user_info['location'] = res['data']['city']
    user_info['account'] = res['data']['account']

    if res['data']['gender'] == '男':
        user_info['sex'] = '1'
    elif res['data']['gender'] == '女':
        user_info['sex'] = '2'
    else:
        user_info['sex'] = ''

    if res['data']['constellation_name'] == '未知':
        user_info['stars'] = ''
    else:
        user_info['stars'] = res['data']['constellation_name']

    user_info['personal_profile'] = res['data']['signature']

    if res['data']['content_tags'] == []:
        user_info['label'] = ''
    else:
        user_info['label'] = res['data']['content_tags'][0]

    user_info['age'] = res['data']['age']
    user_info['mcn'] = res['data']['mcn_name']
    user_info['categoryid'] = res['data']['type']

    fans = res['data']['follower_count']
    if 'w' in fans:
        user_info['fans'] = str(int(float(fans.split('w')[0]) * 10000))
    else:
        user_info['fans'] = str(int(float(fans.split('亿')[0]) * 100000000))
    likes = res['data']['total_favorited']
    if 'w' in likes:
        user_info['likes'] = str(int(float(likes.split('w')[0]) * 10000))
    else:
        user_info['likes'] = str(int(float(likes.split('亿')[0]) * 100000000))

    user_info['production'] = res['data']['aweme_count']
    print(user_info)

    # conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
    #                        database="test",
    #                        charset="utf8mb4")
    # cursor = conn.cursor()
    # try:
    #     sql = "INSERT INTO t_from_user_info (platform, avatar, userid, name, url, location, account, sex, stars, personal_profile, label, production, age, mcn, categoryid, fans, likes) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    #     base = (user_info['platform'], user_info['avatar'], user_info['userid'], user_info['name'],
    #             user_info['url'], user_info['location'], user_info['account'], user_info['sex'],
    #             user_info['stars'], user_info['personal_profile'], user_info['label'],
    #             user_info['production'], user_info['age'], user_info['mcn'], user_info['categoryid'],
    #             user_info['fans'], user_info['likes'])
    #     cursor.execute(sql % base)
    #     conn.commit()
    # except:
    #     conn.rollback()
    #
    # # 获得省份信息
    # url2 = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/detail/followerAna'
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # res2 = json.loads(requests.post(url2, headers=get_headers(), data=data, verify=False).text)
    #
    # for province_info in res2['data']['follower_province']:
    #     try:
    #         province_infos = {}
    #         province_infos['userid'] = uid
    #         province_infos['province'] = province_info['key']
    #         province_infos['percentage'] = float(province_info['rate'])
    #         print(province_infos)
    #     except IndexError and TypeError and KeyError:
    #         pass
    #     try:
    #         sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
    #         base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
    #         cursor.execute(sql2 % base2)
    #         conn.commit()
    #     except:
    #         conn.rollback()
    # # 获得年龄信息
    #
    # for age_info in res2['data']['follower_age']:
    #     try:
    #         age_infos = {}
    #         age_infos['userid'] = uid
    #         age_infos['age'] = age_info['key']
    #         age_infos['percentage'] = float(age_info['rate'])
    #         print(age_infos)
    #     except IndexError and TypeError and KeyError:
    #         pass
    #
    #     try:
    #         sql4 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
    #         base4 = (age_infos['userid'], age_infos['age'], age_infos['percentage'])
    #         cursor.execute(sql4 % base4)
    #         conn.commit()
    #     except:
    #         conn.rollback()
    # # 获得性别信息
    # if res2['data']['follower_gender'] == []:
    #     pass
    # else:
    #     sex_infos = {}
    #     sex_infos['userid'] = uid
    #     sex_infos['female_rate'] = float(res2['data']['follower_gender'][1]['rate'])
    #     sex_infos['male_rate'] = float(res2['data']['follower_gender'][0]['rate'])
    #     print(sex_infos)
    #
    #     try:
    #         sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
    #         base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
    #         cursor.execute(sql6 % base6)
    #         conn.commit()
    #     except:
    #         conn.rollback()
    #     conn.close()

# def main(datas):
#     uids = one_page(datas)
#     for uid in uids:
#         two_page(uid)
#
# if __name__ == '__main__':
#     temp = get_data()
#     for eve in temp:
#         for datas in eve:
#             main(datas)


