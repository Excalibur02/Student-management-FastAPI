from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_url = "mongodb+srv://dhruv:fast1234@fast0.q8zzk.mongodb.net/?retryWrites=true&w=majority&appName=fast0"
client = MongoClient(db_url)

database = client.student_management

students_collection = database["students"]
id_collection = database["ID"]

if id_collection.count_documents({"_id": "id"}) == 0:
    id_collection.insert_one({"_id": "id", "value": 0})
