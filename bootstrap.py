from flask import Flask, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("Library")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/python'
db = SQLAlchemy(app)