import os
from flask import request
from flask_paginate import Pagination, get_page_parameter

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
def pagination_function(recipes):
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipes_number = recipes.count()
    pagination = Pagination(page=page, total=recipes_number, search=search, record_name='recipes')
    return pagination



