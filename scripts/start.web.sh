#!/bin/sh

# check if Postgres is working before applying migrations and starting the Django development server
if [[ "$DATABASE" = "postgres" ]]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASES_HOST $DATABASES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py load_init_db_data
python manage.py collectstatic --no-input --clear
gunicorn core.wsgi -b 0.0.0.0:8000
