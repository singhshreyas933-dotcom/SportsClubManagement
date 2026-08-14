from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["SportsClubManagement"]
collection = db["members"]

name = input("Enter member name to delete: ")

result = collection.delete_one({"name": name})

if result.deleted_count > 0:
    print("Member Deleted Successfully!")
else:
    print("Member Not Found!")
