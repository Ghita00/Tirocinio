from flask import Blueprint, render_template
from flask_login import current_user

personale = Blueprint('personale', __name__)

@personale.route('/personaleGestionale')
def personaleGestionale():
    return render_template("gestionale/dipendenti.html")

@personale.route('/organizzazioneStaff')
def organizzazioneStaffGestionale():
    return render_template("gestionale/organizzazioneStaff.html")