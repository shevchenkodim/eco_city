# pull official base image
FROM python:3.10.0-alpine

# set environment variables
# PYTHONUNBUFFERED means Python won't try to create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED makes sure our console output looks familiar and is not buffered by Docker
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/usr/src/app

# create the appropriate directories
RUN mkdir $APP_HOME $APP_HOME/staticfiles $APP_HOME/mediafiles
WORKDIR $APP_HOME

# adding of requirements.txt
ADD ./requirements.txt $APP_HOME/

# Update and install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg\
    && apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev libffi-dev openssl-dev make\
    && pip install psycopg2 \
    && pip install --upgrade pip\
    && pip3 install -U lazy-object-proxy==1.4.3

# copy backend script
COPY ./scripts/start*.sh /

# run pip install
RUN pip install -r requirements.txt

# copy backend project
ADD . $APP_HOME/