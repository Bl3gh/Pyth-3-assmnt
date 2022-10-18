import requests
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:09889099@localhost:4444/python'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Nft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    
    def addToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkInDb(cls, nft_address):
        return cls.query.filter_by(address = nft_address).first()
