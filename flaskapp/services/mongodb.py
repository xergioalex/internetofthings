# MongoDB
import pymongo, pprint
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId


class MongoDB(object):

    def __init__(self, collection='results', db='iot'):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client[db]
        self.dbCollection = self.database[collection]

    # Find all documents
    def find(self):
        result = self.dbCollection.find().sort('createdAt', pymongo.DESCENDING)
        return result

    def find_and_fetch(self):
        result = list(self.dbCollection.find().sort('createdAt', pymongo.DESCENDING))
        return result

    # Find one document
    def find_one(self, document_id=None):
        if document_id:
            result = self.dbCollection.find_one({ '_id': ObjectId(document_id) })
        else:
            result = self.dbCollection.find_one()
        return result

    # Insert data in mongo collection
    def insert_one(self, data):
        data['createdAt'] = datetime.datetime.utcnow()
        data['updatedAt'] = datetime.datetime.utcnow()
        result_id = self.dbCollection.insert_one(data).inserted_id
        return result_id

    # Update data in mongo collection
    def update_one(self, document_id, data):
        data['updatedAt'] = datetime.datetime.utcnow()
        result = self.dbCollection.update_one({'_id': ObjectId(document_id) }, { '$set': data })
        return result

    # Remove data in mongo collection
    def delete_one(self, document_id):
        result = self.dbCollection.delete_one({'_id': ObjectId(document_id) })
        return result

    # Encode data
    def encode(self, data):
        if type(data) == type([]):
            for item in data:
                item['_id'] = str(item['_id'])
        else:
            data['_id'] = str(data['_id'])
        return data

    # Close
    def close(self):
        self.client.close()