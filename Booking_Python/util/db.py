import pymongo
myclient = pymongo.MongoClient("mongodb+srv://workportal1992:gFYgIJRE5WZHc5yf@cluster0.a7j0f.mongodb.net/")
mydb = myclient["myDB"]

mycol = mydb["movietickets"]