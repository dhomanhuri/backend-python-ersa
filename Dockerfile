# start by pulling the python image
FROM python:3.8-alpine


WORKDIR /python-docker

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

RUN pip install opencv-python
RUN pip install flask
RUN pip install python-dotenv==0.21.0
RUN pip install SQLAlchemy==1.4.41
RUN pip install Werkzeug==2.2.2

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]