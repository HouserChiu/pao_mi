import re
import requests
from lxml import etree

def get_headers():
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'chl=key=baidu-dy&word=6aOe55Oc; Hm_lvt_b9de64757508c82eff06065c30f71250=1592191762; Hm_lpvt_b9de64757508c82eff06065c30f71250=1592191762; kschl=key=feigua2_baidu-dy; Hm_lvt_dfceea9861b5ceea1cc1a25232e14f4a=1592191763; Hm_lpvt_dfceea9861b5ceea1cc1a25232e14f4a=1592191763; ASP.NET_SessionId=mchz1eqlbfck0sjfnjcjcqtx; _uab_collina=159219176349251865852504; KUAISHOU=UserId=b393c1e9e1f9aba0&NickName=ff2c429d257b341751d468d3ed7bda7e&checksum=155dbc595ef2&KUAISHOULIMITID=ae1dcdaa92de45449466cb5ade4b1d09; 983f118f7e97e6aa57a73b62a7a1e673=11c014ebad67002f7ad1f454a99db94fffb006cb8f32e1bcf8b19643de7df2ce6033ccd46168861f2cd1f2d1fedc8a7444ae898dee6c6a7c1377d48c8f0c3b3052a884e35ce7972895b971b63c0bf13a244568b1a79fe3d37a788e8439059e28f2d496ca246f1565',
        'Host': 'ks.feigua.cn',
        'Referer': 'https://ks.feigua.cn/Member',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    return headers

def get_one():
    url = 'https://ks.feigua.cn/LiveRank/LiveGift'
    temp = requests.get(url, headers=get_headers()).text
    eve = etree.HTML(temp).xpath("//td[@class='text-center']/a/@href")
    id_list = []
    for id in eve:
        id_list.append(''.join(id).split('?')[1])
    return id_list

def get_two():
    params_list = get_one()
    blogid_list = []
    userid_list = []
    for params in params_list:
        url = 'https://ks.feigua.cn/Blogger/Detail' + str(params)
        blogid = re.search('\#.*?id=(\d+).*?bloggerlivestat', params, re.S).group(1)
        blogid_list.append(blogid)
        temp = requests.get(url, headers=get_headers()).text
        user_info = {}
        user_info['name'] = ''.join(etree.HTML(temp).xpath("//div[@class='nickname v-tag']/text()")).strip()
        user_info['account'] = ''.join(etree.HTML(temp).xpath("//div[@class='info']/ul/li[1]/span/text()"))
        user_info['location'] = ''.join(etree.HTML(temp).xpath("//div[@class='info']/ul/li[2]/span[1]/text()"))
        user_info['age'] = ''.join(etree.HTML(temp).xpath("//div[@class='info']/ul/li[3]/span[1]/text()"))
        user_info['categoryId'] = ''.join(etree.HTML(temp).xpath("//div[@class='info']/ul/li[3]/span[2]/text()"))
        user_info['signature'] = ''.join(etree.HTML(temp).xpath("//div[@class='intro']/span/text()")).strip()
        user_info['avatar'] = ''.join(etree.HTML(temp).xpath("//div[@class='avatar']/img/@src"))
        userid = ''.join(etree.HTML(temp).xpath("//div[@class='btns-area']/a[2]/@href"))
        user_info['userid'] = re.search('\#.*?userid=(\d+)', userid, re.S).group(1)
        userid_list.append(user_info['userid'])
        print(user_info)
    return blogid_list, userid_list

def get_fans():
    blogid_list = get_two()[0]
    userid_list = get_two()[1]
    for blogid, userid in zip(blogid_list, userid_list):
        data = {
            'id': '%s' % blogid,
            'userId': '%s' % userid,
        }
        url = 'https://ks.feigua.cn/Blogger/GetFansDataAnalysis?bloggerId={}'.format(blogid)
        temp = requests.post(url, headers=get_headers(), data=data).text
        sex_infos = {}
        male = ''.join(etree.HTML(temp).xpath("//div[@class='row gender-text']/div[1]/text()"))
        sex_infos['male_rate'] = re.search('男.*?(.*?)\%', male, re.S).group(1).strip()
        female = ''.join(etree.HTML(temp).xpath("//div[@class='row gender-text']/div[2]/text()"))
        sex_infos['female_rate'] = re.search('女.*?(.*?)\%', female, re.S).group(1).strip()
        province_list = etree.HTML(temp).xpath("//table[@class='location-table js-area-blogger'][1]/tbody/tr")
        for province in province_list:
            province_info = {}
            province_info['province'] = province.xpath("./td[1]")
            province_info['percentage'] = province.xpath("./td[2]")

        city_list = etree.HTML(temp).xpath("//table[@class='location-table js-area-blogger'][2]/tbody/tr")
        for city in city_list:
            city_info = {}
            city_info['city'] = city.xpath("./td[1]")
            city_info['percentage'] = city.xpath("./td[2]")

        age_list = eval('[' + re.search('age_data.*?\[(.*?)\]', temp, re.S).group(1) + ']')
        count_list = []
        for sum_temp in age_list:
            count_list.append(sum_temp['count'])
        count_temp = sum(count_list)

        for age in age_list:
            age_info = {}
            age_info['age'] = age['item']
            age_info['percentage'] = round((age['count'] / count_temp) * 100, 2)
            print(age_info)
        star_temp = etree.HTML(temp).xpath("//div[@class='data-section zodiac-section pt20']/div[2]/ul/li")

        for star in star_temp:
            star_info = {}
            star_info['star'] = ''.join(star.xpath("./div[@class='zodiac-name']/text()"))
            star_info['percentage'] = ''.join(star.xpath("./div[@class='zodiac-percent']/text()")).split('%')[0]
            print(star_info)















