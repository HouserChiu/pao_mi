import re
import requests
from web_spider import get_headers
from lxml import etree

def get_fans():

    url = 'https://ks.feigua.cn/Blogger/GetFansDataAnalysis?bloggerId=980398'
    data = {
        'id': '980398',
        'userId': '213801412',
    }
    temp = requests.post(url,headers=get_headers(),data=data).text
    male = ''.join(etree.HTML(temp).xpath("//div[@class='row gender-text']/div[1]/text()"))
    male_rate = re.search('男.*?(.*?)\%', male ,re.S).group(1).strip()
    female = ''.join(etree.HTML(temp).xpath("//div[@class='row gender-text']/div[2]/text()"))
    female_rate = re.search('女.*?(.*?)\%', female ,re.S).group(1).strip()

    print(male_rate)
    # print(male)
    print(female_rate)
    # print(female)
    province_list = etree.HTML(temp).xpath("//table[@class='location-table js-area-blogger'][1]/tbody/tr")
    for province in province_list:
        province_info = {}
        province_info['province'] = ''.join(province.xpath("./td[1]/text()"))
        province_info['percentage'] = ''.join(province.xpath("./td[2]/text()")).split('%')[0]
        print(province_info)

    city_list = etree.HTML(temp).xpath("//table[@class='location-table js-area-blogger'][2]/tbody/tr")
    for city in city_list:
        city_info = {}
        city_info['city'] = ''.join(city.xpath("./td[1]/text()"))
        city_info['percentage'] = ''.join(city.xpath("./td[2]/text()")).split('%')[0]
        print(city_info)

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

# get_fans()

