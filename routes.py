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
    return render_template("ErrorPaths.html")

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
        return render_template('ErrorPaths.html', msg='Bad image file name!')
    return render_template('PixelFunctionalities.html', IMAGE_FILE_NAME=IMAGE_FILE_NAME)

@app.route('/stats/<IMAGE_FILE_NAME>/<function_NAME>', methods=['GET'])
def calc_stats(IMAGE_FILE_NAME,function_NAME):
    check_database = redundant_calculations(IMAGE_FILE_NAME,function_NAME)
    if(check_database!="better luck next time"):
        if(function_NAME[0]=='p'):
            percent = function_NAME[1:]
            statement = 'The ' + str(percent) + '% value of the image (' + IMAGE_FILE_NAME + ') is : ' + check_database
        else:
            statement = 'the ' + function_NAME + ' value of (' + IMAGE_FILE_NAME + ') is: ' + check_database
        return render_template('Calculations.html', value = str(statement), IMAGE_FILE_NAME=IMAGE_FILE_NAME)
    image = URL + IMAGE_FILE_NAME
    grayscale = try_open_image(image)
    numpy_grayscale = np.array(grayscale)
    value = calc_pixel_features(IMAGE_FILE_NAME, function_NAME, numpy_grayscale)   
    update_database(IMAGE_FILE_NAME,function_NAME,value)    
    if (value == "none"):
        return render_template('ErrorPaths.html', msg='Requested function is not suppported!')
    if(function_NAME[0]=='p'):
        percent = function_NAME[1:]
        statement = 'The ' + str(percent) + '% value of the image (' + IMAGE_FILE_NAME + ') is : ' + value
    else:
        statement = 'the ' + function_NAME + ' value of (' + IMAGE_FILE_NAME + ') is: ' + value
    print(statement)
    return render_template('Calculations.html', value = str(statement), IMAGE_FILE_NAME=IMAGE_FILE_NAME)

    
if __name__ == '__main__':    
    app.run(host, port , debug=False)
