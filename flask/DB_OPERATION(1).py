# -*- coding: utf-8 -*-
"""
数据库功能:
建包  create_database
条件建库  table_create  table_set
删除数据库  del_table
复制
新增   table_in
修改  replace_status(单字段  单行)   replace_all(多字段 单行)
删除  del_data_one(单条)   del_data_all(多条)
条件查询  fuzzy_query(单条件)  fuzzy_query_all(多条件)  db_select_data_one(通过id取单条数据)

"""
import pymysql
import time
import threading
import configparser
import re
from datetime import datetime
from datetime import datetime,timedelta,date
class DB_config():
    #初始化参数
    def __init__(self,*args):
        self.DB_IP       =  args[0]["DB_IP"]
        self.DB_PORT     =  args[0]["DB_PORT"]
        self.DB_USER     =  args[0]["DB_USER"]
        self.DB_PASSWORD =  args[0]["DB_PASSWORD"]
        self.DB_NAME     =  args[0]["DB_NAME"]
        self.DB_CODE     =  args[0]["DB_CODE"]

    # 建立数据库连接
    def connet_table(self):
        self.db = pymysql.connect(host=self.DB_IP,
                                  port=self.DB_PORT,
                                  user=self.DB_USER,
                                  password=self.DB_PASSWORD,
                                  db=self.DB_NAME,
                                  charset=self.DB_CODE)
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")

    """
        function1：
        新建数据库 
        所需参数self.DB_NAME : DB_NAME(数据库名称)
    """
    def create_database(self, database_name):
        db = pymysql.connect(host=self.DB_IP,
                             port=self.DB_PORT,
                             user=self.DB_USER,
                             password=self.DB_PASSWORD,
                             charset=self.DB_CODE)
        cursor = db.cursor()
        cursor.execute("show databases")
        rows = cursor.fetchall()
        tmp = []
        for row in rows:
            tmp.append(row[0])
        # 判断数据库是否存在
        try:
            if database_name in tmp:
                print("此数据库已存在")
            else:
                cursor.execute('create database if not exists ' + database_name)
                db.commit()
        except:
            db.rollback()
            print("拿不到数据")
        # 关闭数据库连接
        cursor.close()  # 关闭游标 释放资源
        db.close()

    """
       function2：
       创建表
       所需参数表名： fields_dict、DB_NAME    传入参数 1、需要创建的字段长度number1 2、库表名 table_name
   """
    def table_create(self, table_name, table_number,fields_dict):
        if fields_dict != "":
            fields_dict = fields_dict
        else:
            fields_dict = {"1": "`ID` varchar(128) NOT NULL",
                           "2": "`X_ID` datetime DEFAULT CURRENT_TIMESTAMP",
                           "3": "`SOURCE` varchar(128) NOT NULL",
                           "4": "`KEYWORD` varchar(640) NOT NULL",
                           "5": "`WEB_DATE` varchar(1128) NOT NULL",
                           "6": "`WEB_TIME` datetime DEFAULT CURRENT_TIMESTAMP",
                           "7": "`TITLE` varchar(128) NOT NULL",
                           "8": "`AUTHOR` varchar(128) NOT NULL",
                           "9": "`CONTENT` varchar(10800) NOT NULL",
                           "10": "`URL` varchar(1640) NOT NULL",
                           "11": "`INS` varchar(128) NOT NULL",
                           "12": "`WEB_READ` datetime DEFAULT CURRENT_TIMESTAMP",
                           "13": "`AUTADR` varchar(128) NOT NULL",
                           "14": "`VIEW_NUMBER` varchar(128) NOT NULL",
                           "15": "`TRAN_NUMBER` varchar(128) NOT NULL",
                           "16": "`ANS_NUMBER` varchar(128) NOT NULL",
                           "17": "`WEBADR` varchar(128) NOT NULL",
                           "18": "`WEBCLS` varchar(128) NOT NULL",
                           "19": "`CONTCLS` varchar(128) NOT NULL",
                           "99": "PRIMARY KEY (`ID`)"}

        flelds_number = int(table_number)
        self.flelds_list = []
        for i in range(flelds_number):
            self.flelds_list.append(fields_dict[str(i + 1)])
        flelds = ''
        for j in self.flelds_list:
            flelds = flelds + str(j) + ","
        flelds = str(flelds + str(fields_dict["99"])).strip('[]')
        table_name = str(table_name)
        self.__name = '''
                  CREATE TABLE `%s` (%s) ENGINE=InnoDB DEFAULT CHARSET= "utf8mb4"''' % (table_name, str(flelds))
        print(self.__name)
        self.cursor.execute(self.__name)
        self.db.commit()
        # 关闭数据库连接
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()

    """
       function3：
       设置主键自增
       所需参数 DB_NAME    传入参数 1、需要创建的字段长度number1 2、库表名 table_name
   """
    def table_set(self, table_name):
        table_name = table_name
        self.cursor.execute('''alter table `%s` modify ID int auto_increment,auto_increment = 0''' % (table_name))
        self.db.commit()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()

    """
       function4：
       删除数据库
       所需参数 DB_NAME    传入参数 1、库表名 table_name
   """
    def del_table(self,database_name):
        db = pymysql.connect(host=self.DB_IP,
                             port=self.DB_PORT,
                             user=self.DB_USER,
                             password=self.DB_PASSWORD,
                             charset=self.DB_CODE)
        cursor = db.cursor()
        cursor.execute("show databases")
        rows = cursor.fetchall()
        tmp = []
        for row in rows:
            tmp.append(row[0])
        # 判断数据库是否存在
        try:
            if database_name in tmp:
                cursor.execute('drop database  ' + database_name)
                db.commit()
            else:
                print("此数据库不存在")
        except:
            db.rollback()
            print("删除数据库出错")
        # 关闭数据库连接
        cursor.close()  # 关闭游标 释放资源
        db.close()

    """
        function5：
        获取库表最大数据
        所需参数 DB_NAME    传入参数 1、库表名 table_name
    """
    def db_max(self, table_name):
        __t_name = table_name
        self.cursor_IDMAX = self.db.cursor(pymysql.cursors.DictCursor)
        self.sql_IDMAX = 'select count(id) from `%s`' % (__t_name)
        rows_IDMAX = self.cursor_IDMAX.execute(self.sql_IDMAX)
        CONTENT_OUT = self.cursor_IDMAX.fetchone()
        IDMAX = CONTENT_OUT['count(id)']
        print("我是读取最大" + str(IDMAX))
        self.OUT_MAX = IDMAX
        self.cursor_IDMAX.close()
        return self.OUT_MAX

    def check_fields(self,table_name):
        # self.cursor.execute("select * from `%s`" % table_name)
        # # 获取字段的数组  顺序排列 table_name_arr ['ID', 'X_ID', 'SOURCE', 'KEYWORD', 'WEB_DATE', 'WEB_TIME', 'TITLE', 'AUTHOR', 'CONTENT', 'URL', 'INS', 'WEB_READ', 'AUTADR', 'VIEW_NUMBER', 'TRAN_NUMBER', 'ANS_NUMBER', 'WEBADR', 'WEBCLS', 'CONTCLS']
        # print("self.cursor.description:",self.cursor.description)
        # table_name_arr = [tuple[0] for tuple in self.cursor.description]
        # print("获取字段的正常排序：", table_name_arr)
        # sql = "select COLUMN_NAME from information_schema.columns where table_name= '%s'" % (table_name)
        # self.cursor.execute(sql)
        # result = self.cursor.fetchall()
        table_name_value = {}
        table_name_arr = []
        sql = "select COLUMN_NAME,ORDINAL_POSITION from information_schema.columns where table_name= '%s'and TABLE_SCHEMA= '%s'" % (table_name,self.DB_NAME)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            table_name_value[str(result[i][1])] = result[i][0]
        for i in range(len(table_name_value)):
            table_name_arr.append(table_name_value[str(i+1)])
        print("table_name_arr:",table_name_arr)
    """  
        function6：
        添加一条新的数据内容  (先读出这个表单的字段和类型  然后通过完成插入)
        所需参数  DB_IP 、.DB_PORT、 DB_USER、 DB_PASSWORD、 DB_CODE、fields_dict、DB_NAME    传入参数 1、库表名 table_name 2、需要插入的详细数据list_in dist tuple
    """
    def table_in(self, table_name, list_in):
        # self.sql=sql
        # print(self.sql)
        # print(list_in)
        # 获取字段的类型 table_name_value  {'X_ID': 'datetime', 'WEB_TIME': 'datetime', 'INS': 'varchar', 'WEB_DATE': 'varchar', 'VIEW_NUMBER': 'varchar', 'TITLE': 'varchar', 'AUTADR': 'varchar', 'KEYWORD': 'varchar', 'ANS_NUMBER': 'varchar', 'CONTENT': 'varchar', 'CONTCLS': 'varchar', 'ID': 'int', 'TRAN_NUMBER': 'varchar', 'WEBADR': 'varchar', 'SOURCE': 'varchar', 'WEB_READ': 'datetime', 'AUTHOR': 'varchar', 'URL': 'varchar', 'WEBCLS': 'varchar'}
        # sql = "select COLUMN_NAME,DATA_TYPE from information_schema.columns where table_name= '%s'" % (table_name)
        # self.cursor.execute(sql)
        # result = self.cursor.fetchall()
        # table_name_value = {}
        # for i in range(len(result)):
        #     table_name_value[str(result[i][0])] = result[i][1]
        # print("字段类型：",table_name_value)
        # self.cursor.execute("select * from `%s`" % table_name)
        # # 获取字段的数组  顺序排列 table_name_arr ['ID', 'X_ID', 'SOURCE', 'KEYWORD', 'WEB_DATE', 'WEB_TIME', 'TITLE', 'AUTHOR', 'CONTENT', 'URL', 'INS', 'WEB_READ', 'AUTADR', 'VIEW_NUMBER', 'TRAN_NUMBER', 'ANS_NUMBER', 'WEBADR', 'WEBCLS', 'CONTCLS']
        # table_name_arr = [tuple[0] for tuple in self.cursor.description]
        table_name_value = {}
        table_name_arr = []
        sql_fields = "select COLUMN_NAME,ORDINAL_POSITION from information_schema.columns where table_name= '%s'and TABLE_SCHEMA= '%s'" % (table_name, self.DB_NAME)
        self.cursor.execute(sql_fields)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            table_name_value[str(result[i][1])] = result[i][0]
        for i in range(len(table_name_value)):
            table_name_arr.append(table_name_value[str(i + 1)])
        print("获取字段的正常排序：",table_name_arr)
        #开始拼装数据 自增量插入
        # temp_1 = "insert into " + table_name + ","
        temp_1 = "insert into " + table_name + " set ID=0 ,"
        # 从第二个开始取
        for i in range(1,len(table_name_arr)):
            if i == len(table_name_arr) - 1:
                temp_1 += table_name_arr[i] + '="' + str(list_in[i-1]) + '"'
            else:
                temp_1 += table_name_arr[i] + '="' + str(list_in[i-1]) + '",'
        print(temp_1)
        self.cursor.execute(temp_1)
        # 返回新插入这条数据的id值
        sql1 = ''' select LAST_INSERT_ID() '''
        num = self.cursor.execute(sql1)
        if num > 0:
            col3 = self.cursor.fetchone()
            col2 = list(col3)
            ID = col2[0]
            print("此次入分库的到的自增量id：", ID)
        else:
            ID = 0
        self.db.commit()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return ID

    """  
       function7：
       # 修改库表字段  单字段  单行
       # 所需参数 1、库表名 t_name 2、字段名 cscfield 3、原字段数据 (type:str)oldtabledata 4、要修改成的数据 newtabledata 5、数据在库表内的id号
    """
    def replace_status(self, table_name, arr_field, new_data,ID_number,*args):
        # __table_name = table_name
        # __arr_field = arr_field
        # __new_data = "999999999999999sss"
        # __replace_data = replace_data
        # __ID_number = ID_number
        # print(__table_name, __arr_field,__replace_data, "ID",__ID_number)
        if args == ():
            # sql ='update `%s` set %s=%s where id=%s '%(__table_name, __arr_field,__replace_data,int(__ID_number))
            # sql = 'update `%s` SET %s = "%s" where %s = "%s"' % ()
            # sql = "UPDATE csc_users SET USER_PASSWORD = %s  WHERE ID = 2 " % (str('csc18010587617'))

            sql = 'update %s set %s="%s" where id=%s'%(table_name,arr_field,new_data,int(ID_number))
            print(sql)
        else:
            sql = args[0]
        try:
            self.cursor.execute(sql)
            print("修改成功")
            self.db.commit()
        except:
            print("发生错误时回滚")
            self.db.rollback()
        # 关闭数据库连接
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()

    """
       function8：
       批量修改  多字段 单行
       所需参数 默认参数————1、tablename  库表名   2、content  修改的内容  3、statusstr 修改的那一行条件    输入参数args   传入sql 这里可以动态变成其他条件修改
    """
    def replace_all(self, tablename, content, statusstr, *args):
        __teblename = tablename
        __content = content
        __statusstr = statusstr
        """
        # __teblename = "web_facelibrary"
        # content = {"TITLE": "女", "WEB_DATE": "涉黑团体", "URL": "2019-07-10"}
        # statusstr = {"ID": "4"}
        # __content = content
        # __statusstr = statusstr
        """
        temp_1 = []
        for i in __statusstr.keys():
            temp_1.append(i)
        status_tmpe = temp_1[0]
        status_tmpe_value = __statusstr[str(status_tmpe)]
        print("3546667567")
        print(status_tmpe_value)
        print(status_tmpe)
        str_replace = ''
        # content {"SOURCE":"王九","WEB_DATE":"涉黑团体","URL":"2019-07-10"}
        key_arr = []
        for i in __content.keys():
            key_arr.append(i)
        print(key_arr)
        # for i in range(len(key_arr)):
        #     if i == len(key_arr) - 1:
        #         str_replace = str(str_replace) + str(key_arr[i]) + " = CASE " + str(status_tmpe) + " WHEN '" + str(status_tmpe_value) + "' THEN '" + str(__content[str(key_arr[i])]) + "' END  WHERE " + str(status_tmpe) + " IN('" + str(status_tmpe_value) + "')"
        #     else:
        #         str_replace = str(str_replace) + str(key_arr[i]) + " = CASE " + str(status_tmpe) + " WHEN '" + str(status_tmpe_value) + "' THEN '" + str(__content[str(key_arr[i])]) + "' END" + " ,"
        for i in range(len(key_arr)):
            if i == len(key_arr) - 1:
                str_replace = str(str_replace) + str(key_arr[i]) + ' = CASE ' + str(status_tmpe) + ' WHEN "' + str(status_tmpe_value) + '" THEN "' + str(__content[str(key_arr[i])]) + '" END  WHERE ' + str(status_tmpe) + ' IN("' + str(status_tmpe_value) + '")'
            else:
                str_replace = str(str_replace) + str(key_arr[i]) +  ' = CASE ' + str(status_tmpe) + ' WHEN "' + str(status_tmpe_value) + '" THEN "' + str(__content[str(key_arr[i])]) + '" END' + ' ,'
        if args == ():
            sql = "UPDATE `%s` SET %s" % (__teblename, str_replace)
        else:
            sql = args[0]
        print('sql:',sql)
        try:
            self.cursor.execute(sql)
            print("修改成功")
            self.db.commit()
        except:
            print("发生错误时回滚")
            self.db.rollback()
        # 关闭数据库连接
        self.cursor.close() #关闭游标 释放资源
        self.db.close()

    """
      function9：
      删除单条数据  
      所需参数 默认参数————1、tablename  库表名   2、statusstr  删除判断的字段 3.content 判断删除条件的的内容   输入参数args   传入sql 
   """
    def del_data_one(self,tablename,statusstr,content):
        __tablename = tablename
        __statusstr = statusstr
        __content   = content
        sql = 'delete from `%s` where %s = "%s"'%(__tablename,__statusstr,__content)
        self.cursor.execute(sql)
        print("单条数据删除成功")
        self.db.commit()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()

    """
      function10：
      删除多条数据  
      所需参数 默认参数————1、tablename  库表名   2、statusstr  删除判断的字段 3.content 判断删除条件的的内容   输入参数args   传入sql 
    """
    def del_data_all(self,tablename,statusstr_start,content_start,statusstr_end,content_end):
        __tablename         = tablename
        __statusstr_start   = statusstr_start
        __content_start     = content_start
        __statusstr_end     = statusstr_end
        __content_end       = content_end
        sql = 'DELETE FROM `%s` WHERE %s > "%s" and %s < "%s"' % (__tablename,__statusstr_start,__content_start,__statusstr_end,__content_end)
        self.cursor.execute(sql)
        print("批量删除成功")
        self.db.commit()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()

    """
      function11：
      模糊查询  单字段
      所需参数 默认参数————1、tablename  库表名   2、field  查询的字段名  3、查询的内容    输入参数args   传入sql 这里可以动态变成多条件查询
    """
    def fuzzy_query(self, tablename, field, content, *args):
        __teblename = tablename
        __field = field
        __content = content
        if args == ():
            sql = 'select * from `%s` where %s like "%s"' % (__teblename, __field, __content)
        else:
            sql = args[0]
        print(sql)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
        except:
            print("数据库连接出错")
            row = ()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return row

    """
      function12：
      模糊查询  多字段
      所需参数 默认参数————1、tablename  库表名   2、field  查询的字段名 列表  3、查询的内容  列表  输入参数args   传入sql 这里可以动态变成多条件查询
    """
    def fuzzy_query_all(self, tablename, field, content):
        __teblename = tablename
        __field = field
        __content = content
        sql = 'select * from `%s` where ' % (__teblename)
        for i in range(len(__field)):
            if i == len(__field) - 1:
                sql += __field[i] + " like " + "'" + content[i] +  "'"
            else:
                sql += __field[i] + " like " + "'" + content[i] + "'" + " and "
        print(sql)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
        except:
            print("数据库连接出错")
            row = ()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return row

    """ 
       function13：
       # 给定网站+id号  取出单条数据
       # 所需参数 DB_NAME    传入参数 1、库表名 t_name 2、数据在库表内的id号
    """
    def db_select_data_one(self, table_name, in_number):
        __t_name = table_name
        __ID_number = in_number
        self.sql = "SELECT * FROM `%s` WHERE ID = " % (__t_name) + str(__ID_number)
        try:
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()  # dict
        except:
            print("Error: unable to fetch data")
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return row

    """ 
          function13：
          # 给定网站+id号  取出单条数据
          # 所需参数 DB_NAME    传入参数 1、库表名 t_name 2、数据在库表内的id号
       """
    # row_2 = cursor.fetchmany(3)
    def db_select_data_all(self, table_name):
        __t_name = table_name
        # aa = cur.execute("select * from student")
        # self.sql = "SELECT * FROM `%s` WHERE ID = " % (__t_name) + str(__ID_number)
        self.sql ="select * from %s"%(__t_name)
        try:
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchall()  # dict
        except:
            print("Error: unable to fetch data")
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return rows

    def db_select_data_many(self, table_name,table_number):
        __t_name = table_name
        __table_number=table_number

        self.sql ="select * from %s"%(__t_name)
        try:
            self.cursor.execute(self.sql)
            rows = self.cursor.fetchmany(__table_number)  # dict
        except:
            print("Error: unable to fetch data")
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return rows


    """ 
       function14：
       复制表到另外一个新建表
       # 所需参数 1.带复制的表  2.目的表  
    """
    def copy_table(self,tablename,totablename):
        pass

    """ 
      function15：
      查询当日数据
      # 所需参数 1.库表名  2.字段名
   """
    def agent_pool(self,tablename,fieldname):
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 今天0点0分1秒开始
        nowtimeyear = datetime.now().strftime('%Y-%m-%d')
        fristtime = nowtimeyear + " " + "00:00:01"
        try:
            sql = 'select * from %s where %s between "%s" and "%s"' % (tablename,fieldname,fristtime, nowtime)
            # 使用 execute()  方法执行 SQL 查询
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
        except:
            print("数据库连接出错")
            row = ()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return row

    def join_two(self, tablename, field, content, *args):
        __teblename = tablename
        __field = field
        __content = content
        if args == ():
            sql = 'select * from `%s` where %s like "%s"' % (__teblename, __field, __content)
        else:
            sql = args[0]
        print(sql)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
        except:
            print("数据库连接出错")
            row = ()
        self.cursor.close()  # 关闭游标 释放资源
        self.db.close()
        return row


if __name__ == '__main__':
    pass
    DB_cfg={"DB_IP":"localhost","DB_PORT":3306,"DB_USER": 'root',"DB_PASSWORD": 'root', "DB_NAME":'test',"DB_CODE":'utf8mb4'}

    '''--------------------------Create_table-----------------------------------'''
    fields_dict = {"1": "`ID` varchar(128) NOT NULL",
                   "2": "`X_ID` datetime DEFAULT CURRENT_TIMESTAMP",
                   "3": "`MACHINE_NAME` varchar(128) NOT NULL",
                   "4": "`MACHINE_TYPE` varchar(128) NOT NULL",
                   "5": "`MACHINE_UPDATE` datetime DEFAULT CURRENT_TIMESTAMP",
                   "99": "PRIMARY KEY (`ID`)"}

    DB_config_client=DB_config(DB_cfg)
    DB_config_client.connet_table()  # 创建数据库连接
    # DB_config_client.create_database('csc')
    # # 创建数据库表  传入库表名  字段数  字段列表
    # DB_config_client.connet_table() # 创建数据库连接
    # DB_config_client.table_create("csc_machines", 5, fields_dict) #创建数据库代码  此代码运行后回自动关闭连接
    # # # # 数据库表设置为自增量  传入数据库表名
    # time.sleep(3)
    # DB_config_client.connet_table() # 创建数据库连接
    # DB_config_client.table_set("csc_machines") # 数据库主键自增代码  此代码运行后回自动关闭连接
    '''--------------------------Check_table_max-----------------------------------'''
    # print(DB_config_client.db_max("age_info"))
    '''--------------------------Check_add_one-------------------------------------'''
    # in_data = ["2020", "test"]
    # DB_config_client.connet_table()  # 创建数据库连接
    # print(DB_config_client.table_in("age_info", in_data))
    '''--------------------------Check_select_one-------------------------------------'''
    # print(DB_config_client.db_select_data_one("user", 1))
    user_data = DB_config_client.fuzzy_query('b','userid','%1%')
    print("user_data:",user_data)
    # 读取所有user表单
    # user_data = ((1, 'aaa', 18, '123111', 12), (2, 'bbb', 24, '3443', 16))
    user_data_1 = {}
    for i in user_data:
        user_data_1[str(i[4])] = str(i[0])
    print(user_data_1) # {'12': '1', '16': '2'}

    DB_config_client.connet_table()
    user_data_info = DB_config_client.fuzzy_query('a', 'userid', '%2%')
    print("user_data_info:", user_data_info)
    # 读取所有user表单
    # # user_data = ((1, 'aaa', 18, '123111', 12), (2, 'bbb', 24, '3443', 16))
    #     # user_data_1 = {}
    # info_all = []
    # for i in user_data_info:
    #     ID_1 = i[0]
    #     account_id = user_data_1[str(i[1])]
    #     print("account_id:%s,ID_1:%s"%(account_id,ID_1))
    #     DB_config_client.connet_table()
    #     DB_config_client.replace_status('age_info','accountID',account_id,ID_1)
    # print(user_data_1)  # {'12': '1', '16': '2'}

    user_data = DB_config_client.fuzzy_query('b', 'userid', '%1%')
    print("user_data:", user_data)
    # 读取所有user表单
    # user_data = ((1, 'aaa', 18, '123111', 12), (2, 'bbb', 24, '3443', 16))
    user_data_1 = {}
    for i in user_data:
        user_data_1[str(i[4])] = str(i[0])
    print(user_data_1)