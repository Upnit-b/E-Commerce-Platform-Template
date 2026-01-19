#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn e_commerce.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
