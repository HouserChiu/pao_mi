# -*- coding: utf-8 -*-

import requests
import time
import frida
from f_rpc import on_message, js_code
import base64
import json
import pprint
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad


def get_ciphertext():
    session = frida.get_usb_device().attach('com.lawyee.wenshuapp')
    script = session.create_script(js_code())
    script.on('message', on_message)
    script.load()
    ll = script.exports.getsig()
    session.detach()
    return ll


def get_data():
    ids = time.strftime("%Y%m%d%H%M%S")
    ciphertext = get_ciphertext()
    json_str = {"id": "%s" % ids, "command": "queryDoc",
                "params": {"pageNum": "1", "sortFields": "s50:desc", "ciphertext": "%s" % ciphertext,
                           "devid": "486d96d7b04c4d8f99c58d09dca762ef", "devtype": "1", "pageSize": "20",
                           "queryCondition": [{"key": "s8", "value": "02"}]}}
    eve_str = json.dumps(json_str).encode("utf-8")
    print(eve_str)
    str_data = base64.b64encode(eve_str)
    data = "request=" + str_data.decode()
    print(data)
    # pprint.pprint(data)
    return data
get_data()

# 请求接口
def requ():
    url = "http://wenshuapp.court.gov.cn/appinterface/rest.q4w"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; 1605-A01 Build/NMF26F)',
        'Host': 'wenshuapp.court.gov.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Content-Length': '890',
    }
    res = requests.post(url, headers=headers, data=get_data()).text
    res_eve = json.loads(res)
    content = res_eve['data']['content']
    key1 = res_eve['data']['secretKey']
    iv = time.strftime("%Y%m%d")
    des3 = DES3.new(key=key1.encode(), mode=DES3.MODE_CBC, iv=iv.encode())
    decrypted_data = des3.decrypt(base64.b64decode(content))
    plain_text = unpad(decrypted_data, DES3.block_size).decode()
    result = json.loads(plain_text)
    pprint.pprint(result)


# requ()
