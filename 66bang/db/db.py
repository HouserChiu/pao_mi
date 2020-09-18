#todo:
# coding=utf-8
# Author: tester_pei

import pymysql
import conf



def get_data_by_sql(sql):
    '''
    查询方法
    :param sql: 完整的sql语句
    :return:
    '''
    conn = pymysql.connect(**conf.mysql_config)
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_first_data(sql):
    '''
    获取查询到的数据第一份数据
    :param sql:
    :return:
    '''
    return get_data_by_sql(sql)[0][0]


def update_sql(sql):
    '''
    修改语句
    :param sql: 完整的sql语句
    :return:
    '''
    conn = pymysql.connect(**conf.mysql_config)
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
            result = cur.fetchone()
            print('操作成功')
            return result
    except EOFError:
        print('修改失败，已回滚')
        print(EOFError)
        conn.rollback()
    finally:
        conn.close()


# sql_004 = f"select t.url from `test`.`t_from_user_info` t where url = 'aa'"
# url = get_data_by_sql(sql_004)
#
# print(url == ())