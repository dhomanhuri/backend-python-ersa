# start by pulling the python image
FROM python:3.8-alpine

WORKDIR /rootapp
COPY . /rootapp
# RUN pip --no-cache-dir install -r requirements.txt
CMD ["python3", "server.py"]