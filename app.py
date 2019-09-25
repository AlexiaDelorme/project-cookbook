import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from helpers import *
from forms import *
import logging

# Create a log file
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = "366eff16939348b3153b7dff1b2fc2e1æ"

mongo = PyMongo(app)



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", 
                            Page_name = "Home",
                            Page_title = "The Pâtisserie Journal", 
                            Welcome_image = "../static/img/home-bg.jpg")

  
@app.route("/recipes")
def recipes():
    return render_template("recipes.html",
                            Page_name = "Recipes",
                            Page_title = "Discover recipes by...", 
                            Welcome_image = "../static/img/recipes-bg.jpg", 
                            categories = mongo.db.recipes_categories.find(), 
                            carousel = image_folder("carousel"))


@app.route("/recipes/<category_name>")
#Use the_category in the routing
def recipes_categories(category_id):
    the_category =  mongo.db.recipes_categories.find_one({"_id": ObjectId(category_id)})
    
    category_name = the_category["category_name"]
        
    #Log the_category
    logging.info('The variable the_category has the following result: {}'.format(category_name))
    
    return render_template("recipes_categories.html", 
                            Page_name = category_name,
                            Page_title = "Discover recipes for...", 
                            Welcome_image = "../static/img/recipes-bg.jpg", 
                            category=the_category, 
                            carousel = image_folder("carousel"))


@app.route("/about")
def about():
    return render_template("about.html", 
                            Page_name = "About Us",
                            Page_title = "About Us", 
                            Welcome_image = "../static/img/about-bg.jpg")


@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html",
                            Page_name = "Sign up",
                            Welcome_image = "../static/img/sign-up.jpg",
                            form=form)


@app.route("/insert_user_account", methods=["GET", "POST"])
def insert_user_account():
    
    form = SignupForm()
    
    user_accounts = mongo.db.user_accounts
    
    # Create a query to get all emails stored in the user_accounts collection
    user = user_accounts.find_one( { "email": form.email.data })
    
    #Log the query
    logging.info('Email found in MongoDB: {} match the email provided by the user in the form'.format(user))
    
    # Check if email provided is not already linked to an existing account
    if user:
        flash(f"An account already exists for {form.email.data}", "white-text red")
        return redirect(url_for("signup"))
    
    # If no existing account was found, then we add this new user
    else:
        # Encrypt password to send it to MongoDB for storage
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Insert user information account to MongoDB
        user_accounts.insert_one({
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": form.email.data,
            "password": hashed_password,
            "my_recipes": "",
            "favorite_recipes": ""
        })
        flash(f"{form.first_name.data.capitalize()}, your account has been created, you can now log in!", "white-text green darken-1")
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "alexia.delorme@gmail.com" and form.password.data == "hola":
            flash("Login successful!", "white-text green darken-1")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful! Email and/or password incorrect.", "white-text red")
    return render_template("login.html",
                            Page_name = "Log In",
                            Welcome_image = "../static/img/sign-up.jpg",
                            form=form)


@app.route("/recipes/brownie")
def brownie():
    return render_template("brownie.html", recipes=mongo.db.recipes_information.find())



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)