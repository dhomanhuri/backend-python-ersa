# start by pulling the python image

FROM python:3.10-slim-buster

WORKDIR /python-docker
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN flask run --host 0.0.0.0