# coding: utf-8

import requests
from Crypto.Cipher import AES
import hashlib
import base64
from Crypto.Util.Padding import pad
import datetime
import pprint
import uuid
import urllib3

def get_headers():
    headers = {
        'tenant': '29374364aa63b4aa9d8a7bfc6faf01e9',
        'authtoken': 'cc9f697075a103ec18e7429531de591cbe1c2fc4ca5babb7fc43320942b4d22a',
        'timestamp': '%s' % (datetime.datetime.now()).strftime('%Y-%m-%d') + 'T' + '%s' % ((datetime.datetime.now()) + datetime.timedelta(hours=-8)).strftime('%H:%M:%S') + 'Z',
        # 'timestamp': '2020-08-03T03:22:50Z',
        # 'nonce': '%s' % uuid.uuid1(),
        'nonce': 'fdc3f5dc-83d9-45b5-be1c-866b1fa1f72d',
        'version': '1.0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; 1605-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045318 Mobile Safari/537.36 DeviceBrand/360 VersionName/4.1.0 okhttp/3.8.1 sid/pxrb xkyApp',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'h5.newaircloud.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    return headers

def get_sign():
    key = get_headers().get("authtoken")
    sha256 = hashlib.sha256()
    sha256.update(key.encode())
    res = sha256.digest()
    vi = base64.b64decode(b"AAAAAAAAAAAAAAAAAAAAAA==")
    u = "%s" % get_headers().get("nonce")
    aes_str = "29374364aa63b4aa9d8a7bfc6faf01e9" + u + "%s" % get_headers().get('timestamp') + "1.0" + "1400800" + "27320c53b805b303acf60f26eab6c9bc" + "4"
    # print(aes_str)
    aes = AES.new(res, AES.MODE_CBC, vi)
    pad_pcks7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pcks7)
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypt_text_str = encrypt_text.replace("\n", "")
    # print(encrypt_text_str)
    return encrypt_text_str

def get_params():
    params = {
        'sid': 'pxrb',
        'cid': '14008',
        'lastFileID': '0',
        'rowNumber': '0',
        'deviceID': '27320c53b805b303acf60f26eab6c9bc',
        'version': '5',
        'adLastID': '0',
        'uid': '0',
        'isRec': 'false',
        'source': '4',
        'sign': '%s' % get_sign(),
    }
    # pprint.pprint(params)
    return params

def pxrb_spider():
    url = "https://h5.newaircloud.com/api/getArticlesDy"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, params=get_params(), headers=get_headers(), verify=False).text
    pprint.pprint(res)

pxrb_spider()



