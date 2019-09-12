import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from helpers import *



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)



@app.route('/')
def home():
    return render_template("home.html", 
    Page_name = 'Home',
    Page_title = "The Pâtisserie Journal", 
    Welcome_image = "../static/img/home-bg.jpg")

  
@app.route('/recipes')
def recipes():
    return render_template("recipes.html",
    Page_name = 'Recipes',
    Page_title = "Discover recipes by...", 
    Welcome_image = "../static/img/recipes-bg.jpg", 
    categories = mongo.db.recipes_categories.find(), 
    carousel = image_folder('carousel'))


@app.route('/signup')
def signup():
    return render_template('signup.html',
    Page_name = 'Sign up')
    
@app.route('/insert_user_account', methods=['POST'])
def insert_user_account():
    user_accounts = mongo.db.user_accounts
    user_accounts.insert_one(request.form.to_dict())
    return "Thanks for signing up!"


@app.route('/login')
def login():
    return render_template('login.html',
    Page_name = 'Log In')
    

@app.route('/recipes/brownie')
def brownie():
    return render_template("brownie.html", recipes=mongo.db.recipes_information.find())

 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            