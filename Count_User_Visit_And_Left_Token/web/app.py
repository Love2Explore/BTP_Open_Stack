from flask import Flask,jsonify,request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb+srv://rewatiraman725042:Hello123@cluster0.oa2ao.mongodb.net/")
db  = client["aNewDB"]
UserNum = db["UserNumber"]
UserRegistration_DB = db["users"]

UserNum.insert_one({ "userNumber": 0 })

class UserRegistration(Resource):
    def post(self):
        postData = request.get_json()
        username = postData["username"]
        description = postData["description"]
        password = bcrypt.hashpw(postData["password"].encode('utf-8') , bcrypt.gensalt(10))
        result = UserRegistration_DB.insert_one({"username":username,"password":str(password),"description":description,"token":5})
        return jsonify({"Object_Id":str(result.inserted_id)})

class Store(Resource):
    def post(post):
        postData = request.get_json()
        username = postData["username"]
        password = postData["password"]
        description = postData["description"]
        #Check username and password
        hash_pw = getUserPassword(username)
        check_password = bcrypt.checkpw(password.encode('utf-8') , bytes(hash_pw[2:-1],'utf-8'))
        if not check_password:
            return { "status": 302 } ,302
        #count number of token
        count_token = countToken(username)
        if count_token <= 0:
            return { "status": 302 } ,302
        #update actual count
        update_token(username,description,count_token)
        return {"status": 200},200
        # UserRegistration_DB.update_one

def getUserPassword(username):
    user_detail = UserRegistration_DB.find_one({"username":username})
    if user_detail["password"]:
        return user_detail["password"]
    else:
        return None

def countToken(username):
    user_detail = UserRegistration_DB.find_one({"username":username})
    if user_detail["token"]:
        return user_detail["token"]
    else:
        return 0

def update_token(username,description,count_token):
    UserRegistration_DB.update_one({"username":username},{"$set":{
        "description":description,
        "token":count_token-1
    }})

class Visit(Resource):
    def get(self):
        current_number = UserNum.find({})[0]["userNumber"]
        new_number = current_number + 1
        UserNum.update_one({"userNumber": current_number}, {"$set":{"userNumber": new_number}})
        return str(new_number)

def  checkData(postData,method):
        if method == "add" or method == "subtract" or method == "multiply":
            if "x" not in postData or "y" not in postData:
                return 301
            else:
                return 201
        
        if method == "divide":
            if ("x" not in postData or "y" not in postData) :
                return 301
            else:
                if int(postData["y"]) == 0:
                    return 400
                return 201


class Add(Resource):
    def post(self):
        postData = request.get_json()
        if checkData(postData, "add") == 301:
            return {"message":"Error","status":301}, 301
        x = postData["x"]
        y = postData["y"]
        x = int(x) 
        y = int(y)
        response = { 'message': x+y , 'status':201}
        return jsonify(response)

class Subtract(Resource):
    def post(self):
        postData = request.get_json()
        if checkData(postData, "subtract") == 301:
            return {"message":"Error","status":301}, 301
        x = postData["x"]
        y = postData["y"]
        x = int(x) 
        y = int(y)
        response = { 'message': x-y , 'status':201}
        return jsonify(response)

class Divide(Resource):
    def post(self):
        postData = request.get_json()
        checkvalue = checkData(postData, "divide")
        if checkvalue == 301:
            return {"message":"Error","status":301}, 301
        elif checkvalue == 400:
            return {"message":"Y can not be 0","status":400}, 400
        x = postData["x"]
        y = postData["y"]
        x = int(x) 
        y = int(y)
        response = { 'message': x/y , 'status':201}
        return jsonify(response)

class Multiply(Resource):
    def post(self):
        postData = request.get_json()
        if checkData(postData, "multiply") == 301:
            return {"message":"Error","status":301}, 301
        x = postData["x"]
        y = postData["y"]
        x = int(x) 
        y = int(y)
        response = { 'message': x*y , 'status':201}
        return jsonify(response)

api.add_resource(Add,"/add")
api.add_resource(Subtract,"/sub")
api.add_resource(Multiply,"/mul")
api.add_resource(Divide,"/div")

api.add_resource(Visit,"/")

api.add_resource(UserRegistration,'/register')
api.add_resource(Store,'/store')

@app.route("/add_two_num", methods=["POST"])
def add_num():
    req = request.get_json()
    return jsonify(req) ,202

# @app.route("/", methods=["GET"])
# def num():
#     return "Hello World!"

if __name__ == "__main__":
    # app.run(host="127.0.0.1",port=8080)
    print("Application running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0")
    
