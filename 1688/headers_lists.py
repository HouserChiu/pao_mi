# coding: utf-8

import urllib.parse


def get_headers1():
    headers1 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'cna=+X2EF7EN4DUCAd7RUm0VEDFE; cookie2=1c2d2d506f3974eaca20f2d0da306840; t=fd877f4115abf99852e1fc9d3e551295; _tb_token_=f3447f61eb1b6; __cn_logon__=false; alicnweb=touch_tb_at%3D1593675771270; UM_distinctid=1730e7a849038a-0cffe56c210ecb-4353760-1fa400-1730e7a84917da; CNZZDATA1253659577=2013546509-1593675146-https%253A%252F%252Fp4psearch.1688.com%252F%7C1593675146; _csrf_token=1593675779111; taklid=46d4f762882b4670975e63ba2f5f778a; JSESSIONID=57E9EDE3EEE9F2FCB97DF658AF3096BB; l=eBIiAvjuQqc0fkAtBOfwourza77OjIRfguPzaNbMiOCP_8BwS6YFWZYQA1teCnGVH6PpR3ow4YKMBh0vqyE4VGRGNe8yZVHmndC..; isg=BOzsIXrjnkLSPYp-hc2oe5jevcoepZBPxYWn20Yt9xczUY1bbrV03y9jdRlpWcin',
        'referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?spm=a2609.11209760.it2i6j8a.30.44292de1IGPyHp&cosite=baidujj_pz&keywords=%E7%BE%8A%E7%BB%92%E5%A4%A7%E8%A1%A3&trackid={trackid}&location=re',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers1

def get_headers2(cate):
    headers2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_ga=GA1.2.1141036788.1596186445; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb2718229_2012; cna=npS6Fx4H3U4CAd7RUmzdRIFa; cookie2=185549a16ca867f3123bc8f6abe7aa86; t=ef0629f892a693754b68907fd86e88dd; _tb_token_=7d1e3305ee4b4; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1599442468959; UM_distinctid=1746633a586b81-022f4cc0a6f7ae-f7b1332-1fa400-1746633a587a37; _csrf_token=1599442500679; taklid=b8b3c2bc04cf4d0d9a0b992b39184f08; isg=BFtbbhxdgLfLafyi6ag9_oQK6r_FMG8ytMw9J02YFNp1LHsO1QHYgrMtxoyiDMcq; l=eB_e_HkVO_T7OZdOBOfZlurza779AIRAguPzaNbMiOCPOJCB5k0FWZyWZtL6CnGVhspeR3SxXm94BeYBq7F-nxvTkgnijfHmn; tfstk=cWqNBgYKSGINjkmfyci2crGM4seOaz2gnHkSSr0IRPYAzBhrasVpMvXBMvkXb63G.; JSESSIONID=360E3484B9B142393F8156AA4A9A6994',
        'referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?spm=a2609.11209760.it2i6j8a.30.67b62de1YU0Kt1&cosite=&keywords=%s&trackid=&location=' % urllib.parse.quote(cate),
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers2

def get_headers3():
    headers3 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.1141036788.1596186445; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb2718229_2012; cna=npS6Fx4H3U4CAd7RUmzdRIFa; cookie2=185549a16ca867f3123bc8f6abe7aa86; t=ef0629f892a693754b68907fd86e88dd; _tb_token_=7d1e3305ee4b4; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1599442468959; UM_distinctid=1746633a586b81-022f4cc0a6f7ae-f7b1332-1fa400-1746633a587a37; CNZZDATA1253659577=94334282-1599441302-https%253A%252F%252Fp4psearch.1688.com%252F%7C1599441302; _csrf_token=1599442500679; taklid=b8b3c2bc04cf4d0d9a0b992b39184f08; JSESSIONID=0CFE860AB927B8DDBF2606D840D42612; tfstk=chs1BVqoGfcsR4UqbOweg-AKV18cZFkWhPOGCNNzPfQYGd61iuiyNpkGojHFnp1..; l=eB_e_HkVO_T7OPCbBOfwourza77O7IRAguPzaNbMiOCPOpXekntGWZyWIBxwCnGVhs1XR3SxXm92BeYBqmqJ6lRRACeLozkmn; isg=BLe3TOjspNvbwiA2LfTZwji-RqsBfIveuNgBkwlkwwb1uNf6EU5bL7hanhjmUGNW',
        'referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?spm=a2609.11209760.it2i6j8a.30.67b62de1YU0Kt1&cosite=&keywords=%E7%BE%8A%E7%BB%92%E5%A4%A7%E8%A1%A3&trackid=&location=',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers3

def get_headers4():
    headers4 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_ga=GA1.2.1141036788.1596186445; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb2718229_2012; cna=npS6Fx4H3U4CAd7RUmzdRIFa; cookie2=185549a16ca867f3123bc8f6abe7aa86; t=ef0629f892a693754b68907fd86e88dd; _tb_token_=7d1e3305ee4b4; __cn_logon__=false; xlly_s=1; UM_distinctid=1746633a586b81-022f4cc0a6f7ae-f7b1332-1fa400-1746633a587a37; _csrf_token=1599442500679; taklid=b8b3c2bc04cf4d0d9a0b992b39184f08; alicnweb=touch_tb_at%3D1599445238666; tfstk=ckolBi9Oe4z5Fozm53ZSCfEJBOnlZ6jUsDoj0mDjcYQILxmVi_7V7U6Jn7075w1..; l=eB_e_HkVO_T7OsrABOfwourza77OSIRAguPzaNbMiOCP9Ufw5zrlWZyW1nTeC3GVh65yR3SxXm94BeYBqoj-eNYPUOZ1T6kmn; isg=BDIyYRYiuRgEW4VF-BuUoeWpg3gUwzZdtU8kQPwLXuXRj9KJ5FOGbThpeysz_671',
        'referer': 'https://detail.1688.com/offer/624283430841.html?spm=a312h.2018_new_sem.dh_002.3.354b5fa7RFIJN4&tracelog=p4p&clickid=eaf6163029bb45dea7718fe78a77e06a&sessionid=3b5a0b33b223f7e9136eb233bca3a698',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers4

def get_headers5():
    headers5 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://detail.1688.com/offer/588015758191.html?spm=a312h.2018_new_sem.dh_002.1.54465fa7IliKHa&tracelog=p4p&clickid=679c5ada0b164e13afec3e4208974b62&sessionid=46a39b945a6c7ae2ef89f5167ef13745',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers5

def get_headers6():
    headers6 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'cna=ooyEF+L8uiYCAd7RUm4Cx5kZ; UM_distinctid=1730eb5ef1987d-0b9f5e9c01400b-4353760-1fa400-1730eb5ef1a780; taklid=d01552286eda45fe9e091de36d2483c8; cookie2=106034585b298a1c1937b0870d87f997; t=c0daa371795cd5609673c84812c21556; _tb_token_=ee5145395149e; __cn_logon__=false; _csrf_token=1594086450080; alicnweb=touch_tb_at%3D1594115824515; JSESSIONID=4BBC3D6D18640EFCD64F20A6F309C430; isg=BK2tZSWhjgiSQGsdwcO4he5gvEknCuHcPPJGeO-yGsRVZswYt1xUrC33VDqAZvmU; l=eBM6riuRQqUBgj-xBO5Cnurza779WIRb8sPzaNbMiInca6dRELxb9NQqwWiDmdtjgtfv1etrb3kJjdewkqULRPkDBeYCCgrrF299-',
        'referer': 'https://re.1688.com/?keywords={keywords}&cosite=baidujj_pz&location=re&trackid={trackid}&keywordid={keywordid}&format=normal',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers6

def get_headers7(userid):
    headers7 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.1141036788.1596186445; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb2718229_2012; cna=npS6Fx4H3U4CAd7RUmzdRIFa; cookie2=185549a16ca867f3123bc8f6abe7aa86; t=ef0629f892a693754b68907fd86e88dd; _tb_token_=7d1e3305ee4b4; __cn_logon__=false; xlly_s=1; UM_distinctid=1746633a586b81-022f4cc0a6f7ae-f7b1332-1fa400-1746633a587a37; CNZZDATA1253659577=94334282-1599441302-https%253A%252F%252Fp4psearch.1688.com%252F%7C1599441302; _csrf_token=1599442500679; taklid=b8b3c2bc04cf4d0d9a0b992b39184f08; alicnweb=touch_tb_at%3D1599445238666; JSESSIONID=9DD6834ED8AB692681850837C1414AF8; cbu_mmid=7E3C55520E991B9B6A5D97E08A6697F623F137761C179394FB6FDFDFD583D82F09F848C1F03189F29DE43978D3109381F058A703ED6C61E7054575550BFB2234; ta_info=69D091960A00D3F2363D55CAD75990D7AF2651492692FC72F8FCD304CF11CF6EB039D1B914DC75A32392DE49999E6CF514A5CAB8BECF8977693063708C5CEB9027D454A48C91B48C4A564C51A6AD590042C2F8C1A44CADB9BB1DEE3769A06B570E536F2EE8C776DF3DEAD8D884435ADA4597474615EEC31F8A0CFB78BA1469E57C83E744E0A5247832396943E06CF9561E03F9C838A9A737C453DA121C4362122112DEFE0E5199234A43BEB0022D97CD; l=eB_e_HkVO_T7ORXyBOfanurza77OSIRYYuPzaNbMiOCPO3CB5P_OWZyWsaL6C3GVhsaHR3SxXm92BeYBq7NSnxvTkgnijcDmn; tfstk=cALPB3qAq43rrEbIXa_URHsCzHARwHdktr51qHjXDrhe0_fDBJCmGJCVOzkAq; isg=BPj4Fwl70w7wjj_rNjnu13NryaaKYVzrY00-rjJpRDPmTZg32nEsew79AwXYBhTD',
        'Host': 'detail.1688.com',
        'Referer': 'https://detail.1688.com/offer/{}.html?tracelog=p4p&clickid=86bdc9eabe464e03acc2ef047afb28a5&sessionid=191c66c530e0ba32e5d994ae532577e4'.format(userid),
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers7

def get_headers8():
    headers8 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'cna=ooyEF+L8uiYCAd7RUm4Cx5kZ; UM_distinctid=1730eb5ef1987d-0b9f5e9c01400b-4353760-1fa400-1730eb5ef1a780; taklid=d01552286eda45fe9e091de36d2483c8; cookie2=106034585b298a1c1937b0870d87f997; t=c0daa371795cd5609673c84812c21556; _tb_token_=ee5145395149e; __cn_logon__=false; CNZZDATA1261052687=465297774-1593767879-%7C1594025092; _csrf_token=1594175720310; alicnweb=touch_tb_at%3D1594193390137%7ChomeIdttS%3D59265532384332960222041967254734501341%7ChomeIdttSAction%3Dtrue; CNZZDATA1253659577=1729731420-1593675146-%7C1594193575; JSESSIONID=634D5D95F3DE05BA465133FDE6805789; l=eBM6riuRQqUBgKzfBOfwFurza77OKIRVguPzaNbMiOCP9C695zHFWZl7ugxpCnGVnsXvJ3ow4YKgBJLTQy4UlM88ZrEghhsUbdTh.; isg=BF5e_bGBjYyTediQpvYb4AHtr_SgHyKZ4y_VtQjnhKGcK_wFca3RqLgJJzcnExqx',
        'Host': 'detail.1688.com',
        'Referer': 'https://detail.1688.com/offer/557131854707.html?tracelog=p4p&clickid=86bdc9eabe464e03acc2ef047afb28a5&sessionid=191c66c530e0ba32e5d994ae532577e4',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers8

def get_headers9(userid):
    headers9 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.1141036788.1596186445; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb2718229_2012; cna=npS6Fx4H3U4CAd7RUmzdRIFa; cookie2=185549a16ca867f3123bc8f6abe7aa86; t=ef0629f892a693754b68907fd86e88dd; _tb_token_=7d1e3305ee4b4; __cn_logon__=false; xlly_s=1; UM_distinctid=1746633a586b81-022f4cc0a6f7ae-f7b1332-1fa400-1746633a587a37; _csrf_token=1599442500679; taklid=b8b3c2bc04cf4d0d9a0b992b39184f08; alicnweb=touch_tb_at%3D1599445238666; JSESSIONID=9BAF353534C1D55EB5FE59DF12251ECA; cbu_mmid=7E3C55520E991B9B6A5D97E08A6697F623F137761C179394FB6FDFDFD583D82F09F848C1F03189F29DE43978D3109381F058A703ED6C61E7054575550BFB2234; ta_info=69D091960A00D3F2363D55CAD75990D7AF2651492692FC72F8FCD304CF11CF6EB039D1B914DC75A32392DE49999E6CF514A5CAB8BECF8977693063708C5CEB9027D454A48C91B48C4A564C51A6AD590042C2F8C1A44CADB9BB1DEE3769A06B570E536F2EE8C776DF3DEAD8D884435ADA4597474615EEC31F8A0CFB78BA1469E57C83E744E0A5247832396943E06CF9561E03F9C838A9A737C453DA121C4362122112DEFE0E5199234A43BEB0022D97CD; tfstk=cIZVB7T-oiIVtSn1JmiwfPg1nWoAwUw0I3kIoP07yMlbQxf0eCHlFCHrCn5-o; l=eB_e_HkVO_T7OSJAKOfanurza77OSIRYYuPzaNbMiOCPOgCB5OmVWZyWsC86C3GVh652R3SxXm92BeYBq7VonxvOUOZ1T6kmn; isg=BBUVQU6C5gGdMcKc0wpbSK7IJBHPEskkTk6juZe60Qzb7jXgX2LZ9CMovPLYbuHc',
        'Host': 'laputa.1688.com',
        'Referer': 'https://detail.1688.com/offer/{}.html?spm=a312h.2018_new_sem.dh_002.1.31e51ebeWdk1G1&tracelog=p4p&clickid=0046504d53d04c3c98b0d7976606a6f6&sessionid=b0257cc2dacee29e7bfaf1a073636d76'.format(userid),
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }
    return headers9

def get_headers10():
    headers10 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cna=8FmVF+VBJxgCAd7RUm5VHyu7; cookie2=11baad53f0e72b068205987923f6a275; t=2860081a67b697359e9c35a3d908fa6f; _tb_token_=ee8d7fe63eee3; __cn_logon__=false; UM_distinctid=173554c31e71ad-02843fe713af65-b7a1334-1fa400-173554c31e81fa; taklid=32db1f161ce34650a48000ae5bc0e578; _csrf_token=1594863925709; alicnweb=touch_tb_at%3D1594894388026; x5sec=7b226c61707574613b32223a223232393836653036336664323339653436336232323334356564326335613938434f72587750674645504c452f3744412b38754e48513d3d227d; CNZZDATA1253659577=289555298-1594862669-https%253A%252F%252Fp4psearch.1688.com%252F%7C1594892306; JSESSIONID=A6329CCA93315ED4A0F015FF25D5A4CB; l=eBOTngjROLe3xVxQBOfwourza77OSIRAguPzaNbMiOCPOE6p5exOWZkxDIx9C3GVhs_HR3oIr-vXBeYBqo0fb0I2yT6ngjkmn; isg=BB4esVcwzVmUXRkiSTDoSIhBb7Rg3-JZJLnWg8inimFc677FMG8yaUQJ5_dnU9px',
        'Host': 'detail.1688.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    return headers10

def get_headers11():
    headers11 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cna=8FmVF+VBJxgCAd7RUm5VHyu7; cookie2=11baad53f0e72b068205987923f6a275; t=2860081a67b697359e9c35a3d908fa6f; _tb_token_=ee8d7fe63eee3; __cn_logon__=false; UM_distinctid=173554c31e71ad-02843fe713af65-b7a1334-1fa400-173554c31e81fa; taklid=32db1f161ce34650a48000ae5bc0e578; _csrf_token=1594863925709; CNZZDATA1253659577=289555298-1594862669-https%253A%252F%252Fp4psearch.1688.com%252F%7C1594892306; JSESSIONID=9637693D3CF542C4BEE9B0902A7BEA6E; l=eBOTngjROLe3xU0LBOfwourza77OjIRAguPzaNbMiOCPOBX65ZRfWZkxmnKBCnGVhsCJR3oIr-vXBeYBql01b0I4PxMDzUkmn; isg=BK2tb3bLjhzog2rv7kUL7ScMvEknCuHcOyQFDu-y5sSzZs0Yt1k6rPK8VDqAZvmU; alicnweb=touch_tb_at%3D1594897263268',
        'Host': 'detail.1688.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    return headers11



