import requests
from requests_toolbelt import MultipartEncoder

url = 'https://www.luonet.com/dcapi/api/douyinUserReport/list'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer1591326861866-151eb5bf-fa5e-4dfb-b918-839d9b07e4cc',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '853',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryPfrplkBrbVKQjLrf',
    'Cookie': 'Hm_lvt_7b7f8c848620f517ba2e97ac5881177a=1588860131,1591366181; localeLanguage=zh; luonetUUID=aYN6fQ12A31591366182522; deviceId=aYN6fQ12A31591366182522-37859fd1f8e0879d85913fcc66cd4970; connect.sid=s%3AnotztZzLVYW8imlMX5p9jQhSMpnAFFKH.oNnEjr1aRdT7tyYIFB8aAQubkkOcRADDG2aQrssKChE; user-token={%22access_token%22:%221591326861866-151eb5bf-fa5e-4dfb-b918-839d9b07e4cc%22%2C%22refresh_token%22:%22c831600e-2fe8-4c33-86da-163674620968%22%2C%22scope%22:%22select%22%2C%22token_type%22:%22bearer%22%2C%22expires_in%22:565437}; Hm_lpvt_7b7f8c848620f517ba2e97ac5881177a=1591366248; JSESSIONID=8705B1205B54BFF1A940E48012FDB7CB',
    'deviceId': 'aYN6fQ12A31591366182522-37859fd1f8e0879d85913fcc66cd4970',
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
data = {
    's_fdStartTime': '2020-06-04 00:00:00',
    's_fdType': '1',
    's_Like_fdArea': '',
    's_MATCH_fdLabels': '娱乐',
    's_fdGrade': '',
    'pageIndex': '1',
    'reLoad': 'false',
    'limit': '30',
}

m = MultipartEncoder(data)
headers['Content-Type'] = m.content_type
# print(headers['Content-Type'])
res = requests.post(url, data=m, headers=headers, timeout=10)
print(res.text)
