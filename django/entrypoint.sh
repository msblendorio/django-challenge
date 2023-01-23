#!/bin/bash
set -e

cd /code/challenge

echo "Running with mode $MODE"
export DJANGO_SETTINGS_MODULE="main.settings.$MODE"

if [ ${MODE} = "development" ]; then 
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
fi

if [ ${MODE} = "staging" ]; then 
    python manage.py migrate
    gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers=3
fi
