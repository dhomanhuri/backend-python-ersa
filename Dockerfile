# start by pulling the python image
FROM python:3.8-alpine

COPY app.py .
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "server:app"]