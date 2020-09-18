# coding: utf-8

def get_params1(cate, page):
    params1 = {
        'cityId': '028',
        'keyword': '%s' % cate,
        'channel': '',
        'cp': '%s' % page,
        'ps': '10',
        'st': '0',
        'set': '5',
        'cf': '',
        'iv': '-1',
        'ci': '',
        'ct': '-1',
        'channelId': 'WAP',
        'sp': '',
        'sg': '',
        'sc': '',
        'prune': '',
        'operate': '0',
        'isAnalysised': '0',
        'istongma': '1',
        'jlfstoreCode': 'null',
        'jlfOnly': '0',
        'jlftownCode': 'null',
        'saleMode': 'null',
        'v': '99999999',
        'sesab': 'ABB0A',
        'jzq': '1274',
        'callback': 'success_jsonpCallback',
    }
    return params1

def get_params2():
    params2 = {
        'safp': 'f73ee1cf.20071.resultWrap.159',
        'safc': 'prd.3.wapssjgy_sph_sp18-p_jz',
        'safpn': '10007',
    }
    return params2
