# start by pulling the python image
FROM python:3.8-alpine

# create directory app
RUN mkdir /rootapp

# set or make /app our working directory
WORKDIR /rootapp

# copy all files to /app
COPY ./ /rootapp


# configure the container to run in an executed manner
CMD ["flask", "run", "--host=0.0.0.0"]