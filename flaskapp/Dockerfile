FROM python:3.5

WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt

ENV FLASK_DEBUG=1
ENV FLASK_APP=main.py
CMD flask run --host=0.0.0.0
EXPOSE 5000