python manage.py collectstatic --no-input

python manage.py migrate

web: gunicorn --worker-tmp-dir /dev/shm djangocrm.wsgi