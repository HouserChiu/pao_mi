# coding: utf-8

import json
import random
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
import time


def result_decrypt():
    for page in range(1, 2):
        print(page)
        key = '2018-CQSDX-SOFT.'.encode("utf-8")
        vi = "A-16-Byte-String"
        aes = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
        # 推荐,只有1页
        aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page

        # # 一件代发,2页
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846608000"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # 服装鞋包,93页
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609000"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 美妆护肤,119
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609001"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 珠宝首饰13
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609002"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 母婴童装20
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609003"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 家居生活25
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609004"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 电子数码11
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609005"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 美食水果34
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609006"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page
        # # 其他货源61
        # aes_str = '{"android_channel":"tencent","android_version":30,"content":{"pageNo":"%s","type_id":"1533103846609007"},"device_id":"android_913eea43","language":"zh","os":"android-25-360-1605-A01"}' % page


        res = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
        encrypt_aes = aes.encrypt(res)
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '').replace('+', '%2B').replace('/', '%2F').replace('=', '%3D')
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
        res = requests.post("http://wsgjx.cqsdx.cn/wsgjx/app/supply/list_recommend", headers=headers,
                            data=data, verify=False).text
        print(res)
        res_temp = json.loads(res)
        aes_str1 = base64.b64decode(res_temp['content'])
        aes1 = AES.new(key, AES.MODE_CBC, bytes(vi, encoding='utf-8'))
        res1 = aes1.decrypt(aes_str1)
        res2 = res1.decode(encoding='utf-8')
        res3 = res2.replace('\r', '').replace('\n', '').replace('\t', '')
        print(res3)
        res4 = json.loads('{"' + re.search('totalRow(.*?)\}\]\}', res3, re.S).group(1) + '}]}')
        for store_info in res4['list']:
            store_info_dict = {}
            store_info_dict['title'] = store_info['title']
            store_info_dict['wx_number'] = store_info['wx_number']
            store_info_dict['phone'] = store_info['phone']
            store_info_dict['cate'] = "推荐"
            pprint.pprint(store_info_dict)

            conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root",
                                   database="gong_xiang_hy",
                                   charset="utf8mb4")
            cursor = conn.cursor()
            try:
                sql = "INSERT INTO ws_gongjuxiang (title, wx_number, phone, cate) VALUE ('%s','%s','%s','%s')"
                base = (store_info_dict['title'], store_info_dict['wx_number'], store_info_dict['phone'], store_info_dict['cate'])
                cursor.execute(sql % base)
                conn.commit()
            except:
                conn.rollback()
            conn.close()
        sleep_time = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        time.sleep(random.choice(sleep_time))


result_decrypt()

