#pulling python image
FROM python:3.8.5

#copying HTML files and downloading requirements
COPY templates /templates/
COPY requirements.txt ./
RUN pip install -r requirements.txt

#copying the python code to the image
COPY functions.py .
COPY routes.py .
COPY configuration.py .

#run python code in the docker image and expose the output to port 8080
EXPOSE 8080
CMD python routes.py
