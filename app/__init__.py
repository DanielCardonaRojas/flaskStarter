from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# celery = Celery()
# celery.config_from_object('celeryconfig')

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)
# celery.conf.celerybeat_schedule = {
    # 'add-every-30-seconds': {
        # 'task': 'tasks.someFunction',
        # 'schedule': 5.0
    # },
# }

from app import views, models
import tasks

