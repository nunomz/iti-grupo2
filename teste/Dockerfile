# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY templates templates

COPY app.py .

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]