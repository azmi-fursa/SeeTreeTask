# Image Pixel Statistics:

## Motivation and Goals:
AI is an expanding field in the industry, in this application we will learn how to extract interesting features about images and how to calculate Image Statistics.
Images are made out of multiple pixels, each pixel has a grayscale level in the range "0 - 255", where 0 is black and 255 is white. 
The goal of this application is to implement functions that help us extract statistics about multiple images, and their pixels; these functions include: 
min, max, mean, median and percentile. 

The images are stored in a Cloud Storage Bucket, and in order to access these images we will have to send a GET request to the following api:  https://storage.googleapis.com/seetree-demo-open/.

There are 10 images in the api labeled "IMG_i.jpg" - where i is in the range 1:10. To access the 4th image for instance, we will need to go to : https://storage.googleapis.com/seetree-demo-open/IMG_4.jpg

## Calculation Method:

*In order to calculate the desired image statistics, we must first turn our RGB image into a grayscale image, we can easily do that using python's libraries (PIL)
*After turning the image into a grayscale image, now we can view the level of gray in each pixel as a histogram in the range (0:255).
*To calculate each of the required functions, we can use python's "numpy" library which supports all the desired functionality.

## HTML pages:
We use the render_template to align the work of python with the HTML pages easily. we first create a simple HTML template for each page and implement the python output through render_template.

## Bonus Section:
Many requests are redundant, therefore we must think of a way to spare ourselves from calculating problems which we already faced and calculated.
(redundant problems are problems that include the same image and the same function as a previously calculated request)

The solution is to create a database for each image that includes all the functions: When an image is presented with a function that it hadn't calculated before, we calculate the desired function and add it to the image's database, whereas when we are faced with a previously calculated function we automatically return the previous calculation. 

# Getting Started:
To work with the application, you must first make sure to install all these prerequisites (if you haven't already):
1)Flask, in order to install: ```apt install python3-flask``` 
2)Docker Desktop - to install, follow the instructions here : https://docs.docker.com/desktop/windows/install/
3)Python, to install, follow instructions: https://www.python.org/downloads/
4) and lastly, you need to have GIT installed on your terminal. I strongly suggest working with "Git Bash", to download: https://git-scm.com/downloads

Now that you have everything you need to work with the app, follow these simple steps to access the application:
1)git clone https://github.com/azmi-fursa/SeeTreeTask.git
2)cd SeeTreeTask
3)docker build -t imagestatistics .
4)docker run -itdp 8080:8080 imagestatistics

Voila! you are ready to go, access the application through: http://localhost:8080/ , you will be directed to this webpage:

![image](https://user-images.githubusercontent.com/91056755/140448754-48cd6377-434c-4dcb-802a-b14e7192716a.png)

