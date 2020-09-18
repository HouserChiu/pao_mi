import pymongo
from pymongo.collection import Collection

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        #数据库名
        self.db_data = self.client['douyin_fans']

    def insert_item(self,item):
        #表名
        db_collection = Collection(self.db_data,'douyin_fans_range')
        db_collection.insert(item)

mongo_info_range = Connect_mongo()