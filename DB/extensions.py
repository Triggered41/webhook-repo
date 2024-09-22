from pymongo import MongoClient


# Setup MongoDB here
client = MongoClient("mongodb+srv://vehdat:Sad47dd8N@github-actions.mgpqw.mongodb.net/")
db = client['github-actions']
col = db['actions']