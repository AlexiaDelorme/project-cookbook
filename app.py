import os
import logging
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from bson.objectid import ObjectId
from helpers import *
from forms import *


# Create a log file
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

app = Flask(__name__)
bcrypt = Bcrypt(app)


app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = "366eff16939348b3153b7dff1b2fc2e1æ"


mongo = PyMongo(app)


# Configuring flask login for authentication

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create a user "Class" to manage user sessions

class User(UserMixin, mongo.db):
    meta = {'collection': 'user_accounts'}
    email = mongo.db.StringField()
    password = mongo.db.StringField()

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


# Routes

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
def recipes_categories(category_name):
    
    the_category =  mongo.db.recipes_categories.find_one({"category_name": category_name})
    
    #Log the_category
    logging.info('The variable the_category has the following result: {}'.format(the_category))
    
    the_name_category = the_category["category_name"]

    return render_template("recipes_categories.html", 
                            Page_name = the_name_category,
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
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = SignupForm()
    
    return render_template("signup.html",
                            Page_name = "Sign up",
                            Welcome_image = "../static/img/sign-up.jpg",
                            form=form)


@app.route("/insert_user_account", methods=["GET", "POST"])
def insert_user_account():
    
    form = SignupForm()
    
    user_accounts = mongo.db.user_accounts
    
    # Create a query to check if a user already registered with this email:
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
            "my_recipes": [],
            "favorite_recipes": []
        })
        flash(f"{form.first_name.data.capitalize()}, your account has been created, you can now log in!", "white-text green darken-1")
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": form.email.data })

        #Log the query
        logging.info('User found {}'.format(user))
        
        user_password = user["password"]
        
        if user and bcrypt.check_password_hash(user_password, form.password.data):
            
            user_obj = User.objects(email=form.email.data).first()
            login_user(user_obj)
            
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