import pymongo
from pymongo import MongoClient

url = "mongodb+srv://efraim:admin@cluster0.8qnuc.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print((db.list_collection_names))
