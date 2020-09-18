# coding: utf-8
import json

import requests
import urllib3
from requests_toolbelt import MultipartEncoder

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer1593333006805-e72abe8c-9b68-456b-bdaa-85a85c6832a7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '851',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryOLBTheinO0rm8mLD',
    'Cookie': 'user-token={%22access_token%22:%221593333006805-e72abe8c-9b68-456b-bdaa-85a85c6832a7%22%2C%22refresh_token%22:%22ebc99962-7d7c-4b68-bbc4-c873ec16a326%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:604799}; Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1593332971,1593592472; localeLanguage=zh; luonetUUID=cZ91c9pGsj1593592475722; deviceId=cZ91c9pGsj1593592475722-376831e25d601397e58ad070d554fb3f; connect.sid=s%3AhDB6zvEu3rTZOMhar8u5VC4gA2zS1VIK.69Gz%2FnjERxsLIefdMVKG1ZAAxu8f7PJZi7iDKv17LqA; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1593592499; JSESSIONID=7DBC314C98E432B083B3B64D550C9274',
    'deviceId': 'cZ91c9pGsj1593592475722-376831e25d601397e58ad070d554fb3f',
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
url = 'https://www.luonet.com/dcapi/api/douyinUserReport/list'
data = {
    's_fdStartTime': '2020-06-29 00:00:00',
    's_fdType': '1',
    's_Like_fdArea': '',
    's_MATCH_fdLabels': '',
    's_fdGrade': '',
    'pageIndex': '1',
    'reLoad': 'false',
    'limit': '30',
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
m = MultipartEncoder(data)
headers['Content-Type'] = m.content_type
res = json.loads(requests.post(url, headers=headers, data=m, verify=False, timeout=10).text)
print(res)

