import hashlib
import json
import requests
import datetime
import urllib3


def get_headers():
    ss = hashlib.md5(b"https://a2.liao4fun.com/LoadUsersNew").hexdigest()
    # headers = {
    #     'accept': 'application/json',
    #     'll_csi': '{"android":{"market":"_360","mac":""},"platform":"Android","resolution":{"w":1080,"h":1920,"s":3},"brand":"vivo","model":"V1923A","ov":"5.1.1","av":"1.1.40","lang":"zh","currTime":"%sT%sZ"}' % ((datetime.datetime.now()).strftime('%Y-%m-%d'), ((datetime.datetime.now()) + datetime.timedelta(hours=-8)).strftime('%H:%M:%S')),
    #     'll_ukn': 'B2WNomSYNnc8PDphJLWAMf9kQDc3Gcb0v2jArnsaBeywH5TdNQnu9XAwDKZufc8V87gUfuZBYjxlYCz9TdzhqA==',
    #     'll_pln': '{"id":20173,"phone":"17726454236","nick":"paul","sex":"Male"}',
    #     'll_legal': '%s' % ss,
    #     'Content-Type': 'application/json',
    #     'Content-Length': '180',
    #     'Host': 'a2.liao4fun.com',
    #     'Connection': 'Keep-Alive',
    #     'Accept-Encoding': 'gzip',
    #     'User-Agent': 'okhttp/3.12.1',
    # }

    headers = {
        'accept': 'application/json',
        'll_csi': '{"android":{"market":"_360","mac":""},"platform":"Android","resolution":{"w":900,"h":1600,"s":2},"brand":"Android","model":"MI%209","ov":"5.1.1","av":"1.1.40","lang":"zh","currTime":"' + '%s' % (datetime.datetime.now()).strftime('%Y-%m-%d') + 'T' + '%s' % ((datetime.datetime.now()) + datetime.timedelta(hours=-8)).strftime('%H:%M:%S') + 'Z"}',
        'll_ukn': '1RdM6030J3MoXpkNeROGQ3y4yLkeZWQp99vK/D2aNG2KaUMmnCCsCZwVOnENeKiqQmwoYRZZu9JvCAUIErDHUA==',
        'll_pln': '{"id":32704,"phone":"18391726137","nick":"James","sex":"Male"}',
        'll_legal': '%s' % ss,
        'Content-Type': 'application/json',
        'Content-Length': '164',
        'Host': 'a2.liao4fun.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.1',
    }

    return headers


def get_data():
    datas = '{"page":{"index":1,"size":50},"prefer":{"sex":"Famale","online":false,"maxAge":60,"minAge":16,"realMan":false,"vip":false},"geo":{"lon":116.404207,"lat":39.914288}}'
    # data = datas.encode('utf-8')
    return datas


def get_one():
    url = 'https://a2.liao4fun.com/LoadUsersNew'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = json.loads(requests.post(url, headers=get_headers(), data=get_data(), verify=False).text)
    print(res)


get_one()
