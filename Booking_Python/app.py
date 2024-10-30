from flask import Flask
from flask_restful import Api
from util.db import mycol
from controller.booking import booking


app = Flask(__name__)
api = Api(app)
api.add_resource(booking, '/booking/<string:name>')


if __name__ == '__main__':
    print("Application is running on port 3000!!")
    app.run(port=3000)