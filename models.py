### STEP ONE: Create Database and model -- while setting up the project, add the DEBUG TOOLBAR IN app.py
"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMG_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)