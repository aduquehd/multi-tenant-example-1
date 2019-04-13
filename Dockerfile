FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get install libxml2-dev libxmlsec1-dev libxmlsec1-openssl
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py migrate_schemas