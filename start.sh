RUN flask db init
RUN flask db migrate
RUN flask db upgrade
sudo docker build -t imgpro-app:latest .
sudo docker run -d -p 5000:5000 --name imgpro imgpro-app:latest
