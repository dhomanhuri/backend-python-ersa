# start by pulling the python image

FROM python:3.10-slim-buster

WORKDIR /python-docker
RUN apt-get update && apt-get install -y python3-opencv
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN flask run --host 0.0.0.0