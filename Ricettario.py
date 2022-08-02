from flask import Blueprint, render_template
from flask_login import current_user

ricettario = Blueprint('ricettario', __name__)

@ricettario.route('/ricettarioGestionale')
def ricettarioGestionale():
    return render_template("gestionale/ricettario.html")

@ricettario.route('/ricetta/<id>')
def ricetta(id):
    return render_template("gestionale/ricetteSingle.html")

@ricettario.route('/addRicetta')
def aggiungiRicetta():
    return render_template("gestionale/formRicette.html")

