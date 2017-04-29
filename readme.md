# Flask Scaffold

Sets up a proyect for python2.7 with login functionality  and celery configuration ready. 

## Setup

Create application folder and cd into it

Create sqlite3 database

```shell
sqlite3 app.db
#Or
sqlite3
#Then
.open app.db
```

Create a virtual environment and install flask in it
```shell
virtualenv venv
```

Run the app with `./run.py`


## Install dependencies


```shell
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install flask
pip install flask-SQLAlchemy
pip install flask-login
pip install Celery
```

## Run migrations

Create the users table from the User object model
```shell
cd app
export FLASK_APP=$PWD/__init__.py
echo $FLASK_APP
flask shell
```

From shell
```python
form app import db
#Run all migrations
db.create_all()
```

## Cheatsheet

Source the virtual environment
```shell
source <venv_name>/bin/activate
```

Write down all dependencies to requirements.txt file and install them
```shell
pip freeze > requirements.txt
pip install -r requirements.txt
```


## Creating Users

```shell
#Create a user
curl --data "user_name=admin&user_passwd=admin" http://localhost:5000/create_user
curl --data "user_name=admin&user_passwd=admin&user_mail=dcardona@grupodyd.com" http://localhost:5000/create_user
```


## Celery Configuration

Run celery with beat embeded in workers 
```shell
celery -A app.celery worker --beat -E -l INFO
```

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

## Deployment with NGINX and uWSGI

```shell
sudo apt-get install nginx
sudo apt-get install uwsgi
sudo apt-get install uwsgi-plugin-python
```

### Configure interactive repl for project

```shell
pip install flask-shell-bpython

#START THE SHELL LIKE THIS
export FLASK_APP=<path_to_your_project>/app/__init__.py
flask shell
#Then from the interactive shell
from app.views import *
from app.models import *
```


TODO:

- Test Flask-migrate, flask-admin
- Add logger to app
- Manage log directories
