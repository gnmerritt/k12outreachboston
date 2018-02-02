#!/bin/bash
set -e
cd "$(dirname "$0")"

python manage.py makemigrations
python manage.py migrate
gunicorn outreach.wsgi \
  --workers 2 \
  -b 0.0.0.0:8000
