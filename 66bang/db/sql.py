# todo:
# coding=utf-8
# Author: tester_pei


from db.db import get_first_data, update_sql, get_data_by_sql


def sql_001(name):
    '''
    # 通过昵称查询id
    :param name:标签
    :return:
    '''
    name = str(name)
    sql_001 = f'SELECT id FROM t_from_category WHERE NAME like "%{name}%"'
    category_id = get_first_data(sql_001)
    return category_id


def sql_002(dict):
    sql_002 = f'''
    INSERT INTO `test`.`t_from_user_info`(
    platform,account,name,head_thumb,sex,stars,age,district,remark,mcn,label,fans,collection,likes,url,categoryid
    )
    VALUE (
    {dict['platform']},{dict['account']},{dict['name']},{dict['head_thumb']},{dict['sex']},{dict['stars']},{dict['age']},{dict['district']},
    {dict['remark']},{dict['mcn']},{dict['label']},{dict['fans']},{dict['collection']},{dict['likes']},{dict['url']},{dict['categoryid']}
    )'''
    update_sql(sql_002)
    return 'ok'


def sql_003(dict):
    sql_003 = f'''
    INSERT INTO `test`.`t_from_user_info`(
    platform,account,name,head_thumb,sex,stars,age,district,remark,mcn,label,fans,collection,likes,url,categoryid
    )
    VALUE (
    {dict['platform']},{dict['account']},{dict['name']},{dict['head_thumb']},{dict['sex']},{dict['stars']},{dict['age']},{dict['district']},
    {dict['remark']},{dict['mcn']},{dict['label']},{dict['fans']},{dict['collection']},{dict['likes']},{dict['url']},{dict['categoryid']}
    )'''
    print(sql_003)
    update_sql(sql_003)
    return 'ok'


def sql_004(url):
    sql_004 = f"select t.url from `test`.`t_from_user_info` t where url = '{url}'"
    if get_data_by_sql(sql_004) == ():
        url = ''
        return url
    else:
        url = get_first_data(sql_004)
    return url


def sql_005(dict):
    sql_005 = f'''
    UPDATE  `test`.`t_from_user_info` SET
    platform = '{dict['platform']}',
    account = '{dict['account']}',
    name = '{dict['name']}',
    head_thumb = '{dict['head_thumb']}',
    sex = '{dict['sex']}',
    stars = '{dict['stars']}',
    age = '{dict['age']}',
    district = '{dict['district']}',
    remark = '{dict['remark']}',
    mcn = '{dict['mcn']}',
    label = '{dict['label']}',
    fans = '{dict['fans']}',
    collection = '{dict['collection']}',
    likes = '{dict['likes']}',
    url = '{dict['url']}',
    categoryid = '{dict['categoryid']}'
    WHERE
    url = '{dict['url']}'
    '''
    print(sql_005)
    update_sql(sql_005)
    return 'ok'


print(sql_004('aa'))
