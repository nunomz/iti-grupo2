# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

#WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000
#VOLUME files:files

COPY templates templates
COPY server.py . 
    #if possible create app folder in host and copy that instead!!

CMD [ "python3", "server.py"]