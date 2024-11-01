from . import db
from datetime import datetime

class Concert(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    venue = db.Column(db.String(200))
    date = db.Column(db.String(15))
    time = db.Column(db.String(15))
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