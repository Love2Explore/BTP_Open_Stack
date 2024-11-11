from flask_restful import Resource,reqparse
from services.userService import UserService
from flask import jsonify,request

class UserResource(Resource):
    def __init__(self) :
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',required=True,help="Username is required" , type=str)
        self.parser.add_argument('password',required=True,help="Password is required" , type=str)

    def get(self):
        username = request.args.get('username')
        id = request.args.get('id')
        user = UserService.find_by_name(username,id)
        if user:
            user["_id"]= str(user["_id"])
            return  jsonify(user)
        else:
            return {"message":"No record Found"} , 404    
    def post(self):
        data = self.parser.parse_args()
        user = UserService.save_to_db(self,data['username'],data['password'])
        return user

