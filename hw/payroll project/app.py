from flask import Flask, render_template, request, redirect, url_for, session
import csv
from blackjack import Card, Deck, Player, Game
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'dfghjiouhgdashswevnohshshshidnasiodn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Employee(db.Model):
	idi = db.Column(db.Integer, unique=True, nullable=False, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    pswrd = db.Column(db.String(80), nullable=False)
    ssn = db.Column(db.Integer, unique=True, nullable = False)
    salary = db.Column(db.Long, nullable = False)
    is_paid = db.Column(db.Boolean, nullable = False)
    benefits
    attendance = db.Column(db.Long, nullable = False)
    rating = db.Column(db.Long, nullable = False)