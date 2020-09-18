'''
带货达人榜
更新cookie
'''
import time
import pymysql
import requests
import json
import datetime


def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=3bb57c6b-679d-454c-9c06-2683109e4889; grwng_uid=95502437-1e8d-40ac-9116-e3f492e799c8; __51cke__=; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592961783,1592990248; 8e22d1b16f393571_gr_session_id=56886d0d-1143-47cc-8194-8a03d46c7b93; 8e22d1b16f393571_gr_session_id_56886d0d-1143-47cc-8194-8a03d46c7b93=true; __tins__20450359=%7B%22sid%22%3A%201592994485675%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201592996288265%7D; __51laig__=4; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592994488; JSESSIONID=196CF4469BED6BB3344955D20B8E5777',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90RuKb2NK12-lHlx67b42pEg',
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
            {'tag': '%s' % cate, 'type': '4', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '5', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },


        ]
        cate_list.append(params)
    return cate_list


def get_one():
    temp = get_params()
    Id_lists = []
    for eve in temp:
        for params in eve:
            url = 'http://www.huo1818.com/live-api/v1_2/ranking-list/video'
            res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
            Id_list = []
            for id in res['result']['resultList']:
                Id_list.append(id['streamerId'])
            Id_lists.append(Id_list)
    # print(Id_lists)
    # Id_lists = [[159728888, 307385628, 363730683], [3421034, 48333793, 76595390, 159728888, 790067062, 1094530492, 881901883, 913197813, 128806259, 473449950], [573011572, 731896009, 492776986, 1268032543, 655880597, 699637354, 1165695393, 827910579], [292796929, 827870516, 192149983, 753538073, 773839251, 783206781, 631229972, 1080400767, 242579846, 238401657], [573011572, 731896009, 699637354, 292796929, 192149983, 492776986, 1268032543, 773839251, 632014870, 753538073], [137797843, 789873595, 691616396, 106339089, 296869187], [174438890, 172690077, 262213365, 1056559871, 131753852, 252454626, 518056959, 619287369, 15212177, 363760454], [174438890, 137797843, 172690077, 262213365, 296869187, 106339089, 1056559871, 691616396, 619287369, 15212177], [252278664, 209219915, 1163843891, 129407164, 627135568, 1272974271, 702550432, 498180472, 1264957953, 951438077], [158020817, 1247079935, 511756605, 366354345, 976786976, 251985566, 49670427, 227072675, 1018409759, 690005165], [158020817, 702550432, 64415770, 976786976, 252278664, 748064351, 168397971, 1018409759, 236428191, 49670427], [79123014, 88144803, 403082302, 144031394, 230349758, 393792848, 2181681, 115170970, 91466614, 49704439], [50048771, 201433437, 20170155, 40300003, 83302244, 6309714, 1086657, 2415, 202315478, 143483920], [28648881, 2181681, 50065104, 79123014, 882241725, 632926522, 50048771, 157494646, 26175888, 1161499873], [850425650, 13962256, 6806417, 7149649, 265627410, 616344499, 1015641429, 1091811884, 21506014, 951262584], [12603951, 11026138, 261256789, 329966183, 1215516088, 1261958258, 67584474, 35059695, 372834062, 172160808], [329966183, 13962256, 261256789, 11026138, 265627410, 35059695, 1215516088, 7149649, 104204123, 1015641429]]
    return Id_lists
# get_one()

def get_detail():
    idss = get_one()
    # user_list = []
    for ids in idss:
        for id in ids:
            url = 'http://www.huo1818.com/live-api/v1_2/streamer/horoscope-portrait-v2?streamerId={}'.format(id)
            res = json.loads(requests.get(url, headers=get_headers()).text)
            if res['result'] != []:
                for stars_info in res['result']:
                    stars_infos = {}
                    stars_infos['userid'] = id
                    stars_infos['stars_name'] = stars_info['value']
                    stars_infos['percentage'] = float(float(stars_info['percent']) * 100)
                    print(stars_infos)

                    conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi",
                                           password="ChaxunNewOtMySql1129",
                                           database="test",
                                           charset="utf8mb4")
                    cursor = conn.cursor()

                    try:
                        sql5 = "INSERT INTO t_from_user_stars (userid, stars_name, percentage) VALUE ('%s','%s','%s')"
                        base5 = (stars_infos['userid'], stars_infos['stars_name'], stars_infos['percentage'])
                        cursor.execute(sql5 % base5)
                        conn.commit()
                    except:
                        conn.rollback()

                # 获得性别信息
                url6 = 'http://www.huo1818.com/live-api/v1_2/streamer/gender-portrait-v2?streamerId={}'.format(id)

                try:
                    res6 = json.loads(requests.get(url6, headers=get_headers()).text)
                    sex_infos = {}
                    sex_infos['userid'] = id

                    sex_infos['female_rate'] = float(float(res6['result'][0]['percent']) * 100)
                    sex_infos['male_rate'] = float(float(res6['result'][1]['percent']) * 100)
                    print(sex_infos)
                except IndexError and TypeError and KeyError:
                    pass
                conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi",
                                       password="ChaxunNewOtMySql1129",
                                       database="test",
                                       charset="utf8mb4")
                cursor = conn.cursor()
                try:
                    sql6 = "INSERT INTO t_from_user_sex (userid, female_rate, male_rate) VALUE ('%s','%s','%s')"
                    base6 = (sex_infos['userid'], sex_infos['female_rate'], sex_infos['male_rate'])
                    cursor.execute(sql6 % base6)
                    conn.commit()
                except:
                    conn.rollback()
                conn.close()
        time.sleep(2)

# get_detail()
