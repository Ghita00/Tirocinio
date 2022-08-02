from flask import Blueprint, render_template
from GenDB import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FileField, SelectField, IntegerRangeField, \
    validators, TimeField, SelectMultipleField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo

ricettario = Blueprint('ricettario', __name__)

class newRecipe(FlaskForm):
    Nome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    MateriePrime = SelectMultipleField('Materie prime', choices=list(session.query(Merce.Nome).filter(Merce.MateriaPrima == True)))
    Persone = IntegerRangeField('Persone', [validators.NumberRange(min=1, max=20)])
    Tempo = TimeField('Durata')
    Preparazione = TextAreaField('Inserire preparazione')

    submbit = SubmitField('Aggiungi')

@ricettario.route('/ricettarioGestionale')
def ricettarioGestionale():
    recipes = Ricette.query.all()
    return render_template("gestionale/ricettario.html", ricette = list(recipes), len_ricette = len(list(recipes)))

@ricettario.route('/addRicetta', methods=['GET', 'POST'])
def aggiungiRicetta():
    form = newRecipe();
    return render_template("gestionale/formRicette.html", form=form)

@ricettario.route('/ricetta/<id>', methods=['GET', 'POST'])
def ricetta(id):
    return render_template("gestionale/ricetteSingle.html")

