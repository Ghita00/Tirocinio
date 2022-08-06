from flask import Blueprint, render_template
from flask_login import current_user
from Utility import pages

magazzino = Blueprint('magazzino', __name__)

@magazzino.route('/magazzinoGestionale')
def magazzinoGestionale():
    #TODO QUERY DI TUTTO
    pages.disattiva(0)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine)

@magazzino.route('/magazzino/semilavorati')
def semilavorati():
    # TODO QUERY SOLO SEMILAVORATI
    pages.disattiva(1)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine)

@magazzino.route('/magazzino/prodotti')
def prodotti():
    #TODO QUERY SOLO PRODOTTI
    pages.disattiva(2)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine)

@magazzino.route('/magazzino/materieprime')
def materieprime():
    # TODO QUERY SOLO MATERIE PRIME
    pages.disattiva(3)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine)
