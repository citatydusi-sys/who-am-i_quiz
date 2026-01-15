#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --no-input

# Import data
python manage.py import_data

# Collect static files
python manage.py collectstatic --no-input --clear
