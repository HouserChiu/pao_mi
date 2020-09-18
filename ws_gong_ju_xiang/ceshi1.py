# coding: utf-8

import json

import pymysql
import requests
from Crypto.Cipher import AES
import hashlib
import base64
from Crypto.Util.Padding import pad, unpad
import datetime
import pprint
import urllib3
import re


def result_decrypt():
    key = '2018-CQSDX-SOFT.'.encode("utf-8")
    # aes = AES.new(key, AES.MODE_ECB)
    # aes_str = '{"typeId":"","source":"0","pageIndex":29,"pageSize":40}'
    # res = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    # encrypt_aes = aes.encrypt(res)
    # encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '')
    # # 请求数据
    # headers = {
    #     'Cookie': 'JSESSIONID=8b5942cc-1f4f-4b85-9bf8-78a1297276f8; Domain=.aliyizhan.com; Path=/; HttpOnly',
    #     'Content-Type': 'application/wxt;charset=UTF-8',
    #     'Content-Length': '88',
    #     'Host': 'gz.aliyizhan.com',
    #     'Connection': 'Keep-Alive',
    #     'Accept-Encoding': 'gzip',
    #     'User-Agent': 'okhttp/3.11.0',
    # }
    # data = "%s" % encrypted_text
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # res = requests.post("https://gz.aliyizhan.com/market/getMarketArchivesMouths.action?marketCode=gz", headers=headers,
    #                     data=data, verify=False).text
    res = "9nmp0PJa4ynx+HjjjG7xqvJrA6xC1K5leZ8isszQPWVqkyCfi3C69BVYy4emVjbNgBssK0EqAJBBoK14dMDy/oHsxagoI3PBvoyp6dLXWRPcZwkD0tRHHL8Aa6V2m6+a7mesSm1hKl5MY9Ew/pMDNwMzcjB4grKcpl3WxCMeQSrOijKeEIdULgxCkDDxZ5knNwDuui03vum98tBjgnyBcp+zTXZMIIg3QBI1irpGqiOI//ZpL67VkUMaBtxyP3w1"
    # res = "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"
    # aes_str = base64.b64decode(res)
    # vi = "A-16-Byte-String"
    # aes = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
    # # res1 = aes.decrypt(aes_str)
    # base64_decrypted = base64.decodebytes(aes_str.encode(encoding='utf-8'))
    # decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    # print('decrypted_text', decrypted_text)

    aes_str = base64.b64decode(res)
    vi = "A-16-Byte-String"
    aes = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
    res1 = aes.decrypt(aes_str)
    res2 = res1.decode(encoding='utf-8')
    res3 = res2.replace('\r', '').replace('\n', '')
    print(res3)



result_decrypt()