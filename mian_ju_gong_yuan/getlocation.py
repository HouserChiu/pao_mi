import requests
import json


def get_location():
    url = 'https://restapi.amap.com/v3/geocode/regeo'
    params = {
        'output': 'json',
        'location': '114.9939165581597,31.08201524522569',
        'key': '4dc8c34c6e76aab32828fe50046b8f93',
        'radius': '1000',
        'extensions': 'all',
    }

    response = json.loads(requests.get(url, params=params).text)
    res = response['regeocode']['formatted_address']
    print(res)


get_location()
