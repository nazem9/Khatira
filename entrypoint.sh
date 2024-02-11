#!/bin/bash

# Wait for other services to be ready (e.g., databases) before starting
echo "Waiting for backend service to be ready..."
until nc -z backend 8000; do
  sleep 1
done
echo "Backend service is ready!"

echo "Waiting for frontend service to be ready..."
until nc -z frontend 3000; do
  sleep 1
done
echo "Frontend service is ready!"

# Run any migrations or setup scripts if needed
# e.g., python manage.py migrate

# Start the Nginx service
echo "Starting Nginx..."
nginx -g "daemon off;"
