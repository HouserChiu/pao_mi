import requests
import json
import time

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTIzNjI3MDIsInVzZXJJZCI6MTI2OTkwMDI1MjM3NzE1NzYzNCwiY3JlYXRlRGF0ZSI6IjIwMjAtMDYtMTAgMTA6NTg6MjIifQ.l29WtXpf1FMJdITlpwMKG4WTXe3vHXVub5IYEbgTe-A',
    'Connection': 'keep-alive',
    'Content-Length': '101',
    'Content-Type': 'application/json;charset=UTF-8',
    'dcc-href': 'https://www.douchacha.com/uppoint',
    'dcc-r': 'https://www.douchacha.com/workbench',
    'Host': 'api.douchacha.com',
    'Origin': 'https://www.douchacha.com',
    'Referer': 'https://www.douchacha.com/uppoint',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
data = '{"page_no":1,"page_size":20,"params_data":{"label_name":"","period":"DAY","period_value":"20200609"}}'
url = 'https://api.douchacha.com/api/tiktok/ranking/user_list_gain'
params = {
    'ts': '%s' % str(round(time.time() * 1000)),
    'he': 'wpnDrsKlw43DgcKJUMKmJC7DgsOHwqXDvTPCr8K%2Bwrdow4nDpcKIXMOd',
    'sign': '7bc8700f0ad95dfe',
}
res = requests.post(url,data=data,headers=headers,params=params).text
print(res)
