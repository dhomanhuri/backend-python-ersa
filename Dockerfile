# start by pulling the python image

FROM python:3.10-slim-buster


WORKDIR /python-docker
RUN apt-get update && apt-get install -y opencv-python-headless
RUN pip install opencv-python-headless
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]