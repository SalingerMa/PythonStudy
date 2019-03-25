# -*- coding: utf-8 -*-
import pymongo

class MyMongo():
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         cls._instance = super(MyMongo, cls).__new__(cls)
    #     return cls._instance

    def __init__(self, collection, db='mymongo', host='localhost', port=27017):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def insert_one(self, data):
        result = self.collection.insert_one(data)
        return {'result': result, 'id': result.inserted_id}

    def insert_many(self, *data):
        result = self.collection.insert_many(list(data))
        return {'result': result, 'id': result.inserted_ids}





if __name__ == '__main__':
    mongo = MyMongo('test1')
    mongo2 = MyMongo('test2')
    student1 = {
    'id': '20170101',
    'name': 'Jodan',
    'age': 20,
    'gender': 'male'
}
    student2 = {
        'id': '20170101',
        'name': 'Jdan',
        'age': 20,
        'gender': 'male'
    }
    rec1 = mongo.insert_many(student1, student2)
    print(rec1)
    rec2 = mongo2.insert_many(student1, student2)
    print(rec2)