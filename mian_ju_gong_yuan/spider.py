import requests
import json
import time
from mongo_info import mongo_info_mjgy


def get_params():
    params_list = []
    for city_num in range(1, 355):
        params = {
            's': 'female',
            't': 'hotest',
            'a': '%d' % city_num,
            'lng': '104.083021',
            'lat': '30.6491',
        }
        params_list.append(params)
    return params_list


def get_list_info():
    params_list = get_params()
    id_lists = []
    for params in params_list:
        url = 'https://api.masksaloon.com/query_users'
        headers = {
            'Host': 'api.masksaloon.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Cookie': 'session=.eJw1z0tOxTAMheG9ZMwgdhzXuZupHD8EQhSU9o4Qe6cSYgPn_8532XPF-Voe13rGS9nfvDxKbdEQhtQKwltNd4MWiWGoXI209dCRyKMRyMY2hgp5Anum6EYVrYGPkQLKGoFdkCOnTmQ1sCSPOp0JGWD2mdbn3exAXdi93JCvWB96xHH90-xcuV-f73HcQhelht3QOB2yj_TWTXhuE4cBQU8ddav30vOM9XcLCVsrP7_sFUbT.XrjAfQ.ZH417A1vTFZw6wBT_L61JurWs8M',
            'User-Agent': 'okhttp/3.12.1',
            'If-Modified-Since': 'Mon, 11 May 2020 03:03:25 GMT',
        }
        res = json.loads(requests.get(url, params=params, headers=headers).text)
        id_infos = res['user_list']
        id_list = []
        for id_info in id_infos:
            id_list.append(id_info['user_id'])
        id_lists.append(id_list)
    return id_lists


def get_location(longitude, latitude):
    url = 'https://restapi.amap.com/v3/geocode/regeo'
    params = {
        'output': 'json',
        'location': '%f,%f' % (longitude, latitude),
        'key': '4dc8c34c6e76aab32828fe50046b8f93',
        'radius': '1000',
        'extensions': 'all',
    }
    response = json.loads(requests.get(url, params=params).text)
    res = response['regeocode']['formatted_address']
    return res


def get_detail_info():
    idss = get_list_info()
    for ids in idss:
        for id in ids:
            if id:
                url = 'https://api.masksaloon.com/get_user_details?user_id=' + str(id)
                headers = {
                    'Host': 'api.masksaloon.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'Cookie': 'session=.eJw1z0tOxTAMheG9ZMwgdhzXuZupHD8EQhSU9o4Qe6cSYgPn_8532XPF-Voe13rGS9nfvDxKbdEQhtQKwltNd4MWiWGoXI209dCRyKMRyMY2hgp5Anum6EYVrYGPkQLKGoFdkCOnTmQ1sCSPOp0JGWD2mdbn3exAXdi93JCvWB96xHH90-xcuV-f73HcQhelht3QOB2yj_TWTXhuE4cBQU8ddav30vOM9XcLCVsrP7_sFUbT.XrjAfQ.ZH417A1vTFZw6wBT_L61JurWs8M',
                    'User-Agent': 'okhttp/3.12.1',
                }
                user_infos = json.loads(requests.get(url, headers=headers).text)

                user_info = {}
                user_info['user_id'] = id
                user_info['nickname'] = user_infos['user_details']['nickname']
                user_info['sex'] = '女'
                user_info['age'] = user_infos['user_details']['age']
                user_info['avatar'] = user_infos['user_details']['avatar']
                user_info['description'] = user_infos['user_details']['description']
                user_info['height'] = user_infos['user_details']['height']
                user_info['weight'] = user_infos['user_details']['weight']
                user_info['bust'] = user_infos['user_details']['bust']
                user_info['cup'] = user_infos['user_details']['cup']

                if user_infos['user_details']['geo_point']:
                    longitude = user_infos['user_details']['geo_point']['longitude']
                    latitude = user_infos['user_details']['geo_point']['latitude']
                    geo_city = get_location(longitude, latitude)
                    user_info['geo_city'] = geo_city
                else:
                    user_info['geo_city'] = ''

                timeStamp = user_infos['user_details']['last_time']
                timeArray = time.localtime(timeStamp)
                eve_time = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
                user_info['last_time'] = eve_time

                if user_infos['user_details']['confirmed'] == 1:
                    user_info['confirmed'] = '已认证'
                else:
                    user_info['confirmed'] = '未认证'
                photo_infos = user_infos['user_details']['photos']

                for photo_info in photo_infos:
                    user_info['photo_url'] = photo_info['photo_url']
                print(user_info)
                mongo_info_mjgy.insert_item(user_info)


get_detail_info()
