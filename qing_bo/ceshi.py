import requests
import re
from qb_spider import get_headers
from lxml import etree

url = 'http://www.gsdata.cn/rank/wxdetail?wxname=ZQ3BVDhSbJmqNionYgW5N2u1'
html = requests.get(url,headers=get_headers())
req = etree.HTML(html.text)
user_info = ''.join(req.xpath("//p[@class='fs28']/text()")[-3])
# user_info = re.search('<p.*?cr7d.*?(\d+).*?</p>', html.text, re.S).group(1)

# userid = url.split('=')[1]
print(user_info)
