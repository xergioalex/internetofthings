from services.mongodb import MongoDB
from bson import ObjectId

from flask import jsonify, request
import pprint
import json

def get_binary():
    if request.method == 'GET':
        mongodb = MongoDB('binary')
        result = mongodb.find_one()
        if result is None:
            resultId = mongodb.insert_one({ "value": 0 })
            result = mongodb.find_one(resultId)
        result = mongodb.encode(result)
        mongodb.close()

        return jsonify(dict(status="success", details = result))
    else:
        resp = jsonify(dict(status="error", details="method not allowed"))
        resp.status_code = 400
        return resp

def toggle_binary():
    if request.method == 'GET':
        mongodb = MongoDB('binary')
        result = mongodb.find_one()
        if result is None:
            resultId = mongodb.insert_one({ "value": 0 })
            result = mongodb.find_one(resultId)
        result["value"] ^= 1
        mongodb.update_one(result["_id"], result)
        result = mongodb.encode(result)
        mongodb.close()

        return jsonify(dict(status="success", details = result))
    else:
        resp = jsonify(dict(status="error", details="method not allowed"))
        resp.status_code = 400
        return resp