# Image Pixel Statistics:

## Motivation and Goals:
AI is an expanding field in the industry, in this application we will learn how to extract interesting features about images and how to calculate Image Statistics.
Images are made out of multiple pixels, each pixel has a grayscale level in the range "0 - 255", where 0 is black and 255 is white. 
The goal of this application is to implement functions that help us extract statistics about multiple images and their pixels, these functions include: 
min, max, mean, median and percentile.
i) min is the minimum pixel value of grayscale level in the image
ii) max is the maximum pixel value of grayscale level in the image
iii) mean is the mean pixel value of grayscale level in the image
iv) median is the median pixel value of grayscale level in the image
v) percentile: the user may decide what percentile (range [0-100]) of the image he/she would like to be presented from the image\


The images are stored in a Cloud Storage Bucket, and in order to access these images we will have to send a GET request to the following API:  https://storage.googleapis.com/seetree-demo-open/.  

There are 10 images in the api labeled "IMG_i.jpg" - where i is in the range [1:10]. To access the 4th image for instance, we will need to go to : https://storage.googleapis.com/seetree-demo-open/IMG_4.jpg

## Error URLs:
When trying to access invalid URLs we must present relevant error pages:\
i)if the image is not presented in the given API, if we try to reach http://localhost:8080/Functions/IMG_22.jpg for instance (IMG_22.jpg isn't available), the user is presented with the following error page:
![image](https://user-images.githubusercontent.com/91056755/140619970-a8e8c473-e0cc-4811-b216-74d675facc8b.png)

ii)if the image is present, yet the function isn't supported by the application (avg function for instance), when trying to access http://localhost:8080/stats/IMG_3.jpg/avg the user is presented with the following error page:
![image](https://user-images.githubusercontent.com/91056755/140619985-3b7dae5d-cee3-4653-b1df-7102da43e139.png)

## Calculation Method:

*In order to calculate the desired image statistics, we must first turn our RGB image into a grayscale image, we can easily do that using python's libraries (PIL) and the function ```convert(L)```\
*After turning the image into a grayscale image, now we can view the level of gray in each pixel as a histogram in the range (0:255).\
*To calculate each of the required functions, we can use python's "numpy" library which supports all the desired functionality.

## HTML pages:
We use the render_template to align the work of python with the HTML pages easily. we first create a simple HTML template for each page and implement the python output through render_template.

## Bonus Section:
Many requests are redundant, therefore we must think of a way to spare ourselves from calculating problems which we already faced and calculated. (redundant problems are problems that include the same image and the same function as a previously calculated request)\
The solution is to create a database for each image that includes all the functions: When an image is presented with a function that it hadn't calculated before, we calculate the desired function and add it to the image's database, whereas when we are faced with a previously calculated function we automatically return the previous calculation./
lets view it by code:/
i created a database for each image with the following command: ```database = {"IMAGE_FILE_NAME": { }}``` , if both the image and the function aren't present, we update the database with this command: ```database.update({name: {function: str(value)}})``` , if the image is present yet the function isn't: ```database[name].update({function: str(value)})``` .

# Getting Started:
To work with the application, you must first make sure to install all these prerequisites (if you haven't already):\
i) Flask, in order to install: ```apt install python3-flask``` \
ii) Docker Desktop - to install, follow the instructions here : https://docs.docker.com/desktop/windows/install/ \
iii) Python, to install, follow instructions: https://www.python.org/downloads/ \
iv) Finally, you need to have GIT installed on your terminal. I strongly suggest working with "Git Bash", to download: https://git-scm.com/downloads \

Now that you have everything you need to work with the app, follow these simple steps to access the application: \

## To use the application locally with flask:
i) ```git clone https://github.com/azmi-fursa/SeeTreeTask.git```\
ii) ```cd SeeTreeTask``` \
iii) ```pip install requirements.txt``` \
iv) ```python routes.py```

## To use the application locally with Docker:
i) ```git clone https://github.com/azmi-fursa/SeeTreeTask.git```\
ii) ```cd SeeTreeTask``` \
iii) ```docker build -t pixelstatistics .``` \
iv) ```docker run -itdp 8080:8080 pixelstatistics``` \

Voila! you are ready to go, access the application through: http://localhost:8080/ , you will be directed to this webpage: \

![image](https://user-images.githubusercontent.com/91056755/140619905-68ca3dc0-ff1e-4cd1-ac03-072a6e18f5dd.png)

