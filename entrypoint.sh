#!/bin/bash

# Wait for PostgreSQL to be ready
if [ -n "$DB_HOST" ]; then
  echo "Waiting for PostgreSQL..."
  
  # Install netcat if not available
  which nc >/dev/null || apt-get update && apt-get install -y netcat-openbsd
  
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