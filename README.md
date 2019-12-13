<div align="center">
    <img src="https://i.ibb.co/qMDnM0y/logo.jpg" href="https://patisserie-cookbook.herokuapp.com" target="_blank" alt="The Pâtisserie Journal Logo" />
</div> 

# [The Pâtisserie Journal](https://patisserie-cookbook.herokuapp.com)

Welcome!

[The Pâtisserie Journal](https://patisserie-cookbook.herokuapp.com) is an intuitive online cookbook tool to help you find new recipes and implement them interactively while cooking. You can also share your own recipes by creating an account and join our onlince community!

The purpose of this project is to make patisserie inclusive meaning that anyone with food allergies, specific diet or simply missing an ingredient or a cooking tool would be able to find a suitable recipe. 

By creating a community that can share their own recipes, it will enable us to naturally expand our database but also promote new "chefs" by providing them with visibility. 

## Table of Contents
1. [UX](#UX)
    - [User Stories](#)
        - [External Users](#)
        - [Site Owners](#)
    - [Design](#)
    - [Wireframes](#)
    - [Flowchart](#)

2. [Features](#)
    - [Current Features](#)
    - [Future Features](#)

3. [Database](#)
    - [Database choice](#)
    - [Data Structure](#)

4. [Technologies Used](#)

5. [Testing](#)

6. [Deployment](#)
    - [Heroku Deployment](#)
    - [Local Deployment](#)

7. [Credits](#)
    - [Content](#)
    - [Media](#)
    - [Code](#)
    - [Acknowledgements](#)

# UX

## User Stories

For this project, I identified the following stakeholders:
-	External users
-	Community members
-	The site owners

### External users

###### User story 1
 
As an external user, I want to make use of the site and benefit from having convenient access to the data provided by all community members.

###### User story 2

As an external user, I want to be able to research recipes based on specific criteria and have a visually appealing and interactive interface while I am cooking. 

###### User story 3

As an external user, I also want to be able to browse recipes by category types (meal, diet, occasion or geography) and then have a list of all the recipes available for the category I selected. 

###### User story 4

As a user with specific constraints (food allergies, specific diets or simply missing a cooking tool…), I want to be able to find recipes that address my needs and be presented recipes based on my inputs.

###### User story 5

As an external user, I want to be able to view the recipe instructions for all the recipes available in the database with the same level of details as a community member. I also want to be recommended some of the website creators' favorite recipes. 

###### User story 6

As an external user, I want to be able to share recipes on different social platforms as well as be able to print them. 

###### User story 7

As an external user, I want to be able to create a free account with minimal steps.

### Community members

###### User story 1

As a community member, I want to be able to log in with minimal steps by only using my email and password for authentication. I also want to be able to log out easily.

###### User story 2

As a community member, I want to be able to edit my information details, password and delete my account permanently if necessary.

###### User story 3

As a community member, I want to be able to create new recipes and then have the possibility to edit and/or to delete any of recipes that I have shared with the community.

###### User story 4

As a community member, I want to be able to add/remove a recipe to my favourites so I can create my own online cookbook. 

###### User story 5

Food lovers, wannabe cooks or anyone passionate about patisserie who wants to try out the success of their recipes.

### Site's owner

###### User story 1

Generally speaking we promote a cooking tool and benefit from the collection of the dataset as whole. 

###### User story 2

Be the first member of this community to share my own patisserie recipes!

###### User story 3

Building a full-stack website using Python and mini-framework Flask that allows me to apply my skills in databases handling and interactive design. 

## Design

## Wireframes

- Balsamiq wireframe

## Flowchart

# Features

## Current Features

#### Features for all users

###### Feature 1 - Home page
Any external user landing to the home page of this website will be presented with a general welcome page with the following features:
- Navigation bar with a logo and links to the different pages: Home, Explore, Recipes, About, Sign Up and Log In.
- Recipes teaser and a direct link to explore recipes directly by clicking on the headline.
- Short presentation of the online cookbook and a direct link to register by clicking on the "Join Us" headline.
- A direct link to the "About Us" section of the website.
- A footer with icon links to the following social media: Facebook, Instagram, YouTube, Pinterest, and Twitter (no actual account created as this is for education purpose only). 

###### Feature 2 - Search recipes
- The user can search for recipes by filtering on any criteria provided within the form.
- The user can filter recipes based on the following criteria:
    - recipe difficulty
    - preparation time (selection)
    - max serving (direct input or increment arrow)
    - meal category (multiple selection allowed)
    - diet category (multiple selection allowed)
    - exclude allergens (multiple selection allowed)
    - exclude specific tools (multiple selection allowed)
    - occasion (multiple selection allowed)
    - geography (multiple selection allowed)
- The user has the possibility to leave some fields blank, this will not prevent the form from being submitted. The criteria for which the field was left blank will simply be disregarded. 
- Once the form is succesfully submitted, the user is presented with a list of the recipes matching his criteria. The user is provided with the number of recipes matching his search, and can click any recipe cards (with recipe name and a small picture) and will be redirected to the recipe description. 

###### Feature 3 - Recipes categories
- Users who are looking for inspiration or would like to search for recipes based on specific categories can actually do so.
- After clicking on the "Recipes" menu item in the navigation bar, the user is first presented with 4 general categories to "sort" recipes:
    - occasion
    - geography
    - diet
    - meal
- After selecting one of the previous categories, the user can then choose to sort the recipes by sub-categories as follow:
    - occassion: Christmas, New Year's, Weddings...
    - geography: North America, Asia...
    - diet: Vegan, Vegeterian...
    - meal:Breakfast, Snacks...
- Once the user clicked the desired sub-category, he is then presented with a list of all the recipes matching his category and sub-category selection. The user can click on any recipe cards (with recipe name and a small picture) and will be redirected to the recipe description. 

###### Feature 4 - About Us Page
- The user can learn more about the purpose of this website.
- The user is provided with "fast-track" links to recipes, cookbook and sign in pages. 

###### Feature 4 - Sign Up Page
- Any external user can join the community by creating a new account with us.
- The user is provided with a simple sign up form requiring only basic information: First Name, Last Name, Email and Password (and confirmation).
- Before any account is created, the email provided by the user will be checked to ensure that an existing account is not already link to this email. 
- The user is provided with relevant feedback (flashed messages at the top of the page) if any field is missing or if any information provided is incorrect.
- The user password is hashed for security purposes.
- Once the user succesfully created his account, he is then redirected to the log in page for authentication. 

###### Feature 4 - Log In Page
- The user will only need to enter his email and password for authentication and authorization.
- The hashed version of the password provided by the user will be checked with the password saved in the database. 
- The user is provided with a feedback "login unsuccessful..." (red flashed message at the top of the page) if the email and/or password provided are incorrect. 
- Once the user succesfully logged in to his account, he gets a green flashed message saying "login successful!" and is redirected to his account dashboard.

###### Feature 5 - Recipe Page Description
[C**R**UD] - **R**ead
Be it as a result of the "explore" recipes form or of the "recipes" categories section, the user will be able to view the following information:
- recipe name and description (if any)
- serving size
- diet compatibility
- difficulty
- preparation time
- ingredients list
- cooking tools
- preparation setps
The user will also have the following additional options:
- button to share the recipe on a wide range of social media
- button to print the recipe
- option to check out the website creators' favorite recipes

#### (Additional) Features for community members

###### Feature 5 - Account Dashboard
- xxx
- xxx

###### Feature 6 - Online Cookbook
- xxx
- xxx

###### Feature 7 - CRUD for Recipes
- xxx
- xxx

###### Feature 7 - Add/Remove Favorites
- xxx
- xxx

## Future Features

Please find below the list of improvements I would like to add to this project:

###### Future Feature 1 - description here
- xxx
- xxx
- xxx

###### Future Feature 2 - description here
- xxx
- xxx
- xxx

# Technologies Used

##### [Balsamiq](https://balsamiq.com/) 
- I used Balsamiq to design my wireframes after drawing them manually.

##### [Cloud9](https://c9.io)
- I used AWS Cloud9 as my code editor for the project.

##### [HTML5](https://www.w3.org/TR/html/)
- I used HTML for creating the static content of my webpage.
- The following [code validator](https://validator.w3.org/) was used to test my HTML code.

##### [CSS3](https://www.w3.org/Style/CSS/)
- I used CSS to style my webpage and personalize it.  
- The following [code validator](https://jigsaw.w3.org/css-validator/) was used to test my CSS code.

##### [Materialize](https://bootswatch.com/lux/)
- I used Materialize as the main framework for HTML.

##### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [jQuery](https://jquery.com/) was used to simplify the DOM manipulation based on the user input via the modal form or when the reset button is clicked.
- [JSHint](https://jshint.com/) was used to check my JS code quality.

##### [Picasa](https://picasa.google.com/)
- I used Picasa to resize and change the orientation of my background image.

##### [ImageOptim](https://imageoptim.com/mac)
- I used ImageOptim to optimize the size of my background image and wireframes. 

##### [Font Awesome](https://origin.fontawesome.com/)
- I used Font Awesome to display icons for the footer of my page.

##### [Git & GitHub](https://github.com/)
- I used Git for version control. 
- I used GitHub to store my code in a remote repository, deploy and host my website.

# Testing 

All the documentation regarding the testing of this project can be found in this [TESTING.md](testing/TESTING.md) file.

# Deployment

## Heroku

## Local Deployment

# Credits

### Content
- xxx
- xxx
- xxx 

### Media
- xxx
- xxx
- xxx

### Code
- xxx
- xxx
- xxx

### Acknowledgements
- xxx
- xxx
- xxx