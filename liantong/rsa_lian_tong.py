# coding: utf-8

import base64
import datetime
import pprint

import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def decrypt(msg):
    # 读取文件中的公钥
    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc+CZK9bBA9IU+gZUOc6FUGu7yO9WpTNB0PzmgFBh96Mg1WrovD1oqZ+eIF4LjvxKXGOdI79JRdve9NPhQo07+uqGQgE4imwNnRx7PFtCRryiIEcUoavuNtuRVoBAm6qdB0SrctgaqGfLgKvZHOnwTjyNqjBUxzMeQlEC2czEMSwIDAQAB"
    lll = RSA.importKey(base64.b64decode(public_key))
    # 进行加密
    clipher = PKCS1_v1_5.new(lll)
    clipher_text = base64.b64encode(clipher.encrypt(msg.encode(encoding="utf-8")))
    print(str(clipher_text, 'utf8'))
    # 加密通过base64进行编码
    return str(clipher_text, 'utf8')

def requ():
    url = 'https://m.client.10010.com/mobileService/login.htm'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '669',
        'Host': 'm.client.10010.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.9.1',
    }
    data = {
        'isRemberPwd': 'true',
        'deviceId': '865166022143641',
        'password': '%s' % decrypt('159357'),
        'netWay': 'WIFI',
        'mobile': '%s' % decrypt('13111877109'),
        'yw_code': '',
        'timestamp': '%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        'appId': '1f7af72ad6912d306b5053abf90c7ebbd30555efe10cf5c0fa793f0b853420d3b7de34de35eadd47ce7d25617f96afe3df78ab0be42ad17113c5df9dbd6772f4',
        'keyVersion': '',
        'deviceBrand': 'vivo',
        'pip': '172.16.2.12',
        'provinceChanel': 'general',
        'version': 'android@6.002',
        'deviceModel': 'V1923A',
        'deviceOS': 'android5.1.1',
        'deviceCode': '865166022143641',
    }
    pprint.pprint(data)
    res = requests.post(url, headers=headers, data=data, verify=False).text
    pprint.pprint(res)
requ()