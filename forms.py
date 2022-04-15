"""Forms for Adopt"""

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, URLField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Length, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",
                        validators=[InputRequired(message="Pet must have a name")])
    species = SelectField("Species",
                        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = URLField("Photo URL",
                        validators=[URL(), Optional()])
    age = IntegerField("Age",
                        validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = TextAreaField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available to adopt",
                            default="checked")

class EditPetForm(FlaskForm):
    """Form for editing an existing pet"""

    photo_url = URLField("Photo URL",
                        validators=[URL(), Optional()])
    notes = TextAreaField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available to adopt",
                            default="checked")
