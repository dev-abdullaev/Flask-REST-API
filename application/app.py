"""
Main application file
"""

import os
from datetime import datetime
from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from .services import error_response, success_response, CustomValidationError

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db.get_collection('test')
mongo = db


@app.route('/', methods=['GET'])
def welcome_page():
    """Welcome page route"""
    return 'Welcome to the application'


@app.route('/api/v1/', methods=['GET'])
def get_all_data():
    """API endpoint to get all data"""
    objs = mongo.find().sort("_id", -1)
    if mongo.count_documents({}) == 0:
        raise CustomValidationError(msg='No objects found', code=404)

    new_ls = []
    for obj in objs:
        obj['_id'] = str(obj['_id'])
        new_ls.append(obj)
    return success_response(results=new_ls)


@app.route('/api/v1/add/', methods=['POST'])
def add_data():
    """API endpoint to add data"""
    data = request.json
    key = data.get('key')
    value = data.get('value')

    if key is None or value is None:
        raise CustomValidationError(msg='Key or value not found', code=400)

    if mongo.count_documents({'key': key}, limit=1) > 0:
        raise CustomValidationError(msg='Object with the same key name already exists.', code=400)

    inserted_object = {
        "key": key,
        "value": value,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow()
    }
    mongo.insert_one(inserted_object)
    inserted_object['_id'] = str(inserted_object['_id'])
    return success_response(results=inserted_object)


@app.route('/api/v1/update/<string:key>/', methods=['PUT'])
def update_data(key):
    """API endpoint to update data"""
    data = request.json
    new_value = data.get('value')
    updated_at = datetime.utcnow()

    result = mongo.update_one({"key": key}, {"$set": {"value": new_value, "updated_at": updated_at}})
    if result.modified_count > 0:
        result = mongo.find_one({"key": key})
        result['_id'] = str(result['_id'])
        return success_response(results=result), 200
    return error_response(msg='Object not found'), 404


@app.route('/api/v1/get/<string:key>/', methods=['GET'])
def get_data(key):
    """API endpoint to get specific data by key"""
    obj = mongo.find_one({"key": key})

    if obj:
        obj['_id'] = str(obj['_id'])
        return success_response(results=obj), 200
    return error_response(msg='Object not found'), 404
