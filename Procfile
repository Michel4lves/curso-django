release: pipenv run python manage.py migrate --no-input
web: gunicorn cursodjango.wsgi --log-file -