# start by pulling the python image

FROM python:3.10-slim-buster

WORKDIR /python-docker
RUN source /root/dataenv/bin/activate
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3.10", "-m" , "flask", "run", "--host=0.0.0.0"]