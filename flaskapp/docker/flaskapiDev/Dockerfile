FROM python:3.5

WORKDIR /app

ENV FLASK_DEBUG=1
ENV FLASK_APP=main.py
CMD pip3 install -r requirements.txt && flask run --host=0.0.0.0
EXPOSE 5000