FROM python:3.8.5
COPY templates /templates/
COPY requirements.txt ./
RUN pip install -r requirements.txt

#copying the python code
COPY code.py .

EXPOSE 8080
#run python code in the docker image
CMD python code.py
