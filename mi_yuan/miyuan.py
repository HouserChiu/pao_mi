import os
import requests
import json
from mongo_oper import mongo_info_my
import urllib3


def get_headers():
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; 1605-A01 Build/NMF26F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Content-Type': 'application/json;charset=utf-8',
        'Content-Length': '229',
        'Host': 'miyuanserver.top',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    return headers


def get_city():
    url = 'https://miyuanserver.top/appc/sysDataMgr/getHomeAllCityInfo'
    data = '{"header":{"version":"0.3","platform":"Android_7.1.1_1605-A01","appname":"miyuanapp"},"data":{"token":"cf16faa9-c039-4117-b49e-19fc3b9ec7a1"}}'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(url, headers=get_headers(), data=data, verify=False).text)
    city_list = []
    for city in res['data']:
        city_list.append(city['cnames'])
    return city_list
    # print(city_list)


# get_city()
def get_data():
    citiess = get_city()
    data_list = []
    for cities in citiess:
        for city in cities:
            datas = '{"header":{"version":"0.3","platform":"Android_7.1.1_1605-A01","appname":"miyuanapp"},"data":{"sex":"m","page":"2","vipstate":"","location":"104.08068848_30.65156364","userid":11953,"city":"%s","online":"0","authtstate":""}}' % city
            data = datas.encode('utf-8')
            data_list.append(data)
    return data_list


# get_data()
def get_one():
    data_list = get_data()
    userid_lists = []
    for data in data_list:
        url = 'https://miyuanserver.top/appc/userMgr/searchHomeUserByCondition'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.post(url, headers=get_headers(), data=data, verify=False).text)
        if res['data']['list'] != '':
            userid_list = []
            for user_id in res['data']['list']:
                userid_list.append(user_id['userid'])
            userid_lists.append(userid_list)
    return userid_lists


def get_two():
    user_id_list = get_one()
    for userid in user_id_list:
        for user_id in userid:
            data = '{"header":{"version":"0.3","platform":"Android_7.1.1_1605-A01","appname":"miyuanapp"},"data":{"operuserid":11953,"token":"cf16faa9-c039-4117-b49e-19fc3b9ec7a1","readuserid":"%s","location":"104.08068848_30.65156364"}}' % user_id
            url = 'https://miyuanserver.top/appc/userMgr/getUserOPerInfoById'
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            res = json.loads(requests.post(url, data=data, headers=get_headers(), verify=False).text)
            user_info = {}
            user_info['age'] = res['data']['age']
            user_info['constellation'] = res['data']['constellation']
            user_info['headimg'] = res['data']['headimg']
            user_info['height'] = res['data']['height']
            user_info['hopeuser'] = res['data']['hopeuser']
            # if res['data']['locationcity']:
            #     user_info['locationcity'] = res['data']['locationcity']
            # else:
            #     user_info['locationcity'] = ''
            try:
                user_info['locationcity'] = res['data']['locationcity']
            except KeyError:
                user_info['locationcity'] = ''
            user_info['nickname'] = res['data']['nickname']
            user_info['onlinetime'] = res['data']['onlinetime']
            user_info['partycity'] = res['data']['partycity']
            user_info['partymode'] = res['data']['partymode']
            user_info['personinfo'] = res['data']['personinfo']
            user_info['qq'] = res['data']['qq']
            user_info['relrange'] = res['data']['relrange']
            user_info['sex'] = '男'
            user_info['userid'] = res['data']['userid']
            user_info['wechat'] = res['data']['wechat']
            user_info['weight'] = res['data']['weight']
            user_info['third_id'] = 'my' + '_' + str(user_info['userid'])
            if os.path.isfile('%s' % user_info['third_id'] + '.jpg'):
                pass
            else:
                with open('%s' % user_info['third_id'] + '.jpg', 'wb') as f:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    img = requests.get(user_info['headimg'], verify=False).content
                    f.write(img)
            print(user_info)
            mongo_info_my.insert_item(user_info)


get_two()
