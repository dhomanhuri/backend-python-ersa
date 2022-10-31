# start by pulling the python image
FROM python:3.8-alpine


WORKDIR /python-docker


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]