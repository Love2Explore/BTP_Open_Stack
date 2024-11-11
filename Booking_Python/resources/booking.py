from flask_restful import Resource,reqparse
from services.bookingService import BookingService
from flask import jsonify,request

class BookingResource(Resource):
    def __init__(self) :
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',required=True,help="Username is required" , type=str)
        self.parser.add_argument('movie_id',required=True,help="Movie ID is required" , type=str)

    def get(self ):
        id = request.args.get('id')
        booking = BookingService.find_by_name(id)
        if booking:
            booking["_id"]= str(booking["_id"])
            return  jsonify(booking)
        else:
            return {"message":"No record Found"} , 404   
    
    def post(self):
        data = self.parser.parse_args()
        booking = BookingService.save_to_db(data['username'],data['movie_id'])
        return booking 
