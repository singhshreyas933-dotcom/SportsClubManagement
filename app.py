from flask import Flask, render_template, request, redirect
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["SportsClubManagement"]
collection = db["members"]


@app.route("/")
def home():

    search = request.args.get("search", "")

    if search:
        members = list(collection.find({
            "$or": [
                {"name": {"$regex": search, "$options": "i"}},
                {"sport": {"$regex": search, "$options": "i"}},
                {"membership": {"$regex": search, "$options": "i"}}
            ]
        }))
    else:
        members = list(collection.find())

    total_members = len(members)

    sports = set()

    for member in members:
        sports.add(member["sport"])

    total_sports = len(sports)

    gold_members = collection.count_documents({"membership": "Gold"})
    silver_members = collection.count_documents({"membership": "Silver"})
    bronze_members = collection.count_documents({"membership": "Bronze"})

    return render_template(
        "index.html",
        members=members,
        total_members=total_members,
        total_sports=total_sports,
        search=search,
        gold_members=gold_members,
        silver_members=silver_members,
        bronze_members=bronze_members
    )


@app.route("/add", methods=["POST"])
def add_member():

    name = request.form["name"]
    age = int(request.form["age"])
    sport = request.form["sport"]
    membership = request.form["membership"]
    

    member = {
        "name": name,
        "age": age,
        "sport": sport,
        "membership": membership
    }

    collection.insert_one(member)

    return redirect("/")


@app.route("/edit/<id>")
def edit_member(id):

    member = collection.find_one({"_id": ObjectId(id)})

    return render_template("edit.html", member=member)


@app.route("/update/<id>", methods=["POST"])
def update_member(id):

    name = request.form["name"]
    age = int(request.form["age"])
    sport = request.form["sport"]
    membership = request.form["membership"]

    collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": name,
                "age": age,
                "sport": sport,
                "membership": membership
            }
        }
    )

    return redirect("/")


@app.route("/delete/<id>")
def delete_member(id):

    collection.delete_one({"_id": ObjectId(id)})

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)