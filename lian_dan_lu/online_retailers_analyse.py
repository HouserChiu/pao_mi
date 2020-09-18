# coding: utf-8
'''
电商分析，后续和主程序一起跑
'''
import time

import requests
import json
import datetime
import pymysql




def get_headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=3bb57c6b-679d-454c-9c06-2683109e4889; 8e22d1b16f393571_gr_session_id=e52bfbad-f70d-4932-baec-4ab97168577f; __51cke__=; 8e22d1b16f393571_gr_session_id_e52bfbad-f70d-4932-baec-4ab97168577f=true; grwng_uid=95502437-1e8d-40ac-9116-e3f492e799c8; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1592961783; __tins__20450359=%7B%22sid%22%3A%201592961782377%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201592963671868%7D; __51laig__=3; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1592961872; JSESSIONID=A4CDA2CF2A363F5C7021EF126324B7A6',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    return headers

# 类别信息提取
def get_cate():
    url = 'http://www.huo1818.com/live-api/selector/tags'
    res = json.loads(requests.get(url, headers=get_headers()).text)
    cate_list = []
    for cate in res['result']:
        cate_list.append(cate['tag'])
    return cate_list

# 构建请求参数
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

# 获取id信息
def get_one():
    # temp = get_params()
    # Id_lists = []
    # for eve in temp:
    #     for params in eve:
    #         url = 'http://www.huo1818.com/live-api/v1_2/ranking-list/video'
    #         res = json.loads(requests.get(url, params=params, headers=get_headers()).text)
    #         Id_list = []
    #         for id in res['result']['resultList']:
    #             Id_list.append(id['streamerId'])
    #         Id_lists.append(Id_list)
    # print(Id_lists)
    Id_lists = [[98655088, 75536056, 7203449, 131305305, 5704387, 615576134, 180669233], [1298084233, 675747510, 1326068190, 365696608, 2280970, 1131979390, 1172721571, 811983866, 119536885, 934304282], [589115357, 347951065, 577062739, 861734654, 719324215, 772007850, 1247543076, 126945177, 378220013, 845082728], [69691074, 203657565, 958468058, 107337748, 332842111, 3222547, 1089771349, 433522830, 296114947, 23154795], [296114947, 958468058, 184404999, 55960593, 1211562349, 3314816, 433522830, 38587861, 722364868, 598183207], [943354472, 1562502, 326846463, 203101644, 46718927, 162286990, 78118984, 218934069, 199701824, 702347283], [213993187, 192355602, 203101644, 450210078, 125322822, 124870886, 454210858, 41902485, 326846463, 140231692], [50204684, 74476707, 138209287, 1363397294, 330143373, 358784127, 592541328, 2280970, 70002177, 27993283], [1128706184, 1394588763, 2460082, 1170364825, 1016355266, 549296979, 10915222, 1249194381, 1250304503, 605160123], [1017738636, 829293370, 4048884, 253850265, 15238048, 163685932, 51362414, 73598772, 1098356305, 67724052], [1170364825, 1016355266, 30279825, 615454771, 456069264, 417474403, 483284830, 129632049, 161011607, 792956717], [1096637401, 974889968, 173168681, 40300005, 49169054, 135538136, 1132083990, 220267541, 278694812, 1326068190], [307893635, 113921161, 685528023, 364895229, 173168681, 408265348, 736924574, 1069545237, 715835595, 808379613], [391654873, 238136297, 8075444, 220100760, 8375394, 640378610, 760111069, 25982942, 280480049, 1327715], [1327715, 8075444, 760111069, 515459432, 723350446, 354759881, 269705707, 640378610, 30115383, 391654873], [157328248, 676304670, 739852595, 655526312, 1000795204, 722616934, 774777097, 403554030, 735032071, 712877389], [149145196, 739852595, 661069210, 1000795204, 869854628, 714882647, 761738616, 495726656, 722616934, 157328248], [456376709, 221776806, 616602646, 1289314016, 481341196, 1080979992, 891767534, 374035133, 29559521, 267993171], [357368966, 207480098, 234166435, 241846824, 164136096, 1174225822, 823109594, 904969234, 599787946, 24202405], [1212501318, 959706144, 569755448, 1004679851, 119338179, 496006453], [959706144, 1004679851, 1212501318, 119338179, 496006453, 569755448], [19005228, 20199496, 14817704, 191003593, 17473740, 88637945, 198169829, 1324713342, 454789157], [19005228, 20199496, 191003593, 1324713342, 17473740, 88637945, 198169829, 454789157, 14817704], [23848974, 6813710, 140673020, 43633382, 7731334, 6105884, 103432682, 14817704, 15181585, 156587032], [6813710, 6105884, 86644305, 43633382, 156587032, 15181585, 103432682, 23848974, 140673020, 7731334], [3421034, 48333793, 649234051, 524130388, 307385628, 155087241, 470284984, 564674650, 204835015, 526782016], [50090236, 469962199, 899586692, 749793217, 204835015, 249979004, 564674650, 30206547, 656314055, 1011162896], [731896009, 823685855, 811715162, 492776986, 743815630, 67701725, 52096923, 1268032543, 779476673, 758577498], [957538598, 10311829, 45796436, 233028568, 758577498, 548949891, 492776986, 65228751, 929010714, 145768975], [137797843, 384795944, 106339089, 356288687, 189045867, 569981667, 904269572, 405907058, 266491459, 1056559871], [769328934, 497239416, 514532971, 949199383, 982025886, 388435458, 781527212, 114798219, 32361104, 18965475], [881758958, 126087195, 219714049, 1325878023, 4048884, 253850265, 736772342, 897801489, 66334989, 209219915], [347331302, 1327715, 900274515, 164635732, 8075444, 657347041, 446048808, 165117285, 33861759, 433673433], [89133130, 115170970, 28648881, 91466614, 308274448, 684795561, 5236028, 9484044, 431559867, 83302244], [699220794, 77301131, 103317431, 30911422, 210861214, 111553041, 21915782, 549296979, 490578553, 866330378], [455244900, 35059695, 368920374, 884484672, 415913398, 7149649, 582751055, 265627410, 943460800, 122314311], [122314311, 582751055, 975249328, 353061961, 995642791, 207757930, 398553367, 620736145, 35059695, 480994775]]
    return Id_lists
# get_one()

# 获取电商分析信息
def get_analyse():
    idss = get_one()
    for ids in idss:
        for id in ids:
            url = 'http://www.huo1818.com/live-api/v1_2_1/streamer/goods-trend'
            params = {
                'streamerId': '%s' % id,
                'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')),
                'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                'rankStatus': '1',
            }
            res = json.loads(requests.get(url, headers=get_headers(), params=params).text)
            count_list = []
            for sum_temp in res['result']:
                count_list.append(sum_temp['goodsNum'])
            count_temp = sum(count_list)



            for temp in res['result']:
                goods_trend = {}
                goods_trend['userid'] = id
                goods_trend['goods_num'] = temp['goodsNum']
                if count_temp != 0:
                    goods_trend['goods_rate'] = round((temp['goodsNum'] / count_temp) * 100, 2)
                else:
                    goods_trend['goods_rate'] = 0.00
                goods_trend['goods_category'] = temp['liveCategoryName']
                goods_trend['sell_count'] = temp['sellCount']
                goods_trend['sell_amount'] = temp['sellAmount']
                print(goods_trend)

                conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
                                       database="test",
                                       charset="utf8mb4")

                sql = "INSERT INTO t_from_user_goods_trend (userid, goods_num, goods_rate, goods_category, sell_count, sell_amount) VALUE ('%s','%s','%s','%s','%s','%s')"
                base = (
                    goods_trend['userid'], goods_trend['goods_num'], goods_trend['goods_rate'], goods_trend['goods_category'], goods_trend['sell_count'],
                    goods_trend['sell_amount'])
                try:
                    cursor = conn.cursor()
                    cursor.execute(sql % base)
                    conn.commit()
                except:
                    conn.ping()
                    cursor = conn.cursor()
                    cursor.execute(sql % base)
                    conn.commit()
                    conn.rollback()

                for temp2 in temp['goods']:
                    goods_detail = {}
                    goods_detail['userid'] = goods_trend['userid']
                    goods_detail['goods_category'] = goods_trend['goods_category']
                    goods_detail['goods_id'] = temp2['goodsId']
                    goods_detail['goods_title'] = temp2['kwaiTitle'].replace("'", '').replace('"', '')
                    goods_detail['goods_link'] = temp2['link']
                    goods_detail['sell_count'] = temp2['sellCount']
                    if temp2['sellCountRate'] != None:
                        goods_detail['sell_count_rate'] = float(float(temp2['sellCountRate']) * 100)
                    else:
                        goods_detail['sell_count_rate'] = 0.00

                    goods_detail['sell_amount'] = temp2['sellAmount']

                    if temp2['sellAmountRate'] != None:
                        goods_detail['sell_amount_rate'] = float(float(temp2['sellAmountRate']) * 100)
                    else:
                        goods_detail['sell_amount_rate'] = 0.00
                    print(goods_detail)

                    sql2 = "INSERT INTO t_from_user_goods_detail (userid, goods_category, goods_id, goods_title, goods_link, sell_count, sell_count_rate, sell_amount, sell_amount_rate) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    base2 = (goods_detail['userid'], goods_detail['goods_category'], goods_detail['goods_id'],
                             goods_detail['goods_title'], goods_detail['goods_link'],
                             goods_detail['sell_count'], goods_detail['sell_count_rate'], goods_detail['sell_amount'],
                             goods_detail['sell_amount_rate'])

                    try:
                        cursor = conn.cursor()
                        cursor.execute(sql2 % base2)
                        conn.commit()
                    except:
                        conn.ping()
                        cursor = conn.cursor()
                        cursor.execute(sql2 % base2)
                        conn.commit()
                        conn.rollback()

            url1 = 'http://www.huo1818.com/live-api/v1_2_1/streamer/goods-price-range-trend'
            params1 = {
                'streamerId': '%s' % id,
                'startDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')),
                'endDate': '%s' % ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')),
                'liveCategoryName': '',
            }
            res1 = json.loads(requests.get(url1, headers=get_headers(), params=params1).text)

            count_list1 = []
            for sum_temp1 in res1['result']:
                count_list1.append(sum_temp1['goodsNum'])
            count_temp1 = sum(count_list1)

            conn = pymysql.connect(host="111.231.0.33", port=3306, user="ceshi", password="ChaxunNewOtMySql1129",
                                   database="test",
                                   charset="utf8mb4")

            for temp1 in res1['result']:
                price_trend = {}
                price_trend['userid'] = id
                price_trend['price_range'] = str(int(temp1['leftRange'] / 100)) + '-' + str(
                    int(temp1['rightRange'] / 100))
                price_trend['goods_num'] = temp1['goodsNum']
                if count_temp1 != 0:
                    price_trend['goods_rate'] = round((temp1['goodsNum'] / count_temp1) * 100, 2)
                else:
                    price_trend['goods_rate'] = 0.00

                price_trend['sell_count'] = temp1['sellCount']
                price_trend['sell_amount'] = temp1['sellAmount']
                print(price_trend)



                sql1 = "INSERT INTO t_from_user_price_trend (userid, price_range, goods_num, goods_rate, sell_count, sell_amount) VALUE ('%s','%s','%s','%s','%s','%s')"
                base1 = (
                    price_trend['userid'], price_trend['price_range'], price_trend['goods_num'], price_trend['goods_rate'], price_trend['sell_count'],
                    price_trend['sell_amount'])
                try:
                    cursor = conn.cursor()
                    cursor.execute(sql1 % base1)
                    conn.commit()
                except:
                    conn.ping()
                    cursor = conn.cursor()
                    cursor.execute(sql1 % base1)
                    conn.commit()
                    conn.rollback()

                for temp3 in temp1['goods']:
                    price_detail = {}
                    price_detail['userid'] = price_trend['userid']
                    price_detail['price_range'] = price_trend['price_range']
                    price_detail['goods_id'] = temp3['goodsId']
                    price_detail['goods_title'] = temp3['kwaiTitle'].replace("'", '').replace('"', '')
                    price_detail['goods_link'] = temp3['link']
                    price_detail['sell_count'] = temp3['sellCount']
                    if temp3['sellCountRate'] != None:
                        price_detail['sell_count_rate'] = float(float(temp3['sellCountRate']) * 100)
                    else:
                        price_detail['sell_count_rate'] = 0.00
                    price_detail['sell_amount'] = temp3['sellAmount']
                    if temp3['sellAmountRate'] != None:
                        price_detail['sell_amount_rate'] = float(float(temp3['sellAmountRate']) * 100)
                    else:
                        price_detail['sell_count_rate'] = 0.00
                    print(price_detail)

                    sql3 = "INSERT INTO t_from_user_price_detail (userid, price_range, goods_id, goods_title, goods_link, sell_count, sell_count_rate, sell_amount, sell_amount_rate) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    base3 = (price_detail['userid'], price_detail['price_range'], price_detail['goods_id'],
                             price_detail['goods_title'], price_detail['goods_link'],
                             price_detail['sell_count'], price_detail['sell_count_rate'], price_detail['sell_amount'],
                             price_detail['sell_amount_rate'])
                    try:
                        cursor = conn.cursor()
                        cursor.execute(sql3 % base3)
                        conn.commit()
                    except:
                        conn.ping()
                        cursor = conn.cursor()
                        cursor.execute(sql3 % base3)
                        conn.commit()
                        conn.rollback()

            url2 = 'http://www.huo1818.com/live-api/v1_2_1/streamer/goods-range-trend'
            res2 = json.loads(requests.get(url2, headers=get_headers(), params=params1).text)

            count_list2 = []
            for sum_temp2 in res2['result']:
                count_list2.append(sum_temp2['goodsNum'])
            count_temp2 = sum(count_list2)

            for temp4 in res2['result']:
                count_trend = {}
                count_trend['userid'] = id
                count_trend['count_range'] = str(temp4['leftRange']) + '-' + str(
                    temp4['rightRange'])
                count_trend['goods_num'] = temp4['goodsNum']
                if count_temp2 != 0:
                    count_trend['goods_rate'] = round((temp4['goodsNum'] / count_temp2) * 100, 2)
                else:
                    count_trend['goods_rate'] = 0.00
                count_trend['sell_count'] = temp4['sellCount']
                count_trend['sell_amount'] = temp4['sellAmount']
                print(count_trend)

                sql4 = "INSERT INTO t_from_user_count_trend (userid, count_range, goods_num, goods_rate, sell_count, sell_amount) VALUE ('%s','%s','%s','%s','%s','%s')"
                base4 = (
                    count_trend['userid'], count_trend['count_range'], count_trend['goods_num'], count_trend['goods_rate'], count_trend['sell_count'],
                    count_trend['sell_amount'])

                try:
                    cursor = conn.cursor()
                    cursor.execute(sql4 % base4)
                    conn.commit()
                except:
                    conn.ping()
                    cursor = conn.cursor()
                    cursor.execute(sql4 % base4)
                    conn.commit()
                    conn.rollback()

                for temp5 in temp4['goods']:
                    count_detail = {}
                    count_detail['userid'] = count_trend['userid']
                    count_detail['count_range'] = count_trend['count_range']
                    count_detail['goods_id'] = temp5['goodsId']
                    count_detail['goods_title'] = temp5['kwaiTitle'].replace("'", '').replace('"', '')
                    count_detail['goods_link'] = temp5['link']
                    count_detail['sell_count'] = temp5['sellCount']
                    if temp5['sellCountRate'] != None:
                        count_detail['sell_count_rate'] = float(float(temp5['sellCountRate']) * 100)
                    else:
                        count_detail['sell_count_rate'] = 0.00
                    count_detail['sell_amount'] = temp5['sellAmount']
                    if temp5['sellAmountRate'] != None:
                        count_detail['sell_amount_rate'] = float(float(temp5['sellAmountRate']) * 100)
                    else:
                        count_detail['sell_amount_rate'] = 0.00
                    print(count_detail)

                    sql5 = "INSERT INTO t_from_user_count_detail (userid, count_range, goods_id, goods_title, goods_link, sell_count, sell_count_rate, sell_amount, sell_amount_rate) VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    base5 = (count_detail['userid'], count_detail['count_range'], count_detail['goods_id'],
                             count_detail['goods_title'], count_detail['goods_link'],
                             count_detail['sell_count'], count_detail['sell_count_rate'], count_detail['sell_amount'],
                             count_detail['sell_amount_rate'])

                    try:
                        cursor = conn.cursor()
                        cursor.execute(sql5 % base5)
                        conn.commit()
                    except:
                        conn.ping()
                        cursor = conn.cursor()
                        cursor.execute(sql5 % base5)
                        conn.commit()
                        conn.rollback()
                    conn.close()
        time.sleep(2)

# get_analyse()
