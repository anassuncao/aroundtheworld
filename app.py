import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "aroundtheworld"

app = Flask(__name__)

app.config["MONGODB_NAME"] = "aroundtheworld"
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_cities')
def get_cities():
    return render_template("cities.html", cities=mongo.db.cities.find())

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    #DO NOT FORGET TO SET THIS TO FALSE IN THE END OF THE PROJECT
