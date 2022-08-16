from datetime import date
from datetime import datetime
from sqlalchemy import func
from werkzeug.utils import redirect
from flask import Blueprint, render_template, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, \
    validators, TimeField, TextAreaField, FloatField, FieldList, Form, FormField, IntegerField, DateField, \
    PasswordField, TelField, SelectField, RadioField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from GenDB import *
from Utility import pages

magazzino = Blueprint('magazzino', __name__)


class AddMerce(FlaskForm):
    Nome = StringField('Nome')
    Prezzo = FloatField('Prezzo')
    IVA = FloatField('iva')
    Allergeni = RadioField('Allergeni')

    Submit = SubmitField('Aggiungi')


@magazzino.route('/magazzinoGestionale')
def magazzinoGestionale():
    semi = list(Semilavorati.query.all())
    merce = list(Merce.query.all())

    pages.disattiva(0)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = semi + merce, categoria=0, Semi=semi, Merce=merce)

@magazzino.route('/magazzino/semilavorati')
def semilavorati():
    semi = Semilavorati.query.all()
    pages.disattiva(1)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(semi), categoria=1, Semi=semi, Merce=[])

@magazzino.route('/magazzino/prodotti')
def prodotti():
    merce = Merce.query.filter(Merce.MateriaPrima == False).all()
    pages.disattiva(2)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(merce), categoria=2, Semi=[], Merce=merce)

@magazzino.route('/magazzino/materieprime')
def materieprime():
    merce = Merce.query.filter(Merce.MateriaPrima == True).all()
    pages.disattiva(3)
    return render_template("gestionale/magazzino.html", attiva = pages.pagine, Prod = list(merce), categoria=2, Semi=[], Merce=merce)

@magazzino.route('/magazzino/modificaSemilavorato/<id>', methods=['GET', 'POST'])
def modificaSemilavorato(id):
    semi = Semilavorati.query.filter(Semilavorati.Id == id).first()

    if request.method == "POST":
        nome = request.form['nome']
        prezzo = request.form['prezzo']
        iva = request.form['iva']
        categoria = request.form['categoria']
        descrizione = request.form['descrizione']
        incipit = request.form['incipit']
        quantità = request.form['quantità']

        Semilavorati.query.filter(Semilavorati.Id == id).update({"Nome":nome, "Quantità":quantità, "PrezzoUnitario":prezzo,"IVA":iva,"Categoria":categoria,"Descrizione":descrizione,"Incipit":incipit})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/modificaSemilavorato.html", Semi = semi)

@magazzino.route('/magazzino/modificaMerce/<id>', methods=['GET', 'POST'])
def modificaMerce(id):
    merce = Merce.query.filter(Merce.Id == id).first()

    if request.method == "POST":
        nome = request.form['nome']
        prezzo = request.form['prezzo']
        iva = request.form['iva']
        quantità = request.form['quantità']
        materieprime = request.form['materiaprima']

        Merce.query.filter(Merce.Id == id).update({"Nome":nome, "Quantità":quantità, "PrezzoUnitario":prezzo, "IVA":iva, "MateriaPrima":bool(materieprime)})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/modificaMerce.html", Merce = merce)

@magazzino.route('/magazzino/addMerce', methods=['GET', 'POST'])
def addMerce():
    form = AddMerce()

    form.Allergeni.choices = session.query(Allergeni.Nome).all()

    if request.method == "POST":
        nome = request.form['nome']
        prezzo = request.form['prezzo']
        iva = request.form['iva']
        quantità = request.form['quantità']
        materieprime = request.form['materiaprima']

        Merce.query.filter(Merce.Id == id).update({"Nome":nome, "Quantità":quantità, "PrezzoUnitario":prezzo, "IVA":iva, "MateriaPrima":bool(materieprime)})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/formMerce.html", form=form)