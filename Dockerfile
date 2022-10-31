# start by pulling the python image
FROM python:3.8-alpine

# create directory rootapp
RUN mkdir /rootapp

# copy the requirements file into the image
COPY ./requirements.txt /rootapp/requirements.txt

# switch working directory
WORKDIR /rootapp

# install the dependencies and packages in the requirements file
#RUN pip install -r requirements.txt

# copy every content from the local file to the image

COPY . /rootapp

# configure the container to run in an executed manner
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]