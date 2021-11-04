FROM python:3.8.5

#mkdir templates + cd templates
WORKDIR /templates

COPY templates .

WORKDIR /app

COPY requirements.txt .

#installing requirements to the image
RUN pip install -r requirements.txt

#copying the python code
COPY code.py .

#app is now available on port 8080
EXPOSE 8080

#run python code in the docker image
CMD ["python","/app/code.py"]
