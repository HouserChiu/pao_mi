# coding: utf-8


from pyDes import des, CBC, PAD_PKCS5
import binascii
import base64

# 秘钥
# KEY = 'mHAxsLYz'
KEY = '88880805'

def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = bytearray([1, 2, 3, 4, 5, 6, 7, 8])
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s.encode('utf-8'), padmode=PAD_PKCS5)
    # print(en)
    print(str(base64.b64encode(en), 'utf-8'))
    # print(binascii.b2a_hex(en))
    # return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    # de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    de = k.decrypt(base64.b64decode(s), padmode=PAD_PKCS5)
    print(de)
    # return de

des_encrypt('13888888888|20200805')
des_descrypt("PXWVqYv/gJ1e7qlmi0f0pQ==")


