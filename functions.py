import requests
from flask import render_template
import numpy as np
from PIL import Image

database = {"IMAGE_FILE_NAME": { }}

#function to read and turn RGB image to grayscale image (if the image is available)
def try_open_image(imageFileURL):
    is_valid = requests.get(imageFileURL, stream=True).raw
    try:
        img = Image.open(is_valid).convert('L')
    except Exception:
        return "error"
    return img

    
def calc_pixel_features(name, function, numpy_grayscale):    
    if name in database:
        if function in database[name]:
            statement = 'The ' + function + ' value of the image ('+name+') is : ' + database[name][function]
            return render_template('Statistics.html', value=str(statement), name=name)
    percent = function[1:]
    if function == 'min':
        value = str(np.min(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        return statement,value
    
    elif function == 'max':
        value = str(np.max(numpy_grayscale))
        statement = 'Maximum value of (' + name + ') is: ' + value
        return statement,value
    
    elif function == 'mean':
        value = str(np.mean(numpy_grayscale))
        statement = 'Mean value of (' + name + ') is: ' + value
        return statement,value
    
    elif function == 'median':
        value = str(np.median(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        return statement,value
    
    elif function[0] == 'p' and percent.isnumeric() and int(percent) in range(0,101):
        value = str(np.percentile(numpy_grayscale, int(percent)))
        statement = 'The ' + str(percent) + '% percentile value of the image (' + name + ') is : ' + value
        return statement,value
    else:
        return "none","none"


def redundant_calculations(name,function):
    if name in database:
        if function in database[name]:
            return database[name][function]
    return "better luck next time"


def update_database(name,function,value):
    if name not in database:
        database.update({name: {function: str(value)}})
    elif function not in database[name]:
        database[name].update({function: str(value)})
