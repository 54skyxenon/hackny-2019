from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
from pymongo import MongoClient
from bson import ObjectId


builtin_list = list


mongo = None


def _id(id):
    if not isinstance(id, ObjectId):
        return ObjectId(id)
    return id


# [START from_mongo]
def from_mongo(data):
    """
    Translates the MongoDB dictionary format into the format that's expected
    by the application.
    """
    if not data:
        return None

    data['id'] = str(data['_id'])
    return data
# [END from_mongo]


def init_app(app):
    global mongo

    mongo = PyMongo(app)
    mongo.init_app(app)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# [START list]
def list(limit=10, cursor=None):
    cursor = int(cursor) if cursor else 0

    client = MongoClient()
    db = client.db_name
    collection = db.collection_name

    results = mongo.db.locations.find(skip=cursor, limit=10).sort('Name')

    cursor = collection.find({})
    file = open("collection.json", "w")
    # file.write('[')

    locations = builtin_list(map(from_mongo, results))
    # print(type(locations))
    # print(locations)
    dictOfWords = {i: locations[i] for i in range(0, len(locations))}
    l = JSONEncoder().encode(dictOfWords)
    file.write(l)
    # for item in locations:
    #     file.write(json.dumps(locations))
    #     file.write(',')
    # file.write(']')

    next_page = cursor + limit if len(locations) == limit else None

    return (locations, next_page)
# [END list]


# [START read]
def read(id):
    result = mongo.db.locations.find_one({'_id': _id(id)})
    return from_mongo(result)
# [END read]


# [START create]
def create(data):
    result = mongo.db.locations.insert_one(data)
    return read(result.inserted_id)
# [END create]


# [START update]
def update(data, id):
    mongo.db.locations.replace_one({'_id': _id(id)}, data)
    return read(id)
# [END update]


def delete(id):
    mongo.db.locations.delete_one({'_id': _id(id)})
