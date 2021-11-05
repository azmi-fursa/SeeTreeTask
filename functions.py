import requests
from flask import render_template
import numpy as np
from PIL import Image


#function to read and turn RGB image to grayscale image (if the image is available)
def readImageFromFileURL(imageFileURL):
    check_response = requests.get(imageFileURL, stream=True).raw
    try:
        img1 = Image.open(check_response)
    except:
        return render_template('Error.html', msg='Bad image file name!')
    return img1.convert('L')

def calc_pixel_features(name, function, numpy_grayscale):    
    percent = function[1:]
    if function == 'min':
        value = str(np.min(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        return statement
    
    elif function == 'max':
        value = str(np.max(numpy_grayscale))
        statement = 'Maximum value of (' + name + ') is: ' + value
        return statement
    
    elif function == 'mean':
        value = str(np.mean(numpy_grayscale))
        statement = 'Mean value of (' + name + ') is: ' + value
        return statement
    
    elif function == 'median':
        value = str(np.median(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        return statement
    
    elif function[0] == 'p' and percent.isnumeric() and int(percent) in range(0,101):
        value = str(np.percentile(numpy_grayscale, int(percent)))
        statement = 'The ' + str(percent) + '% percentile value of the image (' + name + ') is : ' + value
        return statement
    else:
        return "none"
