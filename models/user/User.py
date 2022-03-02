import uuid
from flask import jsonify, request
from werkzeug.security import generate_password_hash
from database.mongodb.mongodb import db

class User:

  def signup(self):

    new_user = {
      "_id" : uuid.uuid4().hex,
      "name" : request.form['name'],
      "email" : request.form['email'],
      "password" : request.form['password']
    }

    # Encrypt password
    new_user["password"] = generate_password_hash(new_user["password"])

    # check if same email
    if db.users.count_documents({"email":request.form["email"]}) > 0:
      print("XXX same email XXX")
      return jsonify(new_user), 500

    # add to database
    db.users.insert_one(new_user)

    return jsonify(new_user), 200
