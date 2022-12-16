from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, Boolean, select
from sqlalchemy import text

"""
----- CREATE TABLE IN DATABASE IN TERMINAL-----
flask shell
from app import db
db.create_all()
"""

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/debt_database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = 'product'
    
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text)
    price = db.Column(db.Integer)
    category = db.Column(db.String(255))
    
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category


class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(8))

    # Create relationship
    transactions = db.relationship('Invoice', backref='transactions_table')

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

class Transactions(db.Model):
    __tablename__ = 'transactions_table'
    
    id_trns = db.Column('id_trns', db.Integer, primary_key=True)
    id_customer = db.Column(db.Integer, db.ForeignKey('customer_table.id_customer'))
    date = db.Column(db.Date)
    debt_amount = db.Column(db.Integer)
    remark = db.Column(db.Text)
    is_paid = db.Column(db.Boolean, default=False)
    
    def __init__(self, id_customer, date, debt_amount, remark):
        self.id_customer = id_customer
        self.date = date
        self.debt_amount = debt_amount
        self.remark = remark
        self.is_paid = False

@app.route('/users', methods=['GET', 'POST'])
def adf():
    a = [
        {"id": 1,  "name": "food"},
        {"id": 2,  "name": "mouse"},
        {"id": 3,  "name": "drink"},
        ]
    return a

@app.route('/invoice', methods=['POST'])
def aaa():
    a = [
        {"id": 1,  "name": "food"},
        {"id": 2,  "name": "mouse"},
        {"id": 3,  "name": "drink"},
        ]
    return a



app.run()
