import pymongo
import web_spider
from pymongo.collection import Collection


def gender_female():
    web_spider.get_detail()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ldl_info"]
    mycol = mydb["ldl_info_data"]
    # _id字段设置为0，就不会显示
    # 查询gender字段为1的数据，1代表女，并遍历
    gender_female = []
    for temp in mycol.find({"gender": "1"}, {"_id": 0}):
        gender_female.append(temp)
    return gender_female
