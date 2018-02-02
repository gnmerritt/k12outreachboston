#!/bin/bash
# run this via 'docker exec django /src/setup.sh'
set -e
cd "$(dirname "$0")"

echo "Running setup script"

python manage.py loaddata users.json
