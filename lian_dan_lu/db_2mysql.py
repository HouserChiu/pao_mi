import pymysql
import sql_web



def gender_female():
    sql_web.get_one()
    myclient = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="test", charset="utf8mb4")
    sql = "SELECT "
    # _id字段设置为0，就不会显示
    # 查询gender字段为1的数据，1代表女，并遍历
    gender_female = []
    for temp in mycol.find({"gender": "1"}, {"_id": 0}):
        gender_female.append(temp)
    return gender_female
