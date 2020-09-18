# coding: utf-8
import time


def get_params1():
    params1 = {
        'app': 'DCMS',
        'dataId': '236',
        'to': '3000',
        'n': '30',
        'fields': 'versionContent,errorMsgs,crocoServerTime',
        'sk0': '89fa29b8baf0fd1056a946fffde4b1c8',
        'resourceId': '479414',
        'useCookieMemberId': 'true',
        'rtnMode': '1',
        'callback': 'jsonp_jsxo3vx3r7rby5p',
    }
    return params1

def get_params2():
    params2 = {
        'beginpage': '1',
        'asyncreq': '6',
        'keywords': '羊绒大衣',
        'sortType': '',
        'descendOrder': '',
        'province': '',
        'city': '',
        'priceStart': '',
        'priceEnd': '',
        'dis': '',
        'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL',
        'cosite': 'baidujj_pz',
        'trackid': '{trackid}',
        'location': 're',
        'pageid': '17145fa7ralgjD',
        'p4pid': 'f5abf68bdcb94f5dab3c43c91ea6af09',
        'callback': 'jsonp_{}_65125'.format(int(round(time.time() * 1000))),
        '_': '%s' % int(round(time.time() * 1000)),
    }
    return params2

def get_params3(videoId, memberId):
    params3 = {
        'callback': 'jQuery17205396996955221749_{}'.format(int(round(time.time() * 1000))),
        'site_id': 'winport',
        'videoId': '%s' % videoId,
        'memberId': '%s' % memberId,
        '_csrf_token': '5ef5949a0e2024051a6861515696eccf',
    }
    return params3

def get_params4(userid):
    params4 = {
        'callback': 'jQuery17208545160506528315_{}'.format(int(round(time.time() * 1000))),
        'blocks': '',
        'data': 'offerdetail_ditto_title,offerdetail_common_report,offerdetail_ditto_serviceDesc,offerdetail_ditto_preferential,offerdetail_ditto_postage,offerdetail_ditto_offerSatisfaction,offerdetail_w1190_guarantee,offerdetail_w1190_tradeWay,offerdetail_ditto_whosaleself',
        'offerId': '%s' % userid,
        'pageId': 'laputa20140721212446',
        'sk': 'consign',
    }
    return params4


