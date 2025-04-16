#!/bin/bash

# Wait for PostgreSQL to be ready
if [ -n "$DATABASE_URL" ]; then
  # Install netcat if not available
  apt-get update && apt-get install -y netcat-openbsd

  echo "Waiting for PostgreSQL..."
  
  while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
  done
  
  echo "PostgreSQL started"
fi

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Populate data if needed
if [ "$POPULATE_DATA" = "true" ]; then
  echo "Populating initial data..."
  python manage.py populate_data
fi

# Start server
echo "Starting server..."
exec "$@"