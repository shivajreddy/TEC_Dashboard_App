# from app import app
import pymongo
import certifi


#! MongoDB configuration
CONNECTION_STRING = "mongodb+srv://shivajreddy:con5dential;@cluster0.wmifu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo_client = pymongo.MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())
db = mongo_client.tec_dashboard_users
users_collection = db.users

