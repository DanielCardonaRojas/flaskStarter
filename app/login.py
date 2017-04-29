# coding: utf-8
from app import app, db
from models import *
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        userName = request.form['user_name']
        userPass = request.form['user_passwd']
        userEmail = request.form['user_mail'] if 'user_mail' in request.form else None

        user = User.query.filter_by(username=userName).first()
        if user:
            if check_password_hash(user.password, userPass):
                login_user(user, remember=True)
                return redirect(url_for('admin'))

        return render_template( 'login.html'
                , background_image = "1.jpg"
                , invalid_message = u'Usuario o contraseña incorrectos')

    return render_template('login.html', background_image = "1.jpg")

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == "POST":
        userName = request.form['user_name']
        userPass = request.form['user_passwd']
        userEmail = request.form['user_mail'] if 'user_mail' in request.form else None

        hashed_password = generate_password_hash(userPass, method='sha256')
        new_user = User(username=userName, email=userEmail, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"status":"Ok", "message":"User created succesfully"})

    return jsonify({"status":"Error", "message":"Supply user_name and user_passwd"})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
