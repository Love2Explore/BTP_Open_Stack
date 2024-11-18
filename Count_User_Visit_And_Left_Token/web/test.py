
import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb+srv://rewatiraman725042:Hello123@cluster0.oa2ao.mongodb.net/")
mydb = client["mydatabase"]

mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

