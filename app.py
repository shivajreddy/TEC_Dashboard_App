import os

from flask import Flask, request, render_template, redirect, url_for
from database.mongodb.mongodb import db, users_collection


#! App entry point
project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)



#! Routes
@app.route('/')
def index():
  print(os.getcwd())
  dir = [os.getcwd(),2,3]
  return render_template('homepage.html', dir=dir)

@app.route('/test/')
def test_page():
  return "<h1> TEST PAGE ⚙️ </h1>"



application = app

@application.route('/wtf/')
def wtf():
  return "<h1>wtf</h1>"

#! User Routes
import models.user.routes
