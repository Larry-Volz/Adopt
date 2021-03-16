from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 
from forms import AdoptionForm

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route('/<int:pet_id>')
def pet_detail(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template("pet-detail.html", pet=pet)

@app.route('/add',methods=["GET","POST"])
def add_pet():
    form = AdoptionForm()

    if form.validate_on_submit(): #csrf & is POST
        name = form.name.data  
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        flash(f"Successfully created {name}")
        return redirect('/')

    else:
        return render_template("add_pet.html", form=form)

@app.route('/edit/<int:pet_id>',methods=["GET","POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AdoptionForm(obj=pet)

    if form.validate_on_submit(): #csrf & is POST
        pet.name = form.name.data  
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data


        # db.session.add(pet)
        db.session.commit()

        flash(f"Successfully edited {name}")
        return redirect('/')

    else:
        return render_template("edit_pet.html", form=form)



