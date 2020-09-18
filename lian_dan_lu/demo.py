import requests

def req():
    res = requests.get('http://127.0.0.1:5000')
    print(res.text)
    return res

if __name__ == '__main__':
    req()
