release: python manage.py migrate
web: gunicorn edusphere.wsgi:application --bind 0.0.0.0:$PORT