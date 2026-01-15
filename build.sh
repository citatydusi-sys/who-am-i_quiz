#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Starting build process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate --no-input

# Import data
echo "Importing quiz data..."
python manage.py import_data

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "Build completed successfully!"
