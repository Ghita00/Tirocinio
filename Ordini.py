from flask import Blueprint, render_template
from flask_login import current_user

ordini = Blueprint('ordini', __name__)

@ordini.route('/ordiniGestionale')
def ordiniGestionale():
    return render_template("gestionale/ordini.html")

@ordini.route('/newOrdine')
def newOrdine():
    return render_template("gestionale/nuovoOrdini.html")