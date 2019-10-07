import os
import logging
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
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


# ----- Routes ----- #

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", 
                            Page_name = "Home",
                            Page_title = "The Pâtisserie Journal", 
                            Welcome_image = "../static/img/home/bg.jpg")

  
@app.route("/recipes")
def recipes():
    return render_template("recipes.html",
                            Page_name = "Recipes",
                            Page_title = "Discover recipes by...", 
                            Welcome_image = "../static/img/categories/bg.jpg", 
                            categories = mongo.db.recipes_categories.find(), 
                            carousel = image_folder("carousel"))


@app.route("/recipes/<category_name>")
def recipes_categories(category_name):
    
    the_category =  mongo.db.recipes_categories.find_one({"category_name": category_name})
    
    #Log the_category
    logging.info('The variable the_category has the following result: {}'.format(the_category))
    
    the_name_category = the_category["category_name"].capitalize()

    return render_template("recipes_categories.html", 
                            Page_name = the_name_category,
                            Page_title = "Discover recipes for...", 
                            Welcome_image = "../static/img/categories/bg.jpg", 
                            category=the_category, 
                            carousel = image_folder("carousel"))


@app.route("/about")
def about():
    return render_template("about.html", 
                            Page_name = "About Us",
                            Page_title = "About Us", 
                            Welcome_image = "../static/img/about/bg.jpg")


@app.route("/signup")
def signup():
    
    if "email" in session:
        flash(f"You are logged in as {session['email']}", "white-text green")
        return redirect(url_for('home'))
        
    form = SignupForm()
    
    return render_template("signup.html",
                            Page_name = "Sign up",
                            Welcome_image = "../static/img/sign/bg.jpg",
                            form=form)


@app.route("/insert_user_account", methods=["GET", "POST"])
def insert_user_account():
    
    if request.method == "POST":
  
        form = SignupForm()
        user_accounts = mongo.db.user_accounts
        # Create a query to check if a user already registered with this email:
        user = user_accounts.find_one( { "email": form.email.data })
        
        #Log the query
        logging.info('Email found in MongoDB: {} match the email provided by the user in the form'.format(user))
        
        # Check if email provided is not already linked to an existing account
        if user:
            flash(f"An account already exists for {form.email.data}.", "white-text red")
            return redirect(url_for("signup"))
        
        # If no existing account was found we can add the user to the db
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
        
    return redirect(url_for("signup"))


@app.route("/login", methods=["POST", "GET"])
def login():
    
    if "email" in session:
        flash(f"You are logged in as {session['email']}", "white-text green")
        return redirect(url_for('home'))
    
    form = LoginForm()
        
    if form.validate_on_submit():
            
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": form.email.data })
    
        #Log the query
        logging.info('User found {}'.format(user))
            
        user_password = user["password"]
            
        if user and bcrypt.check_password_hash(user_password, form.password.data):
                
            # Add user to session
            session["email"] = user["email"]
            session["first_name"] = user["first_name"]
            session["last_name"] = user["last_name"]
            flash("Login successful!", "white-text green darken-1")
            return redirect(url_for("account"))
            
        else:
            flash("Login unsuccessful! Email and/or password incorrect.", "white-text red")
        
    return render_template("login.html",
                                Page_name = "Log In",
                                Welcome_image = "../static/img/sign/bg.jpg",
                                form=form)


# Routes (for which login is required)


@app.route("/account")
def account():
    return render_template("account.html",
                            Page_name = "My Account",
                            Page_title = f"Hi {session['first_name'].capitalize()}, welcome!")


@app.route("/cookbook")
def cookbook():
    
    #Check if the user is logged in
    if "email" in session:
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })
    
        #Log the user
        logging.info('User found {}'.format(user))
        
        #Create a variable to store the favorite recipes linked to this user
        favorite_recipes = user["favorite_recipes"]
        
        #Count the number of recipes stored as favourite by the user
        recipes_number = len(favorite_recipes)
        
        #Iterate through each recipes id and extract information in MongoDB collection "recipes_information"
        
        recipes_list_information = []
        
        for i in range(recipes_number):
            
            #Create a query to get recipes information based on user list
            recipe_information_i = mongo.db.recipes_information.find_one( { "_id": ObjectId(favorite_recipes[i]) })

            #Store information in an array
            recipes_list_information.append(recipe_information_i)
            
            #Log each recipe_information variable
            logging.info('For i={}, the recipes information found is {}'.format(i, recipe_information_i))
            
        #Log the variable recipes list information
        logging.info('Array containing all recipes information {}'.format(recipes_list_information))
    
        return render_template("cookbook.html",
                            Page_name = "Cookbook",
                            Page_title = "My Cookbook", 
                            Welcome_image = "../static/img/cookbook/bg.jpg",
                            recipes = recipes_list_information )
    
    flash(f"You are required to login to access this page", "white-text red")
    return redirect(url_for('login'))


@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html",
                            Page_name = "Add Recipe",
                            Page_title = "Add Recipe", 
                            Welcome_image = "TBD")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("email", None)
    session.pop("first_name", None)
    session.pop("last_name", None)
    flash("Thanks for your visit, we hope to see you soon!", "blue-grey lighten-5")
    return redirect(url_for("login"))


# Route created only as an instance of recipe page

@app.route("/results")
def results():
    recipes_count=mongo.db.recipes_information.count()
    return render_template("results.html",
                            recipes=mongo.db.recipes_information.find(),
                            Page_name = "All Recipes",
                            Page_title = f"{recipes_count} Recipes Found")


@app.route("/results/<recipe_id>")
def recipe_description(recipe_id):
    
    the_recipe =  mongo.db.recipes_information.find_one({"_id": ObjectId(recipe_id)})
    
    #Log the_category
    logging.info('The variable the_recipe has the following result: {}'.format(the_recipe))
    
    the_recipe_name = the_recipe["recipe_name"].capitalize()

    return render_template("recipe_description.html", 
                            Page_name = the_recipe_name,
                            Page_title = f"{the_recipe_name}", 
                            recipe=the_recipe)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)