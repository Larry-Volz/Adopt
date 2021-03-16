from flask_sqlalchemy import SQLAlchemy
import datetime
"""Models for Adopt"""

db=SQLAlchemy()
def connect_db(app):
    db.app = app 
    db.init_app(app)


class Pet(db.Model):
    """ Pet/pets Model for Adopt  application for pet adoptions """
    __tablename__ = 'pets'

    def __repr__(self):
           return f"id={self.id} name={self.name}"  #for better referencing

    id = db.Column(db.Integer,
    primary_key = True,
    autoincrement = True)

    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = True)
    photo_url = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default=True)



