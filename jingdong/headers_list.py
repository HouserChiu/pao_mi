# coding: utf-8

def get_headers1():
    headers1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_84dc7fd0fa14482e9b7b38c8c8c314b4',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    return headers1

def get_headers2():
    headers2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'unpl=V2_ZzNtbUtSFkdzXxNVLElcAGIKEQlKBEVGdwEUXSkQDgdnBkFYclRCFnQUR1JnGl4UZwoZXUJcRx1FCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfXgNjBxVURFBzJXI4dmR9HF0AZAAiXHJWc1chVEZSfRFfBCoDFF9EU0cSfA5BZHopXw%3d%3d; __jdu=1737556876; areaId=22; ipLoc-djd=22-1930-50945-0; PCSYCityID=CN_510000_510100_510104; shshshfpa=679a9329-099e-b524-9996-d0e2be9389fd-1595499120; shshshfpb=rHn5lHQJCASKw8xEHxyWjcg%3D%3D; user-key=5d3ea9d8-4ba0-4289-a54a-fb10f248df8a; cn=0; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_84dc7fd0fa14482e9b7b38c8c8c314b4|1595569341269; __jdc=122270672; shshshfp=c26f856b31c778eed712cd8fc03e3ae9; 3AB9D23F7A4B3C9B=JNMFZYOIONQHRY5TT75YI35IIJSBSPC7BGJ23HNASC7E6SS6A75ZLHGR4SQIBF64ZIBTDPM3E3GWXZ25Z2BMTEXMJY; __jda=122270672.1737556876.1595499118.1595569341.1595572667.3; rkv=V0300; __jdb=122270672.5.1737556876|3.1595572667; shshshsID=abc2fc612d5d4ee04ad84cda07729358_3_1595572825573; qrsc=2',
        'referer': 'https://search.jd.com/Search?keyword=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8&enc=utf-8&wq=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8&pvid=9141df83103440d28977c66261232a95',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    return headers2

# 需要修改refer
def get_headers3():
    headers3 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'unpl=V2_ZzNtbUtSFkdzXxNVLElcAGIKEQlKBEVGdwEUXSkQDgdnBkFYclRCFnQUR1JnGl4UZwoZXUJcRx1FCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfXgNjBxVURFBzJXI4dmR9HF0AZAAiXHJWc1chVEZSfRFfBCoDFF9EU0cSfA5BZHopXw%3d%3d; __jdu=1737556876; areaId=22; ipLoc-djd=22-1930-50945-0; PCSYCityID=CN_510000_510100_510104; shshshfpa=679a9329-099e-b524-9996-d0e2be9389fd-1595499120; shshshfpb=rHn5lHQJCASKw8xEHxyWjcg%3D%3D; user-key=5d3ea9d8-4ba0-4289-a54a-fb10f248df8a; cn=0; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_84dc7fd0fa14482e9b7b38c8c8c314b4|1595569341269; __jdc=122270672; shshshfp=c26f856b31c778eed712cd8fc03e3ae9; 3AB9D23F7A4B3C9B=JNMFZYOIONQHRY5TT75YI35IIJSBSPC7BGJ23HNASC7E6SS6A75ZLHGR4SQIBF64ZIBTDPM3E3GWXZ25Z2BMTEXMJY; __jda=122270672.1737556876.1595499118.1595569341.1595572667.3; shshshsID=abc2fc612d5d4ee04ad84cda07729358_4_1595573100752; __jdb=122270672.6.1737556876|3.1595572667',
        'if-modified-since': 'Fri, 24 Jul 2020 06:44:50 GMT',
        'referer': 'https://search.jd.com/Search?keyword=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8&enc=utf-8&wq=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8&pvid=9141df83103440d28977c66261232a95',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    return headers3

# 需要修改refer
def get_headers4(url):
    headers4 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'c.3.cn',
        'Referer': '%s' % url,
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    return headers4