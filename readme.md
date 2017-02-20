# Getting Started With Flask (Mega Tutorial)

This is an attempt to get a basic scaffold for flask apps, it includes SQLAlchemy and Celery.

Just note talking on Flask Mega Tutorial by Miguel.

Download Python3 (with Brew)

Create application folder and cd into it

Create a virtual environment and install flask in it (python3)
```shell
python3 -m venv flask
```

To avoid the upgrade recomendation

> flask/bin/pip install --upgrade pip

Run the app with `./run.py`


[flask-wtf](https://flask-wtf.readthedocs.io/en/stable/) -> Forms
flask-sqlalchemy -> ORM

###Cheatsheet

source the virtual environment
```shell
source <venv_name>/bin/activate
```

Write down all dependencies to requirements.txt file and install them
```shell
pip freeze > requirements.txt
pip install -r requirements.txt
```

Run celery with beat embeded in workers 
```shell
celery -A app.celery worker --beat -E -l INFO
```


#Using Celery

Choose a broker
====

Install and run redis 

```shell
brew install redis
redis-server
#You'll also need to 
pip install redis
```

Install and run rabbitmq
```shell
brew install rabbit
/usr/local/sbin/rabbitmq-server
```

Install and run celery
```shell
pip -U install Celery
celery worker -l info --beat
#OR
celery -A your_application.celery worker
```
All celery flags can be found [here](http://docs.celeryproject.org/en/latest/genindex.html)

Notes: 

Had problems installing covarageo package


