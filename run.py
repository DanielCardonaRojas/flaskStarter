#!venv/bin/python
from app import app
import subprocess

if __name__ == '__main__':
	# subprocess.Popen(["venv/bin/celery -A app.celery worker --pidfile=/tmp/celery.pid --beat --concurrency=10"], stdout=subprocess.PIPE, shell=True)
	app.run(host='0.0.0.0', threaded=True, debug = True)

