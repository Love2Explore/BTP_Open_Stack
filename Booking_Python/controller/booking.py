from flask_restful import Resource,  reqparse
from bson.objectid import ObjectId
from util.db import mycol

class booking(Resource):
    def get(self , name):
        item = mycol.find_one({"_id":ObjectId(name)})
        if item:
            return list(item)
        else:
            return {"message":"No record Found"} , 404    