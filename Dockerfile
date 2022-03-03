# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app


RUN echo "SECRET_KEY = 'django-insecure-_^39%)wfp910i*)2!2+ihrxbnrv$&44nm#pv-yf!7&mqhbgnkz'" > .env


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
