import requests
import json
import urllib.parse


def reg():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        'Cookie': 'gr_user_id=6990664e-dc36-4fb0-bfae-4bf0aeaae26b; grwng_uid=1b3fd648-ec78-4698-9bcc-6aeb3e11d41d; __51cke__=; 8e22d1b16f393571_gr_session_id=c0012ae8-fbc4-4fde-a5b4-01981532006b; Hm_lvt_a135ef5290d5317a9a4a051b9fee8f92=1590045505,1590048761,1590109894,1590135808; 8e22d1b16f393571_gr_session_id_c0012ae8-fbc4-4fde-a5b4-01981532006b=true; __tins__20450359=%7B%22sid%22%3A%201590135807427%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201590138164909%7D; __51laig__=5; Hm_lpvt_a135ef5290d5317a9a4a051b9fee8f92=1590136365; JSESSIONID=1C6B938C2BA71007034930B4509CB7F1',
        'Host': 'www.huo1818.com',
        'PC_OPEN_ID': 'oQ4u90T6S56IOfhGIj69huJ4CZO4',
        'Referer': 'http://www.huo1818.com/ranking/goods',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    url = 'http://www.huo1818.com/live-api/v1_2_5/goods/streamer-ranking-list'
    params = {'tag': '', 'type': '1', 'granularity': '1', 'startDate': '2020-05-21', 'endDate': '2020-05-21',
              'goodsType': '', 'liveCategoryName': '美妆个护', 'pageSize': '40', 'pageNo': '1', }
    res = json.loads(requests.get(url, headers=headers, params=params).text)
    # for nickname in res['result']['resultList']:
    #     user_info = {}
    #     user_info['nickname'] = nickname['userName']
    #     # print(json.dumps(user_info))
    #     return user_info
    city = res['result']['resultList'][0]['city']
    # print(type(city))
    return city

