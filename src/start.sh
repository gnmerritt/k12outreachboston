#!/bin/bash
set -e
cd "$(dirname "$0")"

HOST_IP=`/sbin/ifconfig eth0 | awk '/t addr:/{gsub(/.*:/,"",$2);print$2}'`

source ../venv/bin/activate
source PROD_ENV.sh

python manage.py migrate --settings=outreach.prod_settings
gunicorn --env DJANGO_SETTINGS_MODULE=outreach.prod_settings \
  --workers 2 \
  --pid outreach-gunicorn.pid \
  -b ${HOST_IP}:8000 \
  outreach.wsgi
