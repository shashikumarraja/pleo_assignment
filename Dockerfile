FROM python:latest
RUN apt-get update -y
RUN apt-get install -y vim 
WORKDIR /src
RUN pip install -r requirements.txt
STOPSIGNAL SIGINT