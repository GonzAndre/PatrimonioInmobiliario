 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 RUN apt-get update
 #RUN apt-get install -y mysql-client
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/