from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, DateTimeField, IntegerField, StringField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, AnyOf, URL

class AdoptionForm(FlaskForm):
    valid_species = ['dog', 'cat', 'porcupine']

    name = StringField("Pet's name", 
    validators = [InputRequired(message = "cannot be blank")])

    species = StringField("Species", 
    validators = [InputRequired(message = "cannot be blank"), AnyOf(valid_species, message="can only be %(values)s")])

    photo_url = StringField("Photo URL", 
    validators = [Optional(), URL(require_tld=False)], default="http://127.0.0.1:5000/static/images/no_pic_400x400.jpg")

    age = IntegerField("age", validators=[Optional(), NumberRange(min=0, max=30)])
    
    notes = StringField("notes", validators=[Optional()])

    available = BooleanField("available", validators=[Optional()], default=True)