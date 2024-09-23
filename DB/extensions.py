from pymongo import MongoClient

MONGO_PASS = ''
# Setup MongoDB here
client = MongoClient("mongodb+srv://vehdat:"+MONGO_PASS+"@github-actions.mgpqw.mongodb.net/")
db = client['github-actions']
col = db['actions']