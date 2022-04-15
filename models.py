"""Models for Adopt."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import backref

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False)
    species = db.Column(db.String(50),
                    nullable=False)
    photo_url = db.Column(db.Text)
    
    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                        default=True)


    def __repr__(self):
        """Show info about pet"""

        p = self
        return f"<Pet name: {p.name} | species: {p.species} | photo_url: {p.photo_url} | age: {p.age} | notes: {p.notes} | available: {p.availble} >"

    @classmethod
    def add_pet(self, name, species, photo_url, age, notes, available):
        """Add a pet to the db"""
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()