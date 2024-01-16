import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from app import db

class Appliance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(30), nullable=False)
    sku = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    manufacturing_date = db.Column(db.DateTime, default=datetime.datetime.now)

