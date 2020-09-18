# coding: utf-8

import pymongo
from pymongo.collection import Collection

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        #数据库名
        self.db_data = self.client['alibaba_info_modify']

    def insert_item(self,item):
        #表名
        db_collection = Collection(self.db_data,'alibaba_info_data_modify')
        db_collection.insert(item)

mongo_info_alibaba = Connect_mongo()