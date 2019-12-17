import os
import logging
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from datetime import datetime
from helpers import *
from forms import *

# Create a log file
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# ---------------- #
#      ROUTES      #
# ---------------- #

# ------------------------------------------- #
#           LOG IN | NOT REQUIRED             #
# ------------------------------------------- #

# ----- 1. HOME ----- #
@app.route("/")
@app.route("/home")
def home():
    return render_template("general/home.html", 
                            Page_name = "Home",
                            Page_title = "The Pâtisserie Journal", 
                            Welcome_image = "../static/img/home/bg.jpg")

# ----- 2. EXPLORE ----- #
@app.route("/explore")
def explore():
    """
    Display a form with fields from which the user will be able to filter recipes.
    The user can then click a search button and be redirected to the results page with recipes matching the criteria.
    """
    # Create variables to filter recipes
    meal_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'meal' })
    diet_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'diet' })
    occasion_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'occasion' })
    geography_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'geography' })
    allergen_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'allergen' })
    tool_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'tool' })
    return render_template("recipes/explore.html",
                            Page_name = "Explore Recipes",
                            meal_categories = meal_categories,
                            diet_categories = diet_categories,
                            occasion_categories = occasion_categories,
                            geography_categories = geography_categories,
                            allergen_categories = allergen_categories,
                            tool_categories = tool_categories)

# ----- 2.1 EXPLORE / RECIPES RESULTS ----- #
@app.route("/explore/results", methods=["POST"])
def explore_results():
    """
    Display all the recipes matching the criteria selected in the form from the explore page.
    """
    
    # Prepare serving data
    serving = int(request.form.get("serving")) if request.form.get("serving") else ""
    # Prepare prep_time data
    if (request.form.get("prep_time") != ""):
        prep_time = int(request.form.get("prep_time"))
    else:
        prep_time = ""
    
    ## The following code block (from line 86 to 113) was implemented thanks to the Code Institute Tutor Team
    # Create a dictionary to store the form fields
    form_dictionary = {
        "difficulty": request.form.get("difficulty"),
        "serving": serving,
        "prep_time": prep_time,
        "meal": request.form.getlist("meal"),
        "diet": request.form.getlist("diet"),
        "allergen": request.form.getlist("allergen"),
        "tool": request.form.getlist("tool"),
        "occasion": request.form.getlist("occasion"),
        "geography": request.form.getlist("geography")
    }
    # Format the condition according to the fields
    map_condition = {
        "difficulty": "$eq",
        "serving": "$lte",
        "prep_time": "$lte",
        "meal": "$in",
        "diet": "$in",
        "allergen": "$nin",
        "tool": "$nin",
        "occasion": "$in",
        "geography": "$in"
    }
    query = []
    # Prevent empty fields from being passed to the query
    for field_name, field_value in form_dictionary.items():
        if (field_value != None) and (field_value != "") and (field_value != []):
            condition = { field_name: { map_condition[field_name]: field_value }}
            query.append(condition)
    # logging.info('Query is {}'.format(query))
    if query != []:
        # Pass the formatted dictionary into mongoDB query
        if len(query) == 1:
            recipes = mongo.db.recipes_information.find(condition)
        # Use the "$and" keyword to pass multiple conditions to mongoDB query
        else:
            recipes = mongo.db.recipes_information.find({ "$and": query })
    # Pass all the recipes if user did not input any filters
    else:
        recipes = mongo.db.recipes_information.find()
    
    recipes_number=recipes.count()
    
    return render_template("recipes/explore_results.html",
                            Page_name = "Recipes Results",
                            Page_title = f"{recipes_number} Recipe(s) Found",
                            recipes=recipes,
                            recipes_number = recipes_number)

# ----- 3. RECIPES ----- #
@app.route("/recipes")
def recipes():
    """
    Display categories from which the user will be able to filter recipes.
    Search recipes according a specific category by clicking on this category. 
    """
    return render_template("recipes/recipes.html",
                            Page_name = "Recipes",
                            Page_title = "RECIPES BY...", 
                            Welcome_image = "../static/img/categories/bg.jpg", 
                            categories = mongo.db.recipes_categories.find(), 
                            carousel = image_folder("carousel"))

# ----- 3.1. RECIPES BY CATEGORY ----- #
@app.route("/recipes/<category_name>")
def recipes_categories(category_name):
    """
    Display sub-categories from the category selected previously in the "recipes.html" page
    Search recipes according to a specific sub-category by clicking on this sub-category. 
    """
    # Store the category clicked by the user in a variable
    the_category =  mongo.db.recipes_categories.find_one({"category_name": category_name})
    the_name_category = the_category["category_name"].capitalize()
    return render_template("recipes/recipes_categories.html", 
                            Page_name = the_name_category,
                            Page_title = "RECIPES BY..", 
                            Welcome_image = "../static/img/categories/bg.jpg", 
                            category=the_category, 
                            carousel = image_folder("carousel"))

# ----- 3.2. RECIPES BY SUBCATEGORY ----- #
@app.route("/recipes/<category_name>/<subcategory_name>")
def recipes_subcategories(category_name, subcategory_name):
    """
    Display recipes results according to category and sub-category selected by the user. 
    """
    # Get recipes filtered by the sub-category
    recipes_subcategory_results = mongo.db.recipes_information.find({ category_name: { "$all": [subcategory_name] } })
    recipes_count=recipes_subcategory_results.count()
    return render_template("recipes/recipes_subcategories.html",
                            Page_name = subcategory_name.capitalize(),
                            Page_title = f"{recipes_count} {subcategory_name.capitalize()} Recipes",
                            recipes = recipes_subcategory_results)

# ----- 4. ABOUT ----- #
@app.route("/about")
def about():
    return render_template("general/about.html", 
                            Page_name = "About Us",
                            Page_title = "ABOUT US", 
                            Welcome_image = "../static/img/about/bg.jpg")

# ----- 5. SIGN UP ----- #
@app.route("/signup")
def signup():
    """
    Display a sign up form to create a new user account.
    User can add details and submit the form.
    """  
    # Check if a user is not already logged in to the session
    if "email" in session:
        flash(f"You are logged in as {session['email']}", "white-text green")
        return redirect(url_for('account'))
    form = SignupForm()
    return render_template("general/signup.html",
                            Page_name = "Sign up",
                            Welcome_image = "../static/img/sign/bg.jpg",
                            form=form)

# ----- 5.1. POST / SIGN UP FORM ----- #
@app.route("/insert_user_account", methods=["GET", "POST"])
def insert_user_account():
    """
    Once user have submitted the form, it gets redirected to this function.
    The user details will only be posted to the db as a new account if the email provided is not already linked to an existing account.
    """
    
    if request.method == "POST":
        form = SignupForm()
        # Create a query to the db to filter user accounts with email provided 
        user_accounts = mongo.db.user_accounts
        user = user_accounts.find_one( { "email": form.email.data.lower() })
        logging.info('User account found in MongoDB: {} match the email provided by the user in the form'.format(user))
        # Check if email provided is not already linked to an existing account
        if user:
            flash(f"An account already exists for {form.email.data}.", "white-text red")
            return redirect(url_for("signup"))
        # If no existing account was found user account can be created
        else:
            # Encrypt password
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            # Insert new user account details to the db
            user_accounts.insert_one({
                "first_name": form.first_name.data.lower(),
                "last_name": form.last_name.data.lower(),
                "email": form.email.data.lower(),
                "password": hashed_password,
                "my_recipes": [],
                "favorite_recipes": []
            })
            flash(f"{form.first_name.data.capitalize()}, your account has been created, you can now log in!", "white-text green")
            return redirect(url_for("login"))
    
    return redirect(url_for("signup"))

# ----- 6. LOG IN ----- #
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Display a log in form to enable user to log to his/her account.
    User is required to log in with email and password. 
    """ 
    
    # Check if a user is not already logged in to the session
    if "email" in session:
        flash(f"You are logged in as {session['email']}", "white-text green")
        return redirect(url_for('account'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": form.email.data.lower() })
        logging.info('User found {}'.format(user))
        # Creat user password var only if user object is not empty
        if user:
            user_password = user["password"]
        if user and bcrypt.check_password_hash(user_password, form.password.data):
            # Add user to the session
            session["email"] = user["email"].lower()
            session["first_name"] = user["first_name"].lower()
            session["last_name"] = user["last_name"].lower()
            flash("Login successful!", "white-text green darken-1")
            return redirect(url_for("account"))
        else:
            flash(f"Login unsuccessful! Email and/or password incorrect.", "white-text red")
        
    return render_template("general/login.html",
                            Page_name = "Log In",
                            Welcome_image = "../static/img/sign/bg.jpg",
                            form=form)

# ------------------------------------------- #
#              LOG IN | REQUIRED              #
# ------------------------------------------- #

# ----- ACCOUNT / USER DASHBOARD ----- #
@app.route("/account")
def account():
    """
    Display a personalized user dashboard with different menu options. 
    User can manage his account details, manage his own recipes, create new recipe,
    access his cookbook (with his/her recipes stored as favorites) and finally search
    for more recipes. 
    """
    # Check if the user is logged before rendering the template
    if "email" in session:    
        return render_template("users/account.html",
                                Page_name = "My Account",
                                Page_title = f"Hi {session['first_name'].capitalize()}, welcome!")
    return redirect(url_for('access_denied'))  

# ----- LOG OUT ----- #
@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("email", None)
    session.pop("first_name", None)
    session.pop("last_name", None)
    flash("Thanks for your visit, we hope to see you soon!", "blue-grey lighten-5")
    return redirect(url_for("login"))

# ----- 1. VIEW / USER ACCOUNT DETAILS ----- #
@app.route("/account_details")
def account_details():
    """
    Display a recap of the user account details (First Name, Last Name and Email).
    The user has the option to click a button to edit his/her details and/or password. 
    """
    # Check if the user is logged before rendering the template
    if "email" in session:
        # Create a query to get user information
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })
        return render_template("users/account_details.html",
                                Page_name = "Manage Account",
                                Welcome_image = "../static/img/sign/bg.jpg",
                                account = user)
    return redirect(url_for('access_denied'))

# ----- 1.1. EDIT / ACCOUNT DETAILS ----- #
@app.route("/edit_my_details")
def edit_my_details():
    """
    Display an editable form for the user to amend his/her account details.
    The user can then post a request to update his/her new details by clicking the button form.
    """    
    # Check if the user is logged before rendering the template
    if "email" in session:
        # Create a query to get user information
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })
        return render_template("users/edit_my_details.html",
                                Page_name = "Edit Details",
                                Welcome_image = "../static/img/sign/bg.jpg",
                                account = user)
    return redirect(url_for('access_denied'))

# ----- 1.1.1 UPDATE / ACCOUNT DETAILS ----- #
@app.route("/update_my_details/<account_id>", methods=["POST"])
def update_my_details(account_id):
    """
    Once user have submitted the previous form, it gets redirected to this function.
    The user details will only be updated if the newly provided email is not already linked to an existing account.
    """      
    # Check if email provided is not already linked to an existing account
    user = mongo.db.user_accounts.find_one({ "email": request.form.get("email").lower()})
    if user != None:
        user_first_name = user["first_name"]
        user_last_name = user["last_name"]
        # Exclude the case where the email found is the user logged
        if (user_first_name != session["first_name"]) or (user_last_name != session["last_name"]):
            flash(f"An account already exists for {request.form.get('email')}", "white-text red")
            return redirect(url_for("edit_my_details"))
    else:
        # Update new account details into the db
        mongo.db.user_accounts.update({"_id": ObjectId(account_id)},
                                      {"$set":
                                            {"first_name": request.form.get("first_name").lower(),
                                             "last_name": request.form.get("last_name").lower(),
                                              "email": request.form.get("email").lower()} 
                                      })
        # Update session variable with new account details                             
        session["email"] = request.form.get("email").lower()
        session["first_name"] = request.form.get("first_name").lower()
        session["last_name"] = request.form.get("last_name").lower()
        flash("Your account details have been updated successfully!", "white-text green darken-1")
        return redirect(url_for("account_details"))

# ----- 1.2. EDIT / USER PASSWORD ----- #
@app.route("/edit_password", methods=["POST", "GET"])
def edit_password():
    """
    Display an editable form for the user to change his/her password.
    The user is required to provide existing password, new password and a confirmation of the latest.
    """
    # Check if the user is logged in
    if "email" in session:
        
        form = PasswordForm()
        
        if form.validate_on_submit():
            # Create a query to get user information
            user = mongo.db.user_accounts.find_one( { "email": session["email"] })
            current_user_password_db = user["password"]
            # Check if current password match password stored in the db
            if not bcrypt.check_password_hash(current_user_password_db, form.current_password.data):
                flash(f"Your current password is incorrect!", "white-text red")
            # Check if current password is different from new password 
            if bcrypt.check_password_hash(current_user_password_db, form.new_password.data):
                flash(f"Your new password is not different from your current password.", "white-text red")
            # Check if all conditions to change the password are met   
            if (form.new_password.data == form.confirm_new_password.data) and bcrypt.check_password_hash(current_user_password_db, form.current_password.data):
                # Encrypt new password before storing it
                hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
                # Update new password into MongoDB
                mongo.db.user_accounts.update({ "email": session["email"]},
                                              { "$set":
                                                  { "password": hashed_password }
                                              })
                flash(f"Thanks your password has been updated!", "white-text green")
                return redirect(url_for('account_details'))
            else:
                flash(f"You have to confirm your password. Please make sure the two fields are identical.", "white-text red")
        
        return render_template("users/edit_password.html",
                                Page_name = "Edit Password",
                                Welcome_image = "../static/img/sign/bg.jpg",
                                form=form)
                            
    return redirect(url_for('access_denied'))

# ----- 1.2. DELETE (CONFIRM FORM) / USER ACCOUNT ----- #
@app.route("/delete_account")
def delete_account():
    """
    Display a form for the user to confirm his/her password before account deletion.
    The user is then asked to confirm his/her decision by a 2-tier confirmation modal.
    """    
    # Check if the user is logged before rendering the template
    if "email" in session:
        # Create a query to get user information
        user = mongo.db.user_accounts.find_one({"email": session["email"]})
        return render_template("users/delete_account.html",
                                Page_name = "Delete Account",
                                Welcome_image = "../static/img/sign/bg.jpg",
                                account = user)
    return redirect(url_for('access_denied'))

# ----- 1.2.1. PERMANENTLY DELETE / USER ACCOUNT ----- #  
@app.route("/perm_delete_account/<account_id>", methods=["POST"])
def perm_delete_account(account_id):
    """
    Permanently delete user account after user confirmed his/her decision.
    Check if password provided by the user is correct. 
    """
    user_accounts = mongo.db.user_accounts
    user = user_accounts.find_one({"_id": ObjectId(account_id)})
    current_user_password_db = user["password"]
    # Check if password provided by the user is incorrect
    logging.info('Form is {}'.format(request.form))
    if not bcrypt.check_password_hash(current_user_password_db, request.form.get("password")):
        flash(f"The account has not been deleted because the password provided is incorrect!", "white-text red")
        return redirect(url_for('delete_account'))
    # Check if password provided by the user is correct
    if bcrypt.check_password_hash(current_user_password_db, request.form.get("password")):
        # Delete user account from the db
        user_accounts.remove({"_id": ObjectId(account_id)})
        # Remove user from the session
        session.pop("email", None)
        session.pop("first_name", None)
        session.pop("last_name", None)
        flash("Thanks for your visit but we will miss you :(", "blue-grey lighten-5")
        return redirect(url_for('home'))
    else:
        flash(f"Ooops somthing went wrong! Your account has not been deleted.", "white-text red")
        return redirect(url_for('delete_account'))

# ----- 2. VIEW / MY RECIPES ----- #       
@app.route("/my_recipes")
def my_recipes():
    """
    Display all the recipes that were added by this user.
    The user can edit and/or delete the recipe by clicking on the assigned button.
    """
    # Check if the user is logged in
    if "email" in session:
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })
        # Store recipes added by this user
        my_recipes = user["my_recipes"]
        recipes_number = len(my_recipes)
        
        # Loop through each recipes id and extract information in "recipes_information" collection
        recipes_list_information = []
        for i in range(recipes_number):
            # Create a query to get recipes information based on user list
            recipe_information_i = mongo.db.recipes_information.find_one( { "_id": ObjectId(my_recipes[i]) })
            recipes_list_information.append(recipe_information_i)
            logging.info('For i={}, the recipes information found is {}'.format(i, recipe_information_i))
            
        return render_template("users/my_recipes.html",
                            Page_name = "My recipes",
                            Page_title = "MANAGE RECIPES",
                            Welcome_image = "../static/img/cookbook/bg2.jpg",
                            recipes = recipes_list_information,
                            recipes_number = recipes_number)
    
    return redirect(url_for('access_denied'))

# ----- 2.1. EDIT RECIPE ----- #  
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    """
    Edit recipe selected by the user from the previous menu.
    """
    # Get recipe object based on id of the recipe clicked by the user
    the_recipe =  mongo.db.recipes_information.find_one({"_id": ObjectId(recipe_id)})
    # Create variables to edit recipes
    meal_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'meal' })
    diet_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'diet' })
    occasion_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'occasion' })
    geography_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'geography' })
    allergen_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'allergen' })
    tool_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'tool' })
    # Format prep_time into hours and minutes
    prep_time = the_recipe["prep_time"]
    if prep_time < 60:
        hours = ""
        minutes = prep_time
    else:
        hours = prep_time // 60
        minutes = prep_time % 60
    
    return render_template("recipes/edit_recipe.html",
                            Page_name = "Edit Recipe",
                            meal_categories = meal_categories,
                            diet_categories = diet_categories,
                            occasion_categories = occasion_categories,
                            geography_categories = geography_categories,
                            allergen_categories = allergen_categories,
                            tool_categories = tool_categories,
                            recipe = the_recipe,
                            hours = hours,
                            minutes = minutes,
                            difficulty = ["easy", "medium", "difficult"])

# ----- 2.1.1. UPDATE RECIPE ----- # 
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    """
    Update recipe informations in the db based on form submitted by the user.
    """
    recipes = mongo.db.recipes_information
    # Convert prep_time into minutes
    hours = int(request.form.get("hours"))*60 if request.form.get("hours") else ""
    minutes = int(request.form.get("minutes"))
    prep_time = minutes + hours if hours else minutes
    # Update recipe informations
    recipes.update(
        {'_id': ObjectId(recipe_id) },
        { "$set": { "recipe_name": request.form.get("recipe_name").lower(),
                    "recipe_description": request.form.get("recipe_description").lower(),
                    "serving": int(request.form.get("serving")),
                    "prep_time": prep_time,
                    "difficulty": request.form.get("difficulty"),
                    "occasion": request.form.getlist("occasion"),
                    "geography": request.form.getlist("geography"),
                    "diet": request.form.getlist("diet"),
                    "meal": request.form.getlist("meal"),
                    "ingredients": request.form.getlist("ingredients"),
                    "instructions": request.form.getlist("instructions"),
                    "tool": request.form.getlist("tool"),
                    "allergen": request.form.getlist("allergen"),
                    "image_path": request.form.get("image_path")
                    }
        })
    flash(f"Thanks, the recipe has been updated!", "white-text green")
    return redirect(url_for('recipe_description', recipe_id = recipe_id))

# ----- 2.2. DELETE RECIPE ----- #  
@app.route("/delete_recipe/<recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):
    """
    Delete recipe selected by the user from the previous menu.
    Delete the recipe from the user's recipes list and all users that saved it as a favorite.
    """
    recipes = mongo.db.recipes_information
    user_accounts = mongo.db.user_accounts
    # Get user's ID to link recipe to the logged user
    logged_user = user_accounts.find_one({"email": session["email"]})["_id"]
    # Delete the recipe from the db
    recipes.remove({"_id": ObjectId(recipe_id) })
    # Remove this recipe from the user's field "my_recipes"
    user_accounts.update({"_id": ObjectId(logged_user)},
                         {"$pull": { "my_recipes": ObjectId(recipe_id)}})
    # Remove this recipe for all users that saved it as favorite
    user_accounts.update_many({},
                             {"$pull": { "favorite_recipes": ObjectId(recipe_id)}})
    flash(f"Thanks, your recipe has been successfully deleted!", "white-text green")
    return redirect(url_for('my_recipes'))

# ----- 3. ADD / NEW RECIPE ----- #  
@app.route("/add_recipe")
def add_recipe():
    """
    Display editable form for the user to add new recipe. 
    """
    # Check if the user is logged in
    if "email" in session:
        # Create all the variables required to add recipes
        meal_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'meal' })
        diet_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'diet' })
        occasion_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'occasion' })
        geography_categories = mongo.db.recipes_categories.find_one({ 'category_name': 'geography' })
        allergen_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'allergen' })
        tool_categories = mongo.db.bakery_helpers.find_one({ 'category_name': 'tool' })
        return render_template("recipes/add_recipe.html",
                                Page_name = "Add Recipe",
                                meal_categories = meal_categories,
                                diet_categories = diet_categories,
                                occasion_categories = occasion_categories,
                                geography_categories = geography_categories,
                                allergen_categories = allergen_categories,
                                tool_categories = tool_categories)
    return redirect(url_for('access_denied'))

# ----- 3.1. INSERT / NEW RECIPE ----- # 
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    """
    Add new recipe after user successfully submitted the form, then redirects to user's own recipes list to display the newly added recipe. 
    """
    # Get user's ID to link recipe to the logged user
    logged_user = mongo.db.user_accounts.find_one({ "email": session["email"] })["_id"]
    # Get today's date for recipe
    today = datetime.now().strftime("%Y-%m-%d")
    # Convert prep_time into minutes
    hours = int(request.form.get("hours"))*60 if request.form.get("hours") else ""
    minutes = int(request.form.get("minutes"))
    prep_time = minutes + hours if hours else minutes

    new_recipe = {  "recipe_name": request.form.get("recipe_name").lower(),
                    "recipe_description": request.form.get("recipe_description").lower(),
                    "rates_list":[ ],
                    "serving": int(request.form.get("serving")),
                    "prep_time": prep_time,
                    "difficulty": request.form.get("difficulty"),
                    "occasion": request.form.getlist("occasion"),
                    "geography": request.form.getlist("geography"),
                    "diet": request.form.getlist("diet"),
                    "meal": request.form.getlist("meal"),
                    "ingredients": request.form.getlist("ingredients"),
                    "instructions": request.form.getlist("instructions"),
                    "tool": request.form.getlist("tool"),
                    "allergen": request.form.getlist("allergen"),
                    "recipe_author": logged_user,
                    "recipe_date": today,
                    "image_path": request.form.get("image_path"),
                    "comments_list":[ ]
    }
    
    # Insert recipe information into the db
    mongo.db.recipes_information.insert_one(new_recipe)
     # Get the ID of the newly created recipe
    new_recipe_ID = new_recipe["_id"]
    # Add this recipe to the user's collection "favorite_recipes"
    if request.form.get("is_favorite"):
        mongo.db.user_accounts.update_one({"_id": ObjectId(logged_user)},
                                          {"$push": {"favorite_recipes": new_recipe_ID}})
    # Add this recipe to the user's collection "my_recipes"
    mongo.db.user_accounts.update_one({"_id": ObjectId(logged_user)},
                                      {"$push": {"my_recipes": new_recipe_ID }})
    
    flash(f"Thanks, your recipe was created!", "white-text green")
    return redirect(url_for("my_recipes"))

# ----- 4. VIEW / COOKBOOK ----- #  
@app.route("/cookbook")
def cookbook():
    """
    Display all the recipes that were saved as favorites by this user.
    """
    # Check if the user is logged in
    if "email" in session:
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })
        # Store user's favorite recipes 
        favorite_recipes = user["favorite_recipes"]
        recipes_number = len(favorite_recipes)
        
        # Loop through each recipes id and extract information from "recipes_information" collection
        recipes_list_information = []
        for i in range(recipes_number):
            # Create a query to get recipes information based on user list
            recipe_information_i = mongo.db.recipes_information.find_one( { "_id": ObjectId(favorite_recipes[i]) })
            recipes_list_information.append(recipe_information_i)
            logging.info('For i={}, the recipes information found is {}'.format(i, recipe_information_i))
            
        return render_template("users/cookbook.html",
                            Page_name = "Cookbook",
                            Page_title = "COOKBOOK", 
                            Welcome_image = "../static/img/cookbook/bg.jpg",
                            recipes = recipes_list_information,
                            recipes_number = recipes_number)
    
    return redirect(url_for('access_denied'))

# ----- 5. ADD/REMOVE FAVORITES ----- #

# ----- 5.1. ADD FAVORITES ----- #
@app.route("/recipe/<recipe_id>/add_favorite")
def add_favorite(recipe_id):
    """
    Add recipe to user's favorites and redirect to recipe description page.
    """
    user_accounts = mongo.db.user_accounts
    # Get user's ID to link recipe to the logged user
    logged_user = user_accounts.find_one({"email": session["email"]})["_id"]
    # Remove this recipe from the user's field "favorite_recipes"
    user_accounts.update({"_id": ObjectId(logged_user)},
                         {"$push": { "favorite_recipes": ObjectId(recipe_id)}})
    flash(f"Thanks, this recipe was added to your favorites!", "white-text green")
    return redirect(request.referrer)

# ----- 5.2. REMOVE FAVORITES ----- #
@app.route("/recipe/<recipe_id>/delete_favorite")
def delete_favorite(recipe_id):
    """
    Remove recipe from user's favorites and redirect to recipe description page.
    """
    user_accounts = mongo.db.user_accounts
    # Get user's ID to link recipe to the logged user
    logged_user = user_accounts.find_one({"email": session["email"]})["_id"]
    # Remove this recipe from the user's field "favorite_recipes"
    user_accounts.update({"_id": ObjectId(logged_user)},
                         {"$pull": { "favorite_recipes": ObjectId(recipe_id)}})
    flash(f"Thanks, this recipe was removed from your favorites!", "white-text green")
    return redirect(request.referrer)

# ------------------------------------------- #
#              RECIPES RESULTS                #
# ------------------------------------------- #

# ----- ALL RECIPES PAGE ----- #
@app.route("/results")
def results():
    """
    Display all the recipes stored in the db.
    """
    recipes = mongo.db.recipes_information.find()
    recipes_number=recipes.count()
    return render_template("recipes/results.html",
                            Page_name = "All Recipes",
                            Page_title = f"{recipes_number} RECIPES",
                            recipes=recipes,
                            recipes_number = recipes_number)

# ----- VIEW / RECIPE DESCRIPTION ----- #
@app.route("/recipe/<recipe_id>")
def recipe_description(recipe_id):
    """
    Display recipe informations after user clicked on the image card from the results page.
    """
    # Check if the user is logged in
    if "email" in session:
        # Create a query to get the user stored in the user variable
        user = mongo.db.user_accounts.find_one( { "email": session["email"] })    
        # Store user's favorite recipes
        favorite_recipes = user["favorite_recipes"]
    else:
        favorite_recipes = ""

    # Get recipe object based on id of the recipe clicked by the user
    the_recipe =  mongo.db.recipes_information.find_one({"_id": ObjectId(recipe_id)})
    the_recipe_name = the_recipe["recipe_name"].capitalize()
    # Format prep_time into hours and minutes
    prep_time = the_recipe["prep_time"]
    if prep_time < 60:
        hours = ""
        minutes = prep_time
    else:
        hours = prep_time // 60
        minutes = prep_time % 60
    return render_template("recipes/recipe_description.html", 
                            Page_name = the_recipe_name,
                            recipe = the_recipe,
                            user_favorites = favorite_recipes,
                            hours = hours,
                            minutes = minutes,
                            carousel = image_folder("carousel"))

# ------------------------------------------- #
#               SPECIAL PAGES                 #
# ------------------------------------------- #

# ----- 404 PAGE ----- #
@app.errorhandler(404)
def page_not_found(e):
    """
    Display a customized page for 404 error.
    """
    return render_template("general/404.html",
                            Page_name = "404"), 404

# ----- ACCESS DENIED PAGE ----- #
@app.route('/access_denied')
def access_denied():
    """
    Display a customized denied access page for pages that require to be logged in.
    """ 
    return render_template("general/access.html",
                            Page_name = "Access Denied")

# ---------------- #
#      RUN APP     #
# ---------------- #

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)