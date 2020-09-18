# import json
# import requests
# url = 'https://api.roseparkapp.com/query/user/other/person/info'
# headers = {
#     'x-mac': '74:ac:5f:ca:d6:47',
#     'x-system-plateform': 'android',
#     'x-network': 'wifi',
#     'x-version': '1.2.0',
#     'x-terminal-type': '360',
#     'x-correlation-id': 'cac82dcc2f7b675c',
#     'x-crfs-token': 'r4CJC1ODl/3eYOGBUhxrXSnI1zQTfhJ7m2YV31YpZS12QMdmU39tZ87wXZaTbK+l_PDjrrVMwwh68Lqks4hYmcA==',
#     'Content-Type': 'application/json; charset=utf-8',
#     'Content-Length': '124',
#     'Host': 'api.roseparkapp.com',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip',
#     'User-Agent': 'okhttp/3.14.4',
# }
#
# datas = '{"beViewUID":107294,"latitude":30.6491,"longitude":104.083021}'
# data = datas.encode('utf-8')
# res = json.loads(requests.post(url, headers=headers, data=data).text)
# print(res)


import requests
# import os
#
# path = './'
# isExists = os.path.exists('./headImage')
#不存在则创建
# if not isExists:
#     os.mkdir('./headImage')
# else:
#     pass
# os.chdir('headImage')
# with open('image' + '.jpg','wb') as f:
#     img = requests.get('https://file.roseparkapp.com/AAC0Gy8q/332ef30b8e195935e1b29a543ebc9e07.jpg').content
#     f.write(img)

"https://file.roseparkapp.com"

#存在返回True,不存在返回False
# print(os.path.isfile('image.jpg'))
nickname = '薇薇佳\\:*?"><|'
nickname1 = nickname.replace("\\","1")
nickname2 = nickname1.replace("/","2")
nickname3 = nickname2.replace(":","3")
nickname4 = nickname3.replace("*","4")
nickname5 = nickname4.replace("?","5")
nickname6 = nickname5.replace('"',"6")
nickname7 = nickname6.replace("<","7")
nickname8 = nickname7.replace(">","8")
nickName = nickname8.replace("|","9")
print(nickName)



