import requests
import json

json_data = {"name": '123', "password": '123456'}
# res = requests.get('http://127.0.0.1:5000/')
res = requests.post(url='http://127.0.0.1:5000/', json=json_data)
print(res.text)
print(type(res.text))
