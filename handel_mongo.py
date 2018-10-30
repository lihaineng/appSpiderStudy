import pymongo
from pymongo.collection import Collection


class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='172.18.113.176',port=27017)
        print('连接成功')
        self.db_data = self.client['dou_guo_mei_shi']

    def insert_item(self,item):
        db_collection = Collection(self.db_data,'dou_guo_mei_shi_item')
        db_collection.insert(item)
        print('存储成功')


mongo_info = Connect_mongo()
