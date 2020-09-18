# coding: utf-8

import time
import pprint
import requests
import urllib3


def get_d1():
    return 56 * int(time.time() / 10)

def get_d2():

    n = get_d1()
    n = str(n)
    i = n[0: 1] + n[3: len(n)]
    res = str((int(i) * 314))[0: len(n)]
    return res

def get_d3():
    n = get_d1()
    n = str(n)
    i = n[0: 1] + n[3: len(n)]
    res = str((int(i) * 128))[0: len(n)]
    return res

def get_d4():
    n = get_d1()
    n = str(n)
    i = n[0: 1] + n[3: len(n)]
    res = str((int(i) * 435))[0: len(n)]
    return res

def get_d5():
    n = get_d1()
    n = str(n)
    i = n[0: 1] + n[3: len(n)]
    res = str((int(i) * 219))[0: len(n)]
    return res

def get_headers():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.2090833223.1592284324; _gid=GA1.2.1101674031.1592284324; Hm_lvt_614c665d6a08fb0dccb1d1744f2756c9=1592284323,1592356595,1592445017; auth={%22token%22:%22972f5ec2c383ad0d85823648b2ad68a2%22%2C%22userId%22:6028869%2C%22wphone%22:%22%22%2C%22wAvatar%22:%22https://imgcdn.meizhuahuyu.com/FrDVjn2jz-3Thaze1eEINiKoeQVm%22%2C%22wNick%22:%22%E6%8B%92%E7%BB%9D%E5%86%8D%E7%8E%A9%22%2C%22adminId%22:1000%2C%22type%22:0%2C%22new%22:false%2C%22vipTime%22:{}%2C%22hasPhone%22:0%2C%22hasInvitedCode%22:0%2C%22isDsbVIP%22:false%2C%22svip%22:false%2C%22dcmVipTime%22:null%2C%22registerTime%22:1592466140}; _gat_gtag_UA_133692412_1=1; Hm_lpvt_614c665d6a08fb0dccb1d1744f2756c9=1592467572',
        'if-none-match': '"b7d0-qg+LmqTbqk3dw2Iwj4fx9ca3j4E"',
        'referer': 'https://www.duanyuer.com/rank/celebrity/total',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }
    return headers

def get_headers1():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '11',
        'content-type': 'application/x-www-form-urlencoded',
        'd1': '%s' % get_d1(),
        'd2': '%s' % get_d2(),
        'd3': '%s' % get_d3(),
        'd4': '%s' % get_d4(),
        'd5': '%s' % get_d5(),
        'Host': 'xcx.meizhuahuyu.com',
        'origin': 'https://www.duanyuer.com',
        'referer': 'https://www.duanyuer.com/user/00QNYoSN',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }
    return headers
# headers = get_headers1()
# headers.pop('content-length')
# headers.pop('content-type')
# print(headers)


url = 'https://xcx.meizhuahuyu.com/douyin/user/getUserDetail'
params = {
    'token': 'c8ce958b9c03de1c5b930d21e29ebd96',
    'toPageCode': '18',
}
data = {
    'id': '00049h3u'
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.post(url, params=params, data=data, headers=get_headers1(), verify=False)
pprint.pprint(res.text)

