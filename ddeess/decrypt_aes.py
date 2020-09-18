# coding: utf-8

from Crypto.Cipher import AES
import hashlib
import base64
from binascii import b2a_hex, a2b_hex
from Crypto.Util.Padding import pad
import uuid

# def add_to_16(text):
#     if len(text.encode('utf-8')) % 16:
#         add = 16 - (len(text.encode('utf-8')) % 16)
#     else:
#         add = 0
#     text = text + ('\0' * add)
#     return text.encode('utf-8')
#
#
# def encrypt(text):
#     key = "6b4d7eadad7121ce479295e273237792"
#     sha256 = hashlib.sha256()
#     sha256.update(key.encode())
#     res = sha256.digest()
#     mode = AES.MODE_CBC
#     vi = base64.b64decode(b"AAAAAAAAAAAAAAAAAAAAAA==")
#     text = add_to_16(text)
#     cryptos = AES.new(res, mode, vi)
#     cipher_text = cryptos.encrypt(text)
#     # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
#     return b2a_hex(cipher_text)
#
# if __name__ == '__main__':
#     key = "6b4d7eadad7121ce479295e273237792"
#     u = "d77dbc83-6401-43f8-ab63-ff359598d870"
#     aes_str = "29374364aa63b4aa9d8a7bfc6faf01e9" + u + "2020-07-17T03:36:12Z" + "1.0" + "1400800" + key + "4"
#     e = encrypt(aes_str)
#     print(e)
# key_encode = "9klb+ZmJMzeNiqpsaeS9+Eaof5KifTkCnz0cVvuDxTc="
# print(base64.b64decode(key_encode))

key = "6b4d7eadad7121ce479295e273237792"
# key = "0f142b0162c9339283588944ef4daf51"
sha256 = hashlib.sha256()
sha256.update(key.encode())
res = sha256.digest()
vi = base64.b64decode(b"AAAAAAAAAAAAAAAAAAAAAA==")
u = "24a6c5dc-002f-4f03-8d52-d47f2fcd8e70"
aes_str = "29374364aa63b4aa9d8a7bfc6faf01e9" + u + "2020-07-31T11:10:45Z" + "1.0" + "1401500" + key + "4"
print(res)
aes = AES.new(res, AES.MODE_CBC, vi)
# aes = AES.new(res, AES.MODE_CBC, vi)
pad_pcks7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
encrypt_aes = aes.encrypt(pad_pcks7)
encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
encrypt_text_str = encrypt_text.replace("\n", "")
print(base64.b64encode(res))
print(vi)
print(encrypt_text_str)
# aes_str_eve = add_to_16(aes_str)
# result = aes.encrypt(aes_str_eve)
# print(b2a_hex(result))
# from Crypto import Random
#
#
# key = '1234567890!@#$%^'   #秘钥，必须是16、24或32字节长度
# iv = Random.new().read(16) #随机向量，必须是16字节长度
# cipher1 = AES.new(key,AES.MODE_CFB,iv)  #密文生成器,MODE_CFB为加密模式
# encrypt_msg = iv + cipher1.encrypt('我是明文')  #附加上iv值是为了在解密时找到在加密时用到的随机iv
# print('加密后的值为：',base64.b64encode(encrypt_msg))   #将二进制密文转换为16机制显示
#
# cipher2 = AES.new(key,AES.MODE_CFB,iv) #解密时必须重新创建新的密文生成器
# decrypt_msg = cipher2.decrypt(encrypt_msg[16:]) #后十六位是真正的密文
# print('解密后的值为：',decrypt_msg.decode('utf-8'))
#
#
# import base64
# from Crypto.Cipher import AES
#
# '''
# 采用AES对称加密算法
# '''
#
#
# # str不是32的倍数那就补足为16的倍数
# def add_to_32(value):
#     while len(value) % 32 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
#
# def add_to_16(value):
#     while len(value) % 16 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
#
# # 加密方法
# def encrypt_oracle(text):
#     # 秘钥
#     key = 'VW1lMjAxMlRyaXAwMzA5AA=='
#     # 待加密文本
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_ECB)
#     # 先进行aes加密
#     encrypt_aes = aes.encrypt(add_to_16(text))
#     # 用base64转成字符串形式
#     encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
#     print(encrypted_text)
#     return encrypted_text
#
#
# # 解密方法
# def decrypt_oralce(text):
#     # 秘钥
#     key = 'VW1lMjAxMlRyaXAwMzA5AA=='
#     # 密文
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_ECB)
#     # 优先逆向解密base64成bytes
#     base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
#     # 执行解密密并转码返回str
#     decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
#     print('decrypted_text', decrypted_text)
#     return decrypted_text
#
#
# if __name__ == '__main__':
#     text = '''{'aaa': '111', 'bbb': '222'}'''
#     entrypted_text = encrypt_oracle(text)
#
#     decrypt_oralce(entrypted_text)
