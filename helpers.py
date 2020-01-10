import os
from flask import request
from flask_paginate import Pagination, get_page_args

# print(image_folder('carousel'))
def image_folder(folder):
    list_of_image = []
    for filename in os.listdir('static/img/'+folder):
        if filename.endswith(".jpg"):
            list_of_image.append(os.path.join('static/img/'+folder+'/'+ filename))
        else:
            continue
    return list_of_image

# Set up pagination for recipes results - Code credit: https://pythonhosted.org/Flask-paginate/
def pagination_function(query_recipes):
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    number_to_skip = (page-1)*per_page
    recipes = query_recipes.skip(number_to_skip).limit(per_page)
    recipes_number = query_recipes.count()
    pagination = Pagination(page=page, total=recipes_number, search=search, record_name='recipes')
    return {"pagination": pagination, 
            "recipes": recipes, 
            "recipes_number": recipes_number}

