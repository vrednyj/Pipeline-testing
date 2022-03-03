#!/bin/bash

os_packages="git python3.9 python3.9-venv python3-pip "

echo "======= Installing OS Packages =============="
apt update -y
apt install $os_packages -y

echo "======= Activating venv and installing requirements =============="
python3.9 -m venv venv && source venv/bin/activate &&  pip3.9 install -r requirements.txt

echo "======= Exporting key to .env file =============="

echo "SECRET_KEY = 'django-insecure-_^39%)wfp910i*)2!2+ihrxbnrv$&44nm#pv-yf!7&mqhbgnkz'" > .env


echo "======= Starting DJANGO Application  =============="

source venv/bin/activate && python3.9 manage.py runserver 0.0.0.0:8000

