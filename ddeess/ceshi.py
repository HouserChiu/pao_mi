# coding: utf-8

import base64
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import pad

'''
采用AES对称加密算法
'''


# str不是32的倍数那就补足为16的倍数
def add_to_32(value):
    while len(value) % 32 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def encrypt_oracle(ori_text):
    # 秘钥
    key = '6b4d7eadad7121ce479295e273237792'
    sha256 = hashlib.sha256()
    sha256.update(key.encode())
    res = sha256.digest()
    vi = base64.b64decode(b"AAAAAAAAAAAAAAAAAAAAAA==")
    # 待加密文本
    # 初始化加密器
    aes = AES.new(res, AES.MODE_CBC, vi)
    # aes = AES.new(add_to_16(key), AES.MODE_CBC, vi)
    # 先进行aes加密
    # encrypt_aes = aes.encrypt(add_to_16(text))
    pad_pkcs7 = pad(ori_text.encode('utf-8'), AES.block_size, style='pkcs7')
    # 用base64转成字符串形式
    encrypt_aes = aes.encrypt(pad_pkcs7)
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)
    print(base64.b64encode(res))

    return encrypted_text


# 解密方法
def decrypt_oralce(ori_text):
    # 秘钥
    key = '6b4d7eadad7121ce479295e273237792'
    vi = base64.b64decode(b"AAAAAAAAAAAAAAAAAAAAAA==")
    sha256 = hashlib.sha256()
    sha256.update(key.encode())
    res = sha256.digest()
    # 密文
    # 初始化加密器
    print("vi=", vi)
    aes = AES.new(res, AES.MODE_CBC, vi)
    # aes = AES.new(add_to_16(key), AES.MODE_CBC, vi)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(ori_text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    print('decrypted_text', decrypted_text)
    return decrypted_text


if __name__ == '__main__':
    ori_text = '''29374364aa63b4aa9d8a7bfc6faf01e924a6c5dc-002f-4f03-8d52-d47f2fcd8e702020-07-31T11:10:45Z1.014015006b4d7eadad7121ce479295e2732377924'''
    entrypted_text = encrypt_oracle(ori_text)
    decrypt_oralce(entrypted_text)