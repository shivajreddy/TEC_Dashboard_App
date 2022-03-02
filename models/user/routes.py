from app import app, application
from flask import jsonify, render_template,redirect, request
from models.user.User import User
from database.mongodb.mongodb import db

@app.route('/signup/')
def signup():
  return render_template('user_signup.html')


@app.route('/createuser/', methods=["POST"])
def createuser():

  new_user = User().signup()
  return new_user