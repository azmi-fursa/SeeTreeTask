from flask import render_template
import numpy as np
from functions import calc_pixel_features
from functions import readImageFromFileURL
from configuration import URL
from configuration import app
from configuration import host
from configuration import port

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

    
if __name__ == '__main__':    
    app.run(host, port , debug=False)
