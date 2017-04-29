# coding: utf-8

from app import app, db

import os
#flask related imports
from flask import render_template, request, jsonify, send_from_directory, send_file, session, redirect, g
import flask
from flask_login import  login_required
from jinja2 import Environment, FileSystemLoader, PackageLoader

from models import *

# import requests, json

import ConfigParser
import logging

# import custom_decorators
# from custom_decorators import *

################################### CONFIGS #####################################
# Read print_processor.conf configuration file
Config = ConfigParser.ConfigParser()
Config.read("view.conf")

logLevel = 10
logPath = ""


# CREATE LOGGER
logger = logging.getLogger("garex")
logger.setLevel(int(logLevel))
logEfLevel = logger.getEffectiveLevel()
filehandler = logging.FileHandler(os.path.join(logPath,'garex.log'),'a')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

logger.debug('Garex server: STARTED')

# tracer = LogDecorator(logger)


############################# REQUEST HANDLERS ############################
@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')



@app.route('/admin')
@login_required
def admin():

	return render_template('admin.html')



@app.route('/info', methods= ['POST','GET'])
def info():
	return {"status":"ok", "data":{"name":"garex", "version": "0.0.1"}}


