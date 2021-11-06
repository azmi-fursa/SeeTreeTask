from flask import render_template
import numpy as np
from configuration import URL
from configuration import app
from configuration import host
from configuration import port
from functions import calc_pixel_features
from functions import update_database
from functions import try_open_image
from functions import redundant_calculations

#handling invalid URLs.
@app.errorhandler(404)
def error(e):
    return render_template("Error.html")

#redirecting to the home page
@app.route('/')
def home():
    return render_template('HomePage.html')

#health page, here you can view tips on how to live a healthy lifestyle
@app.route('/health')
def health():
    return render_template('Health.html')

#choosing required image's functionality
@app.route('/Functions/<IMAGE_FILE_NAME>', methods=['GET'])
def functions(IMAGE_FILE_NAME):
    image = URL + IMAGE_FILE_NAME
    var = try_open_image(image)
    if(var=="error"):
        return render_template('Error.html', msg='Bad image file name!')
    return render_template('Functions.html', IMAGE_FILE_NAME=IMAGE_FILE_NAME)

@app.route('/stats/<IMAGE_FILE_NAME>/<function_NAME>', methods=['GET'])
def calc_stats(IMAGE_FILE_NAME,function_NAME):
    check_database = redundant_calculations(IMAGE_FILE_NAME,function_NAME)
    if(check_database!="better luck next time"):
        return check_database
    image = URL + IMAGE_FILE_NAME
    grayscale = try_open_image(image)
    numpy_grayscale = np.array(grayscale)
    statement,value = calc_pixel_features(IMAGE_FILE_NAME, function_NAME, numpy_grayscale)   
    update_database(IMAGE_FILE_NAME,function_NAME,value)    
    if (value == "none"):
        return render_template('Error.html', msg='Requested function is not suppported!')
    return render_template('Statistics.html', value = str(statement), IMAGE_FILE_NAME=IMAGE_FILE_NAME)

    
if __name__ == '__main__':    
    app.run(host, port , debug=False)
