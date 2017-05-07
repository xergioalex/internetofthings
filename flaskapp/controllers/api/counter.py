from services.mongodb import MongoDB
from bson import ObjectId

from flask import jsonify, request
import pprint
import json

def get_counter():
    if request.method == 'GET':
        print('Entraaa')
        mongodb = MongoDB('counters')
        result = mongodb.find_one()
        if result is None:
            resultId = mongodb.insert_one({ "counter": 0 })
            result = mongodb.find_one(resultId)
        result = mongodb.encode(result)
        mongodb.close()        

        return jsonify(dict(status="success", details = result))
    else:
        resp = jsonify(dict(status="error", details="method not allowed"))
        resp.status_code = 400
        return resp

def add_counter():
    if request.method == 'GET':
        mongodb = MongoDB('counters')
        result = mongodb.find_one()
        if result is None:
            resultId = mongodb.insert_one({ "counter": 0 })
            result = mongodb.find_one(resultId)
        result["counter"] = result["counter"] + 1
        mongodb.update_one(result["_id"], result)
        result = mongodb.encode(result)
        mongodb.close()

        return jsonify(dict(status="success", details = result))
    else:
        resp = jsonify(dict(status="error", details="method not allowed"))
        resp.status_code = 400
        return resp