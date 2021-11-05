import requests
import time
from flask import Flask, render_template, request, g
import numpy as np
from PIL import Image

URL = "https://storage.googleapis.com/seetree-demo-open/"

#functiontion to read and turn RGB image to grayscale image (if the image is available)
def readImageFromFileURL(imageFileURL):
    check_response = requests.get(imageFileURL, stream=True).raw
    try:
        img1 = Image.open(check_response)
    except Exception as e:
        return render_template('Error.html', msg='Bad image file name!')
    return img1.convert('L')

def calc_pixel_features(name, function, numpy_grayscale):    
    percent = function[1:]
    if function == 'min':
        value = str(np.min(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        #return 'The minimum value of the image (' + name + ') is : ' + value, value
        return statement
    
    elif function == 'max':
        value = str(np.max(numpy_grayscale))
        statement = 'Maximum value of (' + name + ') is: ' + value
        #return 'The maximum value of the image (' + name + ') is : ' + value, value
        return statement
    
    elif function == 'mean':
        value = str(np.mean(numpy_grayscale))
        statement = 'Mean value of (' + name + ') is: ' + value
        #return 'The mean value of the image (' + name + ') is : ' + value, value
        return statement
    
    elif function == 'median':
        value = str(np.median(numpy_grayscale))
        statement = 'Minimum value of (' + name + ') is: ' + value
        #return 'The median value of the image (' + name + ') is : ' + value, value
        return statement
    
    elif function[0] == 'p' and percent.isnumeric() and int(percent) in range(0,101):
        value = str(np.percentile(numpy_grayscale, int(percent)))
        statement = 'The ' + str(percent) + '% percentile value of the image (' + name + ') is : ' + value
        #return 'The ' + str(percent) + '% percentile value of the image (' + name + ') is : ' + value, value
        return statement
    else:
        return "none"
    
    
app = Flask(__name__)


@app.errorhandler(404)
def error(e):
    return render_template("Error.html")


@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/health')
def health():
    return render_template('Health.html')


@app.route('/Functions/<IMAGE_FILE_NAME>', methods=['GET'])
def functions(IMAGE_FILE_NAME):
    return render_template('Functions.html', IMAGE_FILE_NAME=IMAGE_FILE_NAME)


@app.route('/stats/<IMAGE_FILE_NAME>/<function_NAME>', methods=['GET'])
def calc_stats(IMAGE_FILE_NAME,function_NAME):
    grayscale = readImageFromFileURL(URL + IMAGE_FILE_NAME)
    numpy_grayscale = np.array(grayscale)
    value = calc_pixel_features(IMAGE_FILE_NAME, function_NAME, numpy_grayscale)
    print(value)
    if (value == "none"):
        return render_template('Error.html', msg='Requested function is not suppported!')
    return render_template('Statistics.html', value = str(value), IMAGE_FILE_NAME=IMAGE_FILE_NAME)

    
    

    
app.run(host='0.0.0.0', port=8080 , debug=False)
