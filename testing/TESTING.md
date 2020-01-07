
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

HTML files succesfully passed this [HTML code validator](https://validator.w3.org/) by direct input as per screenshot provided down below.

![HTML5 Code Validator](link)

##### CSS3

style.css file succesfully passed this [CSS code validator](https://jigsaw.w3.org/css-validator/) by direct input as per screenshot provided down below.

![CSS Code Validator](link)

##### Python

##### JS

JS hint

## Jasmine

## Python

# User Stories Testing

This project has been tested multiple times against each user stories previously listed in the UX section. 

## External users

###### Testing user story 1 

***User story:** As an external user, I want to make use of the site and benefit from having convenient access to the data provided by all community members.

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navigation bar.
- [x] Leave the explore recipes form blank from any filters and click on the `SEARCH RECIPES` button.
- [x] You should have a total number of "x" recipes. TO BE UPDATED
- [x] Click on any of the recipes and you should be able to access the recipe description page without restriction.

**Test result:** Successful :white_check_mark:

###### Testing user story 2

***User story:** As an external user, I want to be able to research recipes based on specific criteria and have a visually appealing and interactive interface while I am cooking. 

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `EXPLORE` menu item in the navigation bar.
- [x] In the explore recipes form, select "vegan" in the `Diet` field. 
- [x] Check that the recipes that are presented to you are indeed vegan. You can do so by performing random checks on some recipes, check that these recipes are flagged as vegan in the recipe description or check the recipe ingredients as well. 

**Test result:** Successful :white_check_mark:

###### Testing user story 3

***User story:** As an external user, I also want to be able to browse recipes by category types (meal, diet, occasion or geography) and then have a list of all the recipes available for the category I selected. 

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

***User story:** As a user with specific constraints (food allergies, specific diets or simply missing a cooking tool…), I want to be able to find recipes that address my needs and be presented recipes based on my inputs.

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

***User story:** As an external user, I want to be able to view the recipe instructions for all the recipes available in the database with the same level of details as a community member. I also want to be recommended some of the website creators' favorite recipes.  

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

***User story:** As an external user, I want to be able to share recipes on different social platforms as well as be able to print them. 

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

***User story:** As an external user, I want to be able to create a free account with minimal steps.

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] Click on the `SIGN UP` menu item in the navigation bar.
- [x] Enter all the required information: First Name, Last Name, Email, Password and Confirm Password. Click the `SIGN UP`button. 
- [x] If you provided a valid email address and succesfully confirmed your password, your account should have been created and you should have been redirected to the log in page. 

**Test result:** Successful :white_check_mark:

## Community members

## The site owners

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