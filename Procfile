web: gunicorn vidhaan.wsgi:application --log-file -
release:python manage.py makemigrations 
release:python manage.py collectstatic 
release:python manage.py migrate
