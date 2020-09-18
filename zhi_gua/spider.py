'''
达人榜
需要修改请求头中的token
'''
import requests
import json
import urllib3
from tb_info_mongo import mongo_info


def get_headers():
    headers = {
        'Host': 'wxamp.zhigua.cn',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A32) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
        'charset': 'utf-8',
        'token': '370afd9e093e4860b42715c57f9366ec',
        'Accept-Encoding': 'gzip',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wxc00a1edcdf8023e2/1/page-frame.html',
    }
    return headers


def get_params():
    cates = ['928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '1360', '1361',
             '1370', '1395', '1401', '1406', '1416', '1418', '1423', '1424', '1426', '1433', '1437', '1463', '1472',
             '1475',
             '1498']
    cate_list = []
    for cate in cates:
        params_list = [
            {'data': '{CategoryId:%s,period:1,pageIndex:1,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:1,pageIndex:2,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:1,pageIndex:3,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:1,pageIndex:4,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:1,pageIndex:5,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:7,pageIndex:1,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:7,pageIndex:2,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:7,pageIndex:3,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:7,pageIndex:4,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:7,pageIndex:5,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:30,pageIndex:1,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:30,pageIndex:2,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:30,pageIndex:3,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:30,pageIndex:4,pageSize:10}' % cate},
            {'data': '{CategoryId:%s,period:30,pageIndex:5,pageSize:10}' % cate},
        ]
        cate_list.append(params_list)
    # print(cate_list)
    return cate_list
# get_params()



def get_one_stage():
    temp = get_params()
    IdKey_lists = []
    LiveAnchorId_lists = []
    for eve in temp:
        for params in eve:
            url = 'https://wxamp.zhigua.cn/v2/RankMarket'
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, headers=get_headers(), params=params, verify=False).text)
            IdKey_list = []
            LiveAnchorId_list = []
            for item in res['Data']['ItemList']:
                IdKey_list.append(item['IdKey'])
                LiveAnchorId_list.append(item['LiveAnchorId'])
            IdKey_lists.append(IdKey_list)
            LiveAnchorId_lists.append(LiveAnchorId_list)
    return IdKey_lists, LiveAnchorId_lists
    # print(IdKey_lists)


# get_one_stage()


def get_detail():
    signss = get_one_stage()[0]
    LiveAnchorIdss = get_one_stage()[1]
    for signs, LiveAnchorIds in zip(signss, LiveAnchorIdss):
        for sign, LiveAnchorId in zip(signs, LiveAnchorIds):
            url = 'https://wxamp.zhigua.cn/v2/AnchorDetail'
            params = {'data': '{"liveAnchorId":"%s","sign":"%s"}' % (LiveAnchorId, sign)}
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.get(url, params=params, headers=get_headers(), verify=False).text)
            if res['Code'] == 200:
                user_info = {}
                user_info['platform'] = '4'
                # user_info['level'] = res['Data']['Anchor']['AnchorLevel']
                # user_info['AnchorTypeName'] = res['Data']['Anchor']['AnchorTypeName']
                user_info['location'] = res['Data']['Anchor']['Location']
                user_info['name'] = res['Data']['Anchor']['Nick']
                user_info['account'] = res['Data']['Anchor']['TBAnchorId']
                # user_info['score'] = res['Data']['Anchor']['Score']
                user_info['fans'] = res['Data']['Anchor']['FansCount']
                # user_info['AvgLike'] = res['Data']['Anchor']['AvgLike']
                # user_info['AvgComment'] = res['Data']['Anchor']['AvgComment']
                user_info['label'] = res['Data']['Anchor']['Tags'][0]['Name']
                user_info['avatar'] = res['Data']['Anchor']['HeadImage']
                user_info['categoryid'] = res['Data']['Anchor']['CategoryName']
                # user_info['TotalComment'] = res['Data']['Anchor']['TotalComment']
                user_info['likes'] = res['Data']['Anchor']['TotalLike']
                user_info['url'] = res['Data']['Anchor']['TBLiveRoomUrl']
                user_info['userid'] = LiveAnchorId
                user_info['sex'] = ''
                user_info['stars'] = ''
                user_info['age'] = ''
                user_info['personal_profile'] = ''
                user_info['mcn'] = ''
                user_info['production'] = ''

                # user_info['FansInfo'] = res['Data']['FansInfo']
                # user_info['AddData'] = res['Data']['Stat']['AddData']
                # user_info['Data'] = res['Data']['Stat']['Data']
                print(user_info)
                mongo_info.insert_item(user_info)


get_detail()
