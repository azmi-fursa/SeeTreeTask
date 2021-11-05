FROM python:3.8.5

#mkdir app + cd app
WORKDIR /app

COPY templates .

COPY requirements.txt .

#installing requirements to the image
RUN pip install -r requirements.txt

#copying the python code
COPY code.py .

#run python code in the docker image
CMD ["python","/app/code.py"]
