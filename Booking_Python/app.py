from flask import Flask
from flask_restful import Api
from resources.booking  import BookingResource
from resources.user  import UserResource


app = Flask(__name__)
api = Api(app)
api.add_resource(BookingResource, '/asmbtp/booking','/asmbtp/booking/<string:id>')
api.add_resource(UserResource, '/asmbtp/user','/asmbtp/user/<string:username>','/asmbtp/user/<string:id>')
# api.add_resource(booking, '/booking')


if __name__ == '__main__':
    print("Application is running on port 3000!!")
    app.run(port=3000)