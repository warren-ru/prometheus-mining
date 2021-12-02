FROM python:3.8-slim

RUN apt update && apt install webhook

RUN pip3 install --no-cache PyP100

RUN mkdir -p /app

RUN adduser --system --home /app app && addgroup app && adduser app app

#COPY ./app /app

#RUN chown -R app:app /app

USER app

WORKDIR /app

CMD webhook -hooks hooks.yml -verbose
