import pymongo

from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://kevin349831:33975712@ds119772.mlab.com:19772/mymongodb")

db = client["mymongodb"]

collection = db.test_collection
