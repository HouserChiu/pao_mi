import os
import re
import time
import requests
import json
import urllib3


def get_params():
    params_list = []
    for i in range(1, 24):
        params = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '头像',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '0',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': '头像',
            's': '0',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': 'head',
            # 'pn': '120',
            'pn': '%s' % (30 * i),
            'rn': '30',
            'gsm': '1e',
            '%s' % int(round(time.time() * 1000)): '',
        }
        params_list.append(params)
    return params_list


def one_page():
    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'BDqhfp=%E5%A4%B4%E5%83%8F%20%E5%BD%B1%E8%A7%86%20%E7%BB%A7%E6%89%BF%E8%80%85%E4%BB%AC%26%2600-10-10%26%260%26%261; BIDUPSID=370D8E33783C441E17927CA08DA16C39; PSTM=1590383576; BAIDUID=370D8E33783C441E529E1437DADA8931:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31728_1447_21094_31110_31254_31592_31270_31463_31714_30824_26350; delPer=0; PSINO=6; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; BCLID=9091013184483427405; BDSFRCVID=gZ8OJeC62G_dhQcuzztJudjrMeImko7TH6aoPjML24WJ1NEV9qNxEG0Pjf8g0Kubqm_IogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJAq_I8MtII3f6rx-trWMt6H-UnLqM3GbgOZ0l8KtJ6tEt54-Ro02lJQ5fOBbfr-2Tuq-p7mWIQHDPbhhUop-JktKPTK5M6Dtg64KKJxWUKWeIJo5tKh3RtOhUJiBhvMBan7LKJIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_xDjKMDjb0eND8qRO0K-o2WbCQ-boN8pcNLTDKhq-fyGoH-RTEQj6t0nc-BR5sOUjh-lO1j4_e2bbfq4vTKKrhMMIyHCJxKq5jDh38XjksD-RC5JoLX25y0hvcyn3cShn6DMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDG0DJj0DJbIs_DIX-nTjKROvhjRJW6kgyxomtjjxXKn3bROaMtcMO45gMR5YbfFDMUPfLUkqKCOTBq61tDbROCj8QqDBKfCbQttjQPThfIkja-5t-R6rOJ7TyURibU47yhtj0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BJCtMMCQP; userFrom=www.baidu.com',
        'Host': 'image.baidu.com',
        'Referer': 'http://image.baidu.com/search/index?ct=201326592&z=0&s=0&tn=baiduimage&ipn=r&word=%E5%A4%B4%E5%83%8F%20%E5%BD%B1%E8%A7%86%20%E7%BB%A7%E6%89%BF%E8%80%85%E4%BB%AC&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1461834053046_R&ic=0&se=&sme=&width=&height=&face=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    params_list = get_params()
    image_urls = []
    for params in params_list:
        url = 'http://image.baidu.com/search/acjson'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = json.loads(requests.get(url, params=params, headers=headers, verify=False).text)
        image_url = []
        image_urll = []
        for headimg in res['data']:
            image_url.append(headimg)
        for img in image_url[0:30]:
            image_urll.append(img['middleURL'])
        image_urls.append(image_urll)
    # print(image_urls)
    return image_urls
# one_page()

def sli():
    image_urlss = one_page()
    temp_list = []
    for image_urls in image_urlss:
        for image_url in image_urls:
            temp_list.append(image_url)
    return temp_list
# sli()


def download_img():
    image_url = sli()
    for url in image_url:
        print(url)
        name = re.search('http.*?\=.*?\,(\d+).*?jpg', url).group(1)
        with open('%s' % name + '.jpg', 'wb') as f:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            img = requests.get(url).content
            f.write(img)
#     image_urlss = one_page()
#     for image_urls in image_urlss:
#         for image_url in image_urls:
#             if os.path.isfile('%s' % image_url + '.jpg'):
#                 pass
#             else:
#                 try:
#                     with open('%s' % image_url + '.jpg', 'wb') as f:
#                         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#                         img = requests.get(image_url, verify=False).content
#                         f.write(img)
#                 except OSError:
#                     print(image_url)


download_img()