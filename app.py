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
    return render_template('cities.html', cities=mongo.db.cities.find())


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/get_search', methods=['GET', 'POST'])
def get_search():
    query = request.form.get('query')
    cities = list(mongo.db.cities.find({'$text': {'$search': query}}))
    return render_template('search.html', cities=cities)


@app.route('/contacts') 
def contacts():
    return render_template('contacts.html')


@app.route('/get_city/<city_id>')
def get_city(city_id):
    city = mongo.db.cities.find_one({'_id': ObjectId(city_id)})
    return render_template('city.html', city=city)


@app.route('/add_city')
def add_city():
    return render_template('addcity.html')


@app.route('/insert_city', methods=['POST'])
def insert_city():
    cities = mongo.db.cities
    cities.insert_one(request.form.to_dict())
    return redirect(url_for('get_cities'))


@app.route('/edit_city/<city_id>')
def edit_city(city_id):
    the_city = mongo.db.cities.find_one({'_id': ObjectId(city_id)})
    return render_template('editcity.html', city=the_city)


@app.route('/update_city/<city_id>', methods=['POST'])
def update_city(city_id):
    cities = mongo.db.cities
    cities.update({'_id': ObjectId(city_id)},
    {
        'city_name': request.form.get('city_name'),
        'country_name': request.form.get('country_name'),
        'best': request.form.get('best'),
        'worst': request.form.get('worst'),
        'eat': request.form.get('eat'),
        'sleep': request.form.get('sleep'),
        'other': request.form.get('other'),
        'img_link': request.form.get('img_link')
    })
    return redirect(url_for('get_cities'))


@app.route('/delete_city/<city_id>')
def delete_city(city_id):
    mongo.db.cities.remove({'_id': ObjectId(city_id)})
    return redirect(url_for('get_cities'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    #DO NOT FORGET TO SET THIS TO FALSE IN THE END OF THE PROJECT