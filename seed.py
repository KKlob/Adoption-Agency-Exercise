"""Seed file to make sample data for adoption_db"""
from models import Pet, db
from app import app

# create all tables
db.drop_all()
db.create_all()

# if table isn't empty, empty it
Pet.query.delete()

# Add new pets
pet1 = Pet(name="Waffle", species="Cat", photo_url="https://images.pexels.com/photos/1543793/pexels-photo-1543793.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age="5", notes="No notes")

pet2 = Pet(name="Samus", species="Dog", photo_url="https://images.pexels.com/photos/2820134/pexels-photo-2820134.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age="7", notes="No notes")

pet3 = Pet(name="Charlie", species="Dog", photo_url="https://images.pexels.com/photos/2820134/pexels-photo-2820134.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age="10", notes="No notes")

pet4 = Pet(name="Pig", species="Cat", photo_url="https://images.pexels.com/photos/1543793/pexels-photo-1543793.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age="3", notes="No notes")


# add pets to db.session and commit to db
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)
db.session.commit()