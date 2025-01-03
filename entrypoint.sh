#!/bin/bash
echo "Running custom entrypoint script..."

# Check if the database is initialized
if [ -f "/var/lib/postgresql/data/PG_VERSION" ]; then
  echo "Database already initialized. Applying migrations..."
  for file in /docker-entrypoint-initdb.d/*.sql; do
    echo "Applying migration: $file"
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$file"
  done
else
  echo "Initializing database..."
fi

# Start PostgreSQL
exec docker-entrypoint.sh postgres
