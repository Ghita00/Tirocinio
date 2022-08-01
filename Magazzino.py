from flask import Blueprint, render_template
from flask_login import current_user

magazzino = Blueprint('magazzino', __name__)

@magazzino.route('/magazzinoGestionale')
def magazzinoGestionale():
    return render_template("gestionale/magazzino.html")

@magazzino.route('/prodotti')
def prodotti():
    return render_template("gestionale/")

@magazzino.route('/semilavorati')
def semilavorati():
    return render_template("gestionele/")

@magazzino.route('/materieprime')
def materieprime():
    return render_template("gestionale/")
