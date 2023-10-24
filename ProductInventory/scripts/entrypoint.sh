#!/bin/sh

# wait for db
./wait-for-db.sh

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# start the Django app
gunicorn ProductInventory.wsgi:application --bind 0.0.0.0:8000
