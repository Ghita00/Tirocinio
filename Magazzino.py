from datetime import date
from datetime import datetime
from sqlalchemy import func
from werkzeug.utils import redirect
from flask import Blueprint, render_template, url_for, request
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
    semi = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                         Semilavorati.PrezzoUnitario, Semilavorati.Quantità, Immagini.img). \
        join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
        join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
        all()
    merce = session.query(Merce.Id, Merce.Nome, Merce.PrezzoUnitario, Merce.Quantità, Immagini.img). \
        join(ImmaginiMerce, ImmaginiMerce.Id_Merce == Merce.Id). \
        join(Immagini, Immagini.Id == ImmaginiMerce.Id_Img). \
        all()

    print(semi[0].Quantità)
    print(merce)
    print(semi + merce)

    pages.disattiva(0)
    return render_template("gestionale/magazzino.html", attiva=pages.pagine, Prod=(semi + merce), categoria=0, Semi=semi,
                           Merce=merce)


@magazzino.route('/magazzino/semilavorati')
def semilavorati():
    semi = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                         Semilavorati.PrezzoUnitario, Semilavorati.Quantità, Immagini.img). \
        join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
        join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
        all()
    pages.disattiva(1)
    return render_template("gestionale/magazzino.html", attiva=pages.pagine, Prod=semi, categoria=1, Semi=semi,
                           Merce=[])


@magazzino.route('/magazzino/prodotti')
def prodotti():
    merce = session.query(Merce.Id, Merce.Nome, Merce.PrezzoUnitario, Merce.Quantità, Immagini.img). \
        join(ImmaginiMerce, ImmaginiMerce.Id_Merce == Merce.Id). \
        join(Immagini, Immagini.Id == ImmaginiMerce.Id_Img). \
        filter(Merce.MateriaPrima == False). \
        all()
    pages.disattiva(2)
    return render_template("gestionale/magazzino.html", attiva=pages.pagine, Prod=merce, categoria=2, Semi=[],
                           Merce=merce)


@magazzino.route('/magazzino/materieprime')
def materieprime():
    merce = session.query(Merce.Id, Merce.Nome, Merce.PrezzoUnitario, Merce.Quantità, Immagini.img). \
        join(ImmaginiMerce, ImmaginiMerce.Id_Merce == Merce.Id). \
        join(Immagini, Immagini.Id == ImmaginiMerce.Id_Img). \
        filter(Merce.MateriaPrima == True). \
        all()
    pages.disattiva(3)
    return render_template("gestionale/magazzino.html", attiva=pages.pagine, Prod=merce, categoria=2, Semi=[],
                           Merce=merce)


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

        Semilavorati.query.filter(Semilavorati.Id == id).update(
            {"Nome": nome, "Quantità": quantità, "PrezzoUnitario": prezzo, "IVA": iva, "Categoria": categoria,
             "Descrizione": descrizione, "Incipit": incipit})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/modificaSemilavorato.html", Semi=semi)


@magazzino.route('/magazzino/modificaMerce/<id>', methods=['GET', 'POST'])
def modificaMerce(id):
    merce = Merce.query.filter(Merce.Id == id).first()

    if request.method == "POST":
        nome = request.form['nome']
        prezzo = request.form['prezzo']
        iva = request.form['iva']
        quantità = request.form['quantità']
        materieprime = request.form['materiaprima']

        Merce.query.filter(Merce.Id == id).update(
            {"Nome": nome, "Quantità": quantità, "PrezzoUnitario": prezzo, "IVA": iva,
             "MateriaPrima": bool(materieprime)})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/modificaMerce.html", Merce=merce)


@magazzino.route('/magazzino/addMerce', methods=['GET', 'POST'])
def addMerce():
    form = AddMerce()

    form.Allergeni.choices = [Allergeni.Nome for Allergeni in Allergeni.query.all()]

    if request.method == "POST":
        nome = request.form['nome']
        prezzo = request.form['prezzo']
        iva = request.form['iva']
        quantità = request.form['quantità']
        materieprime = request.form['materiaprima']

        Merce.query.filter(Merce.Id == id).update(
            {"Nome": nome, "Quantità": quantità, "PrezzoUnitario": prezzo, "IVA": iva,
             "MateriaPrima": bool(materieprime)})
        db.session.commit()

        return redirect(url_for('magazzino.magazzinoGestionale'))

    return render_template("gestionale/formMerce.html", form=form)


@magazzino.route('/magazzino/addPrefe/<id>')
def addPrefe(id):
    prefe = session.query(Semilavorati.Preferito).filter(Semilavorati.Id == id).first()
    Semilavorati.query.filter(Semilavorati.Id == id).update({'Preferito': not prefe[0]})
    db.session.commit()
    return redirect(url_for("magazzino.magazzinoGestionale"))
