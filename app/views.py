from flask import render_template, flash, redirect
from flask import jsonify
from app import app, celery
from .forms import LoginForm

from datetime import timedelta

# from celery.decorator import periodic_task

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Daniel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'DaNiel'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Emiliano'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'Coco'}, 
            'body': 'Discovering new tooling' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/test', methods=['GET', 'POST'])
def test():
    res = add_task.delay(3,4)
    print (res.ready())
    return jsonify({"name":"Prueba", "passed":False})


@celery.task()
def add_task(x,y):
    print ("adding values:  " + str(x) + " " +  str(y))
    return (x + y)

# @periodic_task(run_every=timedelta(seconds = 5))
def say_hi(x,y):
    print("Hi there!!")
    return "Hola"



