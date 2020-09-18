import requests
import json
url = 'https://xd.newrank.cn/xdnphb/nr/cloud/douyin/mini/rank/hotAccountAllRankList'
headers = {
    'Host':'xd.newrank.cn',
    'Connection':'keep-alive',
    'Content-Length':'76',
    'cookie':'',
    'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.82 Mobile Safari/537.36 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
    'charset':'utf-8',
    'Accept-Encoding':'gzip,compress,br,deflate',
    'content-type':'application/json',
    'Referer':'https://servicewechat.comwx55778a0d7b3048c4/16/page-frame.html',
}

data = {
    "type":"","date_type":"days","date":"2020-05-06","start":1,"size":20
}

response = requests.post(url,headers=headers,data=json.dumps(data)).text
res = json.loads(response)
print(res)