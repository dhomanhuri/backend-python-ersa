# start by pulling the python image
FROM python:3.8-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

# RUN pip install -r requirements.txt

# Bundle app source
COPY . .

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]