#!/bin/bash
port=8000
fuser -k $port/tcp
python manage.py runserver $port