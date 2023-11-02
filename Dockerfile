FROM python:3.9-alpine

WORKDIR /forestfire-main

COPY . /application

RUN pip install -r requirements.txt

CMD [ "python3","application.py" ]