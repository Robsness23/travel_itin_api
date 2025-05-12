from . import db
from datetime import datetime

class User(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(128), nullable = False)

class Itinerary(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

class Activity(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    time = db.Column(db.Time)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary_id'), nullable = False)
    