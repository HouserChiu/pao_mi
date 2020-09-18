import json
import requests



def get_one():
    data = {
        's_fdStartTime': '2020-06-03 00:00:00',
        's_fdType': '1',
        's_Like_fdArea': '',
        's_MATCH_fdLabels': '萌宠',
        's_fdGrade': '',
        'pageIndex': '1',
        'reLoad': 'false',
        'limit': '30',
    }
#     datas = """
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="s_fdStartTime"
#
# 2020-06-03 00:00:00
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="s_fdType"
#
# 1
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="s_Like_fdArea"
#
#
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="s_MATCH_fdLabels"
#
# 萌宠
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="s_fdGrade"
#
#
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="pageIndex"
#
# 1
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="reLoad"
#
# false
# ------WebKitFormBoundary1is57E3Gg9bF8KA1
# Content-Disposition: form-data; name="limit"
#
# 30
# ------WebKitFormBoundary1is57E3Gg9bF8KA1--
#     """
#     data = datas.encode('UTF-8')
    # data = {
    #     "s_fdStartTime":(None,'2020-06-03 00:00:00'),
    #     "s_fdType":(None,1),
    #     "s_Like_fdArea":(None,None),
    #     "s_MATCH_fdLabels":(None,'摄影'),
    #     "s_fdGrade":(None,None),
    #     "pageIndex":(None,1),
    #     "reLoad":(None,False),
    #     "limit":(None,30)
    # }
    # data = OrderedDict([
    #     ("s_fdStartTime", (None,'2020-06-03 00:00:00')),
    #     ("s_fdType", (None,1)),
    #     ("s_Like_fdArea", (None,None)),
    #     ("s_MATCH_fdLabels", (None,'摄影')),
    #     ("s_fdGrade", (None,None)),
    #     ("pageIndex", (None,1)),
    #     ("reLoad", (None,'false')),
    #     ("limit", (None,30)),
    # ]
    # )
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer1591326861866-151eb5bf-fa5e-4dfb-b918-839d9b07e4cc',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '853',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiT4nbq4IM3Iha5zh',
        'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1591327831; localeLanguage=zh; luonetUUID=NNeDEP8Dz21591327832127; deviceId=NNeDEP8Dz21591327832127-6b1c6d8dd24d62f41a42f503e033737b; user-token={%22access_token%22:%221591326861866-151eb5bf-fa5e-4dfb-b918-839d9b07e4cc%22%2C%22refresh_token%22:%22c831600e-2fe8-4c33-86da-163674620968%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:603777}; connect.sid=s%3AIz3OUFdIRjeGoxRMpFaT2SporBJEGMcW.wRkrEdV1kIh7g7lBihG7VESbWPit90q3cKAmcsJPf8Y; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591349371; JSESSIONID=6C2C6CEDDA950DDF0144F548F961563F',
        'deviceId': 'NNeDEP8Dz21591327832127-6b1c6d8dd24d62f41a42f503e033737b',
        'Host': 'www.luonet.com',
        'If-Modified-Since': 'Thu, 01 Jun 1970 00:00:00 GMT',
        'Origin': 'https://www.luonet.com',
        'Referer': 'https://www.luonet.com/billboard/celebrity/hot',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'shouldIntercept': 'true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # print(headers)



    url = 'https://www.luonet.com/dcapi/api/douyinUserReport/list'
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.post(url, headers=headers, json=data)
    print(res.text)
get_one()
