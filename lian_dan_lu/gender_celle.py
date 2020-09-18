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
        'Cookie': 'gr_user_id=3bb57c6b-679d-454c-9c06-2683109e4889; grwng_uid=95502437-1e8d-40ac-9116-e3f492e799c8; 8e22d1b16f393571_gr_session_id=8f5d4310-2b98-42d1-bb2d-8bbd1767af13; 8e22d1b16f393571_gr_session_id_8f5d4310-2b98-42d1-bb2d-8bbd1767af13=true; __51cke__=; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592961783,1592990248; __tins__20450359=%7B%22sid%22%3A%201592990247909%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201592992050384%7D; __51laig__=2; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592990251; JSESSIONID=8C1D0D0D002286A6C632FBB6B118E4D0',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
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
            {'tag': '%s' % cate, 'type': '1', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '8', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },
            {'tag': '%s' % cate, 'type': '9', 'granularity': '1',
             'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
             'goodsType': '', 'liveCategoryName': '', 'pageSize': '40', 'pageNo': '1', },

        ]
        cate_list.append(params)
    return cate_list


def get_one():
    # temp = get_params()
    # Id_lists = []
    # for eve in temp:
    #     for params in eve:
    #         url = 'http://www.huo1818.com/live-api/v1_1/ranking-list/reward-out'
    #         res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
    #         Id_list = []
    #         for id in res['result']['resultList']:
    #             Id_list.append(id['streamerId'])
    #         Id_lists.append(Id_list)
    # print(Id_lists)
    Id_lists = [[77370946], [], [], [], [199701824, 683550811, 262688207, 251519354, 233733235, 367049071, 656717204, 587109032, 623155757, 587737733], [199701824, 683550811, 262688207, 251519354, 656717204, 340369428, 218934069], [233733235, 367049071, 587109032, 623155757, 587737733, 13909871, 282934637, 146224321], [177461404, 459062179, 188888880, 1084846349, 21752, 230309282, 43817496, 102250461, 714578967, 915376765], [177461404, 459062179, 188888880, 1084846349, 21752, 230309282, 43817496, 102250461, 714578967, 915376765], [1054290064, 960773034, 1144845308, 1142923853, 359297699, 332603000, 150997125, 116465891, 319958776, 571709088], [128438008, 714578967, 431234568, 257013991, 383559241, 340553898, 41570273, 73931512, 622891537, 548433635], [128438008, 714578967, 431234568, 257013991, 383559241, 340553898, 41570273, 73931512, 622891537, 548433635], [359297699, 332603000], [960773034, 215592837, 894386231, 148314738, 604006129, 388972716, 71862763, 690364010, 241003242, 380655465], [215592837, 894386231, 148314738, 604006129, 388972716, 71862763, 241003242, 380655465], [960773034, 690364010], [177461404], [177461404], [], [1160014364], [1160014364], [], [28166730, 893431, 13028, 563933823, 625992827, 340103191, 69608558, 1235583074, 703877883, 771116081], [893431, 563933823, 625992827, 340103191, 69608558, 703877883, 771116081, 83946967, 617475615, 139135952], [28166730, 13028, 1235583074, 395620490, 14475553, 158037832, 438301830, 300607772, 751354520, 916042565], [], [], [], [14817704, 19005228, 198169829, 191003593], [14817704, 19005228, 198169829, 191003593], [], [14817704, 6813710, 86644305, 23848974, 6105884, 15181585, 103432682, 156587032, 43633382], [14817704, 6813710, 86644305, 23848974, 6105884, 15181585, 103432682, 156587032, 43633382], [], [881901883, 1178205407], [881901883, 1178205407], [], [292796929, 585271561, 609737844, 655880597], [292796929, 609737844, 655880597], [585271561], [691616396, 421600336], [691616396], [421600336], [368301536, 198908786, 416885280, 706167779, 555275259, 542732847, 44297426, 582073650], [368301536, 198908786, 416885280, 706167779, 555275259, 542732847, 44297426, 582073650], [], [88144803, 403082302, 49033571, 393792848, 79123014, 608537780, 74119183, 71186086, 761780724, 462595689], [88144803, 403082302, 49033571, 393792848, 79123014, 608537780, 74119183, 71186086, 462595689, 248421325], [761780724, 49704439, 190120914, 450236149, 1142923853, 823624110, 46935569, 882651883, 100239914, 150997125], [261256789, 951262584, 522740566, 850425650, 547225506, 21506014, 13962256, 834757848, 349474319, 112337954], [261256789, 951262584, 522740566, 850425650, 547225506, 21506014, 13962256, 834757848, 349474319, 112337954], [975249328, 985337255, 888797989, 943460800]]

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
