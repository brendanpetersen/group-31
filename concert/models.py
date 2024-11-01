from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='user')

    def __repr__(self):
        return f"Name: {self.name}"

class Concert(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    venue = db.Column(db.String(200))
    date = db.Column(db.String(15))
    time = db.Column(db.String(15))
    price = db.Column(db.Float)
    comments = db.relationship('Comment', backref='concert', lazy=True)

    def __repr__(self):
        return f"Concert(name={self.name})"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    concert_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return f"Comment(id={self.id}, text={self.text})"

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    concert_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    date = db.Column(db.String(15), nullable=False)
    time = db.Column(db.String(15), nullable=False)
    event_title = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    num_guests = db.Column(db.Integer, default=1)

    user = db.relationship('User', backref='bookings')
    concert = db.relationship('Concert', backref='bookings')

    def __repr__(self):
        return f"<Booking {self.event_title} on {self.date} at {self.time}>"