from services.mongodb import MongoDB
from bson import ObjectId


from flask import jsonify
from flask import request
import pprint
import json

def get_results():
    if request.method == 'GET':
        #### Get parameters
        document_id = request.args.get('document_id')
        mongodb = MongoDB()
        if document_id is not None:
            result = mongodb.find_one(document_id)
        else:
            result = mongodb.find_and_fetch()
        result = mongodb.encode(result)
        mongodb.close()
        
        return jsonify(dict(status="success", details = result))
    else:
        resp = jsonify(dict(status="error", details="method not allowed"))
        resp.status_code = 400
        return resp