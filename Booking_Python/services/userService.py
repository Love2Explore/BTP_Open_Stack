from util.db import myUsers
from bson.objectid import ObjectId
from model.user import UserModel

from util.db import myUsers
from bson.objectid import ObjectId
# myUsers.create_index("username",keys="username")

class UserService:
    def find_by_name(username,id):
        if id:
            result = myUsers.find_one({"_id":ObjectId(id)})
        else:
            result = myUsers.find_one({"username":username})
        return  result

    def save_to_db(username,password):
        user = UserModel(username=username , password=password)
        result = myUsers.insert_one(user.to_dict())
        return {'Object_Id':str(result.inserted_id)}
    
    def delete_from_db(self):
        pass