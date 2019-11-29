import os

# print(image_folder('carousel'))
def image_folder(folder):
    list_of_image = []
    for filename in os.listdir('static/img/'+folder):
        if filename.endswith(".jpg"):
            list_of_image.append(os.path.join('static/img/'+folder+'/'+ filename))
        else:
            continue
    return list_of_image



