#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations UserApp
python manage.py makemigrations PostApp
python manage.py makemigrations ProfileApp
python manage.py migrate
