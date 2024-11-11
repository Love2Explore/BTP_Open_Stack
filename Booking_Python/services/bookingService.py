from util.db import myBookings
from bson.objectid import ObjectId
from model.booking import BookingModel
class BookingService:
    def find_one(id):
        result = myBookings.find_one({"_id":ObjectId(id)})
        return result

    def save_to_db(username,movie_id):
        booking = BookingModel(username=username , movie_id=movie_id)
        result = myBookings.insert_one(booking.to_dict())
        return {'Object_Id':str(result.inserted_id)}
    
    def delete_from_db(self):
        pass