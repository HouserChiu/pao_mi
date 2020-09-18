# -*- coding: utf-8 -*-
# 返回54001是因为需要验证码,anti_content写死也可以
import requests
import pprint
import execjs
from antiContent_Js import js


def get_anticontent(q):
    ctx = execjs.compile(js)
    anti_content = ctx.call('result', q)
    print(anti_content)
    return anti_content

def get_one_page():
    url1 = "http://yangkeduo.com/proxy/api/api/search/opt/9520/groups"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'AccessToken': '2QEK2N6UXPQFUROV37HSFNSG6EUBKOGPV2DPEDETUDY6SLYXOQBQ113a4ac',
        'Connection': 'keep-alive',
        'Cookie': 'api_uid=rBUUTF8fx1FQQQ5qGs4cAg==; _nano_fp=XpdbnpUal0PYn0TJl9_zRD2kexHE0hN_Qi3Ezgbx; ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F84.0.4147.89%20Safari%2F537.36; webp=1; chat_list_rec_list=chat_list_rec_list_xQCgOs; msec=1800000; vds=gaLcNumumLIbieLuLLaLPftlIwOlosQTyBiuiBENPensIsLfnTPTyfEDbdIT; PDDAccessToken=2QEK2N6UXPQFUROV37HSFNSG6EUBKOGPV2DPEDETUDY6SLYXOQBQ113a4ac; pdd_user_id=4276569950116; pdd_user_uin=BFZOUCNHKVD4HOJEXWWU6UI6LU_GEXDA; JSESSIONID=EA04B50A624320EE9EB69A618E933D49',
        'Host': 'yangkeduo.com',
        'Referer': 'http://yangkeduo.com/search_catgoods.html?opt_id=9520&opt1_id=999998&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E6%97%B6%E5%B0%9A%E5%A5%97%E8%A3%85&_x_link_id=c18ff8cb-02a3-470b-adfe-7db68d851160&_x_goods_id=137119754297&refer_page_name=login&refer_page_id=10169_1596012424863_hg5qxeg4uw&refer_page_sn=10169',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'VerifyAuthToken': 'xyM0aGqnquiR1LQMhcgLiQ0a651136c178498bc',
    }
    params = {
        'pdduid': '4276569950116',
        'source': 'search',
        'opt_type': '3',
        'white_ground_pic_goods_id': '137119754297',
        'flip': '',
        'offset': '0',
        'count': '20',
        'list_id': 'NCKgehXhxO',
        'sort': 'default',
        'filter': '',
        # 'anti_content': '%s' % get_anticontent(headers['Referer']),
        'anti_content': '0aoAfxndIyhYY9mpplaP2ZeY4jlgSMENRy2edg4k_nt1oE_OdqzjpbRtPLQuEaoXjvULX5PWoKaTPZaONaLpiRNQMp7QiMyiFDilH-kKMIOAWA3pnm-R-IuxB3rIusyF9zwDFfIJ3jDnehZ5kjkPPNNap9m6093UcLP5cfRv6dY_6yYhfhLxh5U4gcNXDJqJJJ_qKTLXieXSkX-6eZopKafeYPmxTe2BawbcAbtwUC-ZEq4Xm_k5t-9Jv56Zw-GllTxFCoV05hRmu9cCPV9_9FBHwt0jZ_-0Z1u-5Ru4bh-bWN1Li8ijmlpidO4leA__SgVgwqZXzttTJTvVStP3R8qzJ4CFgwIkgPBpwPGw2fKEBpUEzznPunF7OLyjRI_LhtZY2bqPw5AbBvHhj82yWtTuigKl9ZmMStzYaBEvsvVDUaJUpmAPrPF69ohbHhG53N9Ukrnl0WwjSL9c3xjBinf3Ut7PZKm1m2MMAC3Rbhk0jiIl4xIF_LCNem_G5rdtOVNASR7KK8QE6EvG6Pxj3vViR8wqSWwS8RB53md4r3JdCoAMcQMZ813zZ8QentZHrvZoALlOq_kKGLRBN_ropT',
        'opt_source': 'search_opt_goods',
    }

    res = requests.get(url1, headers=headers, params=params).text
    pprint.pprint(res)

if __name__ == '__main__':
    get_one_page()