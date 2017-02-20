#!flask/bin/python
from app import app
import subprocess

# subprocess.Popen(["flask/bin/celery -A celery.app worker --app=app.celery --pidfile=/tmp/celery.pid --beat"], stdout=subprocess.PIPE, shell=True)
subprocess.Popen(["flask/bin/celery -A app.celery worker --pidfile=/tmp/celery.pid --beat --concurrency=10"], stdout=subprocess.PIPE, shell=True)
app.run(debug=True)
