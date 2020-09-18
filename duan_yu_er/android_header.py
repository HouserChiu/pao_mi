import time

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
        'Host': 'xcx.meizhuahuyu.com',
        'Connection': 'keep-alive',
        'd2': '%s' % get_d2(),
        'charset': 'utf-8',
        'content-type': 'application/json',
        'd3': '%s' % get_d3(),
        'version': '106',
        'd1': '%s' % get_d1(),
        'd4': '%s' % get_d4(),
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.10.1580(0x27000A32) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64',
        'type': '2',
        'd5': '%s' % get_d5(),
        'Accept-Encoding': 'gzip',
        'Referer': 'https://servicewechat.com/wxb282b72c05107453/7/page-frame.html',
    }
    return headers

# def get_headers1():
#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'content-length': '11',
#         'content-type': 'application/x-www-form-urlencoded',
#         'd1': '%s' % get_d1(),
#         'd2': '%s' % get_d2(),
#         'd3': '%s' % get_d3(),
#         'd4': '%s' % get_d4(),
#         'd5': '%s' % get_d5(),
#         'origin': 'https://www.duanyuer.com',
#         'referer': 'https://www.duanyuer.com/user/00QNYoSN',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#     }
#     return headers
# headers = get_headers1()
# headers.pop('content-length')
# headers.pop('content-type')
# print(headers)


# url = 'https://xcx.meizhuahuyu.com/douyin/user/getUserDetail'
# params = {
#     'token': '11fbd2336ca6848d064eca2a80d0fde8',
#     'toPageCode': '18',
# }
# data = {
#     'id': '00049h3u'
# }
# res = requests.post(url, params=params, data=data, headers=headers, verify=False)
# print(res.text)
# print(res.status_code)
