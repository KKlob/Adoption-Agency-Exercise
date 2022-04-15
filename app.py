"""Adopt application."""

from flask import Flask, request, render_template, redirect, flash, session, get_flashed_messages
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


# Config app stuff
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'doifhaofhnaifj'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# connect db to app and create all tables
connect_db(app)

@app.route('/')
def show_homepage():
    """Shows homepage for adoption site"""
    pets = Pet.query.all()
    msgs = get_flashed_messages()
    return render_template('homepage.jinja', pets=pets, msgs=msgs)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Pet Add form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        Pet.add_pet(name, species, photo_url, age, notes, available)
        flash(f'Pet {name} has been added successfully')
        return redirect('/')

    else:
        return render_template('pet_add_form.jinja', form=form)

@app.route('/<petID>', methods=['GET', 'POST'])
def show_edit_pet_form(petID):
    """Pet Edit Form; handle editing"""
    pet = Pet.query.get_or_404(petID)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f'Pet {pet.name} updated!')
        return redirect('/')

    else:
        return render_template('pet_edit_form.jinja', form=form, pet=pet)

    