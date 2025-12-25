#!/usr/bin/env bash
set -o errexit

echo "== Install requirements =="
pip install -r requirements.txt

echo "== Migrate =="
python manage.py migrate --no-input

echo "== Collectstatic =="
python manage.py collectstatic --no-input

echo "== Seed (if empty) =="
python manage.py seed_if_empty

echo "== Ensure superuser =="
python manage.py ensure_superuser

echo "== Build done =="
