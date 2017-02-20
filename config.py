import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CELERY_BROKER_URL='redis://localhost:6379'
# CELERY_BROKER_URL = "amqp://localhost:5672/"

# resul_backend ='redis://localhost:6379'
CELERY_RESULT_BACKEND='redis://localhost:6379'
# CELERY_RESULT_BACKEND = "amqp://localhost:5672/"

CELERYBEAT_SCHEDULE = {
        'some-function-every-10-seconds':{
            'task':'tasks.someFunction',
            'schedule': timedelta(seconds=10)
        }
}
