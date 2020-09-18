# coding: utf-8

import json
import re
import pymysql
import requests
from Crypto.Cipher import AES
import hashlib
import base64
from Crypto.Util.Padding import pad, unpad
import datetime
import pprint
import urllib3

def result_decrypt():
    key = '2018-CQSDX-SOFT.'.encode("utf-8")
    vi = "A-16-Byte-String"
    aes = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
    # 服装鞋包
    aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"1","type_id":"1533103846608000"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}'

    res = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(res)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '').replace('+',
                                                                                                      '%2B').replace(
        '/', '%2F').replace('=', '%3D')
    # 请求数据
    headers = {
        'header_version': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '234',
        'Host': 'wsgjx.cqsdx.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.7.2',
    }
    data = "v=" + "%s" % encrypted_text
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.post("http://wsgjx.cqsdx.cn/wsgjx/app/supply/list", headers=headers,
                        data=data, verify=False).text
    res_temp = json.loads(res)
    aes_str1 = base64.b64decode(res_temp['content'])
    aes1 = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
    res1 = aes1.decrypt(aes_str1)
    res2 = res1.decode(encoding='utf-8')
    res3 = res2.replace('\r', '').replace('\n', '').replace('\t', '')
    print(res3)




result_decrypt()