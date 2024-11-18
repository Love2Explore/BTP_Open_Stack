from flask import Flask,jsonify,request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
from thefuzz import fuzz

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb+srv://rewatiraman725042:Hello123@cluster0.oa2ao.mongodb.net/")
db  = client["aNewDB"]
UserNum = db["UserNumber"]
UserRegistration_DB = db["users"]


def UserExist(username):
    result = UserRegistration_DB.find_one({"username":username}) 
    if result == None:
        return False
    else:
        return True

def checkPassword(username,password):
    user_detail = UserRegistration_DB.find_one({"username":username})
    if user_detail["password"]:
        hash_pw = user_detail["password"]
        global token_count 
        token_count = user_detail["token"]
        match_pwd = bcrypt.checkpw(password.encode('utf-8') , hash_pw)
        return match_pwd
    else:
        return False
       

class UserRegistration(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        # Check whether user Exist in DB or not
        if UserExist(username):
            return ({"message":"User ALready Exists.","status":301}), 301
        hash_pw = bcrypt.hashpw(password.encode('utf-8') , bcrypt.gensalt())
        #Save user information
        result = UserRegistration_DB.insert_one({"username":username,"password":hash_pw,"token":6})
        return {"status":201,"msg":"User Created!","Object_Id":str(result.inserted_id)}
    
class Detect(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        text1 = request_data["text1"]
        text2 = request_data["text2"]
        #user Exit or not
        if not UserExist(username):
            return {"status":301 ,"msg":"User not Exist."}
        #Check Password matching or not
        if not checkPassword(username,password):
            return {"status":301 ,"msg":"Invalid Password."}
        if token_count == 0:
            return {"status":302 ,"msg":"Out of Tokens."}
        
        #calculate document matching
        ratio = fuzz.ratio(text1, text2)
        response = {"status":200,"msg":"Text matching Ratio Score.","ratio":ratio}
        # update Token
        UserRegistration_DB.update_one({"username":username} , {"$set":{"token":token_count-1}})
        return jsonify(response)
    
class Recharge(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        #user Exit or not
        if not UserExist(username):
            return {"status":301 ,"msg":"User not Exist."}
        #Check Password matching or not
        if not checkPassword(username,password):
            return {"status":301 ,"msg":"Invalid Password."}
        UserRegistration_DB.update_one({"username":username} , {"$set":{"token":6}})
        return {"status":200,"msg":"Token Updated."}
    
api.add_resource(UserRegistration,"/user-register")
api.add_resource(Detect,"/detect")
api.add_resource(Recharge,"/refill")


if __name__ == "__main__":
    # app.run(host="127.0.0.1",port=8080)
    print("Application running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0")
        

        
