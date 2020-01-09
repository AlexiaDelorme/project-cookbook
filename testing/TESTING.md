
1. Automated Testing
    - Code quality
    - Jasmine
    - Python Testing
2. User Stories Testing
3. Compatibility & Responsiveness
    - Desktop 
    - Tablet and mobile devices
4. Known issues
    - Solved 
    - Unsolved

# Automated Testing

## Code quality

##### HTML5

HTML files were passed through this [HTML code validator](https://validator.w3.org/) at the exception of errors related to the use of jinja templating language that is currently not recognized by the code validator. You can see below a screenshot of these recurring errors:

![HTML5 Code Validator Errors](validators/html-errors.png)

##### CSS3

My style.css file succesfully passed this [CSS code validator](https://jigsaw.w3.org/css-validator/).

![CSS Code Validator](validators/css3.png)

##### JS

My JS file was passed through [JS Hint](https://jshint.com/), please find below the information provided by the code validator. 

**Metrics:**
- There are 12 functions in this file. 
- Function with the largest signature take 1 arguments, while the median is 0.
- Largest function has 10 statements in it, while the median is 1.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.

**Warnings:**
- Arrow function syntax `=>` is only available in ES6 (use 'esversion: 6').

**1 undefined variable:**
- `swal` (used 4 times for Sweet Alert)

**3 unused variables:**
- `myPrintFunction` (function is invoked when print button is clicked)
- `deleteRecipeFunction`(function is invoked when delete recipe button is clicked)
- `deleteAccountFunction` (function is invoked delete account button is clicked)

![JS Hint](validators/js.png)

##### Python

## Jasmine

## Python

# User Stories Testing

This project has been tested multiple times against each user stories previously listed in the UX section. 

## External users

###### Testing user story 1 

**User story:** As an external user, I want to make use of the site and benefit from having convenient access to the data provided by all community members.

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navigation bar.
- [x] Leave the explore recipes form blank from any filters and click on the `SEARCH RECIPES` button.
- [x] You should have a total number of "x" recipes. TO BE UPDATED
- [x] Click on any of the recipes and you should be able to access the recipe description page without restriction.

**Test result:** Successful :white_check_mark:

###### Testing user story 2

**User story:** As an external user, I want to be able to research recipes based on specific criteria and have a visually appealing and interactive interface while I am cooking. 

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navigation bar.
- [x] In the explore recipes form, select "vegan" in the `Diet` field. 
- [x] Check that the recipes that are presented to you are indeed vegan. You can do so by performing random checks on some recipes, check that these recipes are flagged as vegan in the recipe description or check the recipe ingredients as well. 

**Test result:** Successful :white_check_mark:

###### Testing user story 3

**User story:** As an external user, I also want to be able to browse recipes by category types (meal, diet, occasion or geography) and then have a list of all the recipes available for the category I selected. 

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `RECIPES` menu item in the navigation bar. You should be presented with the 4 following recipe categories:
    - occasion
    - geography
    - diet
    - meal
- [x] Click on the `Diet` category. You should be presented with the following diet categories:
    - vegan
    - vegetarian
    - gluten-free
    - sugar-free
    - lactose-free
- [x] Select the `Vegan` diet. You should have the same recipes list as for test case 2. 
- [x] Perform the same checks for other categories and sub-categories. 

**Test result:** Successful :white_check_mark:

###### Testing user story 4

**User story:** As a user with specific constraints (food allergies, specific diets or simply missing a cooking tool…), I want to be able to find recipes that address my needs and be presented recipes based on my inputs.

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navigation bar.
- [x] In the explore recipes form, set the following criteria for your search:
    - `Recipe Difficulty`-> "Medium"
    - `Max Serves`-> "5"
    - `Preparation Time`-> "< 1 hour"
    - `Diet`-> "Gluten-free" & "Lactose-free"
    - `Allergens`-> exclude: "Gluten", "Soy" & "Peanuts"
    - `Tools`-> exclude: "Blender", "Oven" & "Microwave"
- [x] You should have (at least) the following recipe: "Chestnut pancakes (gf)"
- [x] Get back to the form and then select "Eggs" as allergen. Then resubmitt your request.
- [x] The "Chestnut pancakes (gf)" recipe should have disappeared from the results as it contains eggs.

**Test result:** Successful :white_check_mark:

###### Testing user story 5

**User story:** As an external user, I want to be able to view the recipe instructions for all the recipes available in the database with the same level of details as a community member. I also want to be recommended some of the website creators' favorite recipes.  

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Following the same steps from the previous test scenario, click on the "Chestnut pancakes (gf)"
- [x] Check that the following information are available in the recipe description:
    - recipe name 
    - serving size
    - diet 
    - difficulty
    - preparation time
    - button to share the recipe on social media
    - button to print the recipe
    - recipe picture
    - recipe description (if any)
    - ingredients list
    - cooking tools
    - preparation setps
    - carousel displaying recommended recipes

**Test result:** Successful :white_check_mark:

###### Testing user story 6

**User story:** As an external user, I want to be able to share recipes on different social platforms as well as be able to print them. 

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Get back to the previous test case scenario. 
- [x] On the recipe description, click on the "share" button just above the recipe picture.
- [x] A modal form should open with the list of social media icons on which it's possible to share the recipe.
- [x] Click on each icon to check if a new window opens to share the recipe on the corresponding media platform. Remember that you have to be logged in on the social media to be able to view the recipe post. 
- [x] Get back to the recipe description and click on the "print" button just next to the "share" button. 
- [x] A preview print window should open displaying all the relevant information that pertain to the recipe.

**Test result:** Successful :white_check_mark:

###### Testing user story 7

**User story:** As an external user, I want to be able to create a free account with minimal steps.

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `SIGN UP` menu item in the navigation bar.
- [x] Fill all the required information: First Name, Last Name, Email, Password and Confirm Password. Click the `SIGN UP` button. 
- [x] If you provided a valid email address and successfully confirmed your password, your account should have been created and you should have been redirected to the log in page. 

**Test result:** Successful :white_check_mark:

## Community members

###### Testing user story 1

**User story:** As a community member, I want to be able to log in with minimal steps by only using my email and password for authentication. I also want to be able to log out easily.

**Hypothesis:** The user should already have registered to an account. 

**Test scenario:**
- [x] Click on the `LOG IN` menu item in the navigation bar.
- [x] Provide your email and password then click the `LOG IN` button. 
- [x] If you provided a valid email address and a correct password, you should be logged in and redirected to a personalized dashboard.
- [x] On the right of the navigation bar, you should now view a button to `LOG OUT`. Click this button and you should now be back to the Log In page.

**Test result:** Successful :white_check_mark:

###### Testing user story 2

**User story:** As a community member, I want to be able to edit my information details, password and delete my account permanently if necessary.

**Hypothesis:** The user should be logged in to perform this test. 

**Test scenario:**
- [x] After being logged in to your account, on your account dashboard, click on `Manage Account`.
- [x] You should view your account details via an non-editable form (First Name, Last Name, Email address).
- Edit account details
    - [x] Click on the `EDIT DETAILS` button. You should now be able to view an editable form.
    - [x] Amend your First Name, Last Name, Email address and click on the `EDIT ACCOUNT` button.
    - [x] You should be able to view your new account details. 
- Edit password
    - [x] Click on the `EDIT PASSWORD` button. You should now be able to view a form to amend your password. 
    - [x] Enter your current password, choose a new password and then confirm it, finally click on the `UPDATE PASSWORD` button.
    - [x] Your password should be updated. Log out and test logging in with this new password. 
- Delete account
    - [x] Get back to your account details page. At the bottom of the page below the `EDIT PASSWORD` button and above the footer, there should be a small paragraph saying "You want to delete your account? Click Here". Click on the `Here`anchor tag.
    - [x] Confirm your password and then press the `DELETE ACCOUNT` button. 
    - [x] A modal form should appear asking you to confirm your decision. Press the `Delete` button.
    - [x] You should be logged out and a message should confirm you that your account was deleted. 
    - [x] Try to log in with the previous credentials to check if your account has indeed been deleted.

**Test result:** Successful :white_check_mark:

###### Testing user story 3

**User story:** As a community member, I want to be able to create new recipes and then have the possibility to edit and/or to delete any of the recipes that I have shared with the community.

**Hypothesis:** The user should be logged in to perform this test. 

**Test scenario:**
- Add new recipe
    - [x] After being logged in to your account, on your account dashboard, click on `Add new recipe`.
    - [x] You should view a form to add a new recipe. Fill in all the madatory fields that are highlighted with a red star and then click on the `ADD RECIPE` button at the bottom of the form.
    - [x] If you filled in the form correctly, you should see a message confirming that your recipe was added succesfully. 
- Edit recipe
    - [x] Get back to your account dashboard and click on `Manage recipes`.
    - [x] You should have a list of recipe cards for all the recipes you have added. Choose the last recipe you just created and click the `EDIT` button. 
    - [x] You should view an editable form, pre-filled with the information of the recipe. Amend several fields such as the recipe name, recipe difficulty, serving size, add some ingredients etc... Click on the `EDIT RECIPE` button.
    - [x] Check that the amendments done to the recipe are now reflected in the recipe description.
- Delete recipe
    - [x] Get back to your account dashboard and click on `Manage recipes`.
    - [x] Delete your test recipe by clicking on the `DELETE` button. 
    - [x] A modal form should appear asking you to confirm your decision. Press the `Delete` button.
    - [x] A message should confirm you that your recipe was deleted. It should no longer be visible in your menu `Manage recipes`. 

**Test result:** Successful :white_check_mark:

###### Testing user story 4

**User story:** As a community member, I want to be able to add/remove a recipe to my favorites so I can create my own online cookbook. 

**Hypothesis:** The user should be logged in to perform this test. 

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navbar, leave the form blank and then click on `SEARCH RECIPES` so you get all the recipes.
- [x] Pick one recipe that is currently not in your cookbook, click on the recipe to access its description.
- Add to favorites
    - [x] At the bottom of the recipe description, just above the carousel, you should see "Save as favorite?" as well as a pulse icon. 
    - [x] Click on the heart pusle icon to add the recipe as favorite.
    - [x] You should view a message confirming that the recipe was added to your favorites.
    - [x] Click on the `COOKBOOK` menu item to access your favorite recipes and double-check that the recipe was added.
- Remove from favorites
    - [x] Get back to the previous recipe that is now part of your cookbook.
    - [x] Go back to the bottom of the recipe description, you should now see "Remove from favorites?" with a pulse icon.
    - [x] Click on the bin pusle icon to remove the recipe from your favorites.
    - [x] You should view a message confirming that the recipe was removed from your favorites.
    - [x] Get back to your cookbook and check that the recipe was indeed removed.

**Test result:** Successful :white_check_mark:

###### Testing user story 5

This user story is out of testing scope.

## The site owners

These user stories are out of testing scope.

# Compatibility & Responsiveness

A cross browser testing was performed for each user stories scenario to ensure that all functionalities render well in different browsers:
- Safari
- Google Chrome
- Mozilla Firefox
- Internet Explorer
- Opera 

The responsiveness of the webiste was tested thanks to Google Chrome developer tool, the following devices size were tested and all elements were displayed without issued:
- Galaxy S5 
- Pixel 2 / Pixel 2 XL 
- iPhone 5/SE / iPhone X 
- iPhone 6/7/8 and Plus
- iPad / iPad Pro 

# Known Issues

* xxx
* xxx
* xxx