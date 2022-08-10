from flask import Blueprint, render_template, request

from Utility import pages
from GenDB import *

magazzino = Blueprint('magazzino', __name__)


@magazzino.route('/magazzinoGestionale')
def magazzinoGestionale():
    semi = list(Semilavorati.query.all())
    merce = list(Merce.query.all())

    pages.disattiva(0)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = semi + merce)

@magazzino.route('/magazzino/semilavorati')
def semilavorati():
    semi = Semilavorati.query.all()
    pages.disattiva(1)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(semi))

@magazzino.route('/magazzino/prodotti')
def prodotti():
    merce = Merce.query.filter(Merce.MateriaPrima == False).all()
    pages.disattiva(2)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(merce))

@magazzino.route('/magazzino/materieprime')
def materieprime():
    merce = Merce.query.filter(Merce.MateriaPrima == True).all()
    pages.disattiva(3)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(merce))

@magazzino.route('/magazzino/modificaSemilavorato/<id>', methods=['GET', 'POST'])
def modificaSemilavorato(id):
    semi = Semilavorati.query.filter(Semilavorati.Id == id).first()

    if request.method == "POST":
        return "ciao"

    return render_template("gestionale/modificaSemilavorato.html", Semi = semi)

@magazzino.route('/magazzino/modificaMerce/<id>', methods=['GET', 'POST'])
def modificaMerce(id):
    merce = Merce.query.filter(Merce.Id == id).first()

    if request.method == "POST":
        return "ciao"

    return render_template("gestionale/modificaMerce.html", Merce = merce)