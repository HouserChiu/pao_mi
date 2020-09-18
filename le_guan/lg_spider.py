# coding: utf-8
'''
播主搜索页
'''
import pymysql
import requests
import json


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '691',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '120.35.10.209:8083',
        'Origin': 'http://lab.myleguan.com',
        'Referer': 'http://lab.myleguan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }
    return headers


def get_cate():
    cate_list = [
        '品牌', '办公软件', '汽车', '画画', '明星', '技艺', '生活', '老外', '旅行', '时尚', '美妆', '校园', '搞笑', '编程', '政务', '二次元', '魔术', '影视',
        '其它', '星座', '萌娃', '动漫', '情感', '文字', '家居', '玩具', '宠物', '游戏', '音乐', '职场', '金句', '育儿', '网红帅哥', '母婴', '蓝V', '外语',
        '声音', '购物车', '体育', 'Cosplay', '美食', '教育', '科技', '舞蹈', '穿搭', '网红美女', '演员'
    ]
    return cate_list

def get_one():
    cate_list = get_cate()
    for cate in cate_list:
        url = 'http://120.35.10.209:8083/lg_data_dy/dyUser/list'
        datas = {
            'pk_index_flag_date': '2020-06-19',
            'sortFieldName': 'update_time',
            'curPage': '4',
            'limit': '10',
            'analy_status': '1',
            'domain_type_multi': '%s' % cate,
            'boolean_person_authentication': 'false',
            'boolean_blue_v': 'false',
            'boolean_goods_upboard': 'false',
            'boolean_mobile': 'false',
            'listType': '日榜',
            'auth_flag': 'aaa',
            'lgCustomerId': '1002083069',
            'token': 'TEf6EMxqLTwuqrGthkXyAJ7JCTTTHaybyM/kvC0gz1pVAWV7bmS9Eei6i47rzJC59WaiDta5EMYFrodClxQdqNgxBx1tPBsvSBX+Obhzz1NNdjg/zsLHzcY03okDHOLAzczHVv4C0bZwvwAYRZ4qt+/n5dWeyNcL+5dy3ugec/X73XeFY+eVZvomgs2wJAYX1Pj/i8brSd3nFOP/oDIPnIN89N+wV+RO2oIy0xMaZD2GKRUGH2Ljr42xd1YCIcxtX3aAfoO2iuDqsEH9YENTum1WHxhWvft8kY9vMMUnHelrhSsuTQdrQIqhDWkGA/zbnnFv/B7oqGs/uqazTtPdFMDDwbVSr8Qwkhh5W1MsyEs=|1592789206842',
            'identity': '7',
        }
        result = json.loads(requests.post(url, data=datas, headers=get_headers()).text)
        for res in result['data']:
            user_info = {}
            user_info['platform'] = '10'
            user_info['avatar'] = res['logo']
            user_info['userid'] = res['pk_account']
            user_info['name'] = res['nickname']
            user_info['url'] = ''

            user_info['location'] = res['city']
            user_info['account'] = res['dy_id']
            if res['gender'] == '女':
                user_info['sex'] = '2'
            elif res['gender'] == '男':
                user_info['sex'] = '1'
            else:
                user_info['sex'] = ''
            user_info['stars'] = ''
            user_info['personal_profile'] = res['signature']
            user_info['label'] = res['child_domain']
            user_info['age'] = res['age']
            user_info['mcn'] = ''
            user_info['categoryid'] = res['domain_type']
            user_info['fans'] = res['funs_total']
            user_info['likes'] = res['favorited_total']
            user_info['production'] = res['video_total']
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

            if res['age_section'] == '无对应粉丝数据':
                pass
            else:
                for age_info in eval(res['age_section_json']):
                    age_infos = {}
                    age_infos['userid'] = user_info['userid']
                    age_infos['age'] = age_info['name'].split('_')[1] + '-' + age_info['name'].split('_')[2]
                    age_infos['percentage'] = float(float(age_info['percent']) / 100)
                    print(age_infos)

                    try:
                        sql4 = "INSERT INTO t_from_user_age (userid, age, percentage) VALUE ('%s','%s','%s')"
                        base4 = (age_infos['userid'], age_infos['age'], age_infos['percentage'])
                        cursor.execute(sql4 % base4)
                        conn.commit()
                    except:
                        conn.rollback()

                for province_info in eval(res['funs_province']):
                    province_infos = {}
                    province_infos['userid'] = user_info['userid']
                    province_infos['province'] = province_info['name']
                    province_infos['percentage'] = float(float(province_info['percent']) / 100)
                    print(province_infos)

                    try:
                        sql2 = "INSERT INTO t_from_user_province (userid, province, percentage) VALUE ('%s','%s','%s')"
                        base2 = (province_infos['userid'], province_infos['province'], province_infos['percentage'])
                        cursor.execute(sql2 % base2)
                        conn.commit()
                    except:
                        conn.rollback()

                for city_info in eval(res['funs_city']):
                    city_infos = {}
                    city_infos['userid'] = user_info['userid']
                    city_infos['city'] = city_info['name']
                    city_infos['percentage'] = float(float(city_info['percent']) / 100)
                    print(city_infos)

                    try:
                        sql3 = "INSERT INTO t_from_user_city (userid, city, percentage) VALUE ('%s','%s','%s')"
                        base3 = (city_infos['userid'], city_infos['city'], city_infos['percentage'])
                        cursor.execute(sql3 % base3)
                        conn.commit()
                    except:
                        conn.rollback()

                sex_infos = {}
                sex_infos['userid'] = user_info['userid']
                sex_infos['female_rate'] = float(float(res['female_scale']) / 100)
                sex_infos['male_rate'] = 100 - sex_infos['female_rate']
                print(sex_infos)

                try:
                    sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                    base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                    cursor.execute(sql6 % base6)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()
get_one()


