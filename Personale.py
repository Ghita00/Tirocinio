from datetime import date

from sqlalchemy import func
from werkzeug.utils import redirect
from flask import Blueprint, render_template, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, \
    validators, TimeField, TextAreaField, FloatField, FieldList, Form, FormField, IntegerField, DateField, \
    PasswordField, TelField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from GenDB import *

personale = Blueprint('personale', __name__)

class RegistrazioneDipendente(FlaskForm):
    nome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    cognome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Cognome"})
    datanascita = DateField(validators=[InputRequired()], format='%Y-%m-%d')
    mail = StringField(validators=[InputRequired()], render_kw={"placeholder": "Mail"})
    #username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    #password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    #password_confirm = PasswordField(validators=[InputRequired(), EqualTo('password', message='Passwords must match')],render_kw={"placeholder": "Repeat Password"})
    telefono = TelField(validators=[InputRequired()], render_kw={"placeholder": "Telefono"})

    submit = SubmitField('Register')

class addTurno(FlaskForm):
    dipendente = SelectField('Dipendente', choices=[])
    turno = SelectField('Turno', choices=[])

    submit = SubmitField('Aggiungi')

@personale.route('/personaleGestionale')
def personaleGestionale():
    dip_data = session.query(Dipendenti.DataAssunzione).all()
    dip = Persone.query.join(Dipendenti).filter(Dipendenti.Mail == Persone.Mail).all()

    if dip == None:
        flash("Non hai dipendenti")
        return render_template("gestionale/dipendenti.html", len_Dip=0)


    return render_template("gestionale/dipendenti.html", Dip=list(dip), len_Dip=len(list(dip)), Dip_Data=list(dip_data), len_Dip_Data=len(list(dip_data)))

@personale.route('/aggiungiDipendente', methods=['GET', 'POST'])
def addDipendente():
    form = RegistrazioneDipendente()

    if form.validate_on_submit():
        new_Person = Persone(Nome=form.nome.data, Cognome=form.cognome.data, DataNascita=form.datanascita.data, Mail=form.mail.data, Telefono=form.telefono.data, Username='', Password='-', Rating=0)
        new_Dip = Dipendenti(Mail=form.mail.data, DataAssunzione=date.today())
        db.session.add(new_Person)
        db.session.add(new_Dip)
        db.session.commit()

    return render_template("gestionale/formDipendente.html", form=form)

@personale.route('/organizzazioneStaff')
def organizzazioneStaffGestionale():
    turni = Turni.query.all()
    return render_template("gestionale/organizzazioneStaff.html", Turni=list(turni))

@personale.route('/addDipTurno/<data>', methods=['GET', 'POST'])
def addDipendenteTurno(data):
    form = addTurno()
    form.dipendente.choices = [ dipendente.Nome + " " + dipendente.Cognome for dipendente in Persone.query.join(Dipendenti).filter(Persone.Mail == Dipendenti.Mail).all()]
    form.turno.choices = [turno.Nome for turno in Turni.query.all()]

    if request.method == 'POST':
        dip = form.dipendente.data.split()

        dipMail = session.query(Persone.Mail).filter(Persone.Nome == dip[0]).filter(Persone.Cognome == dip[1]).first()
        turnoId = session.query(Turni.Id).filter(Turni.Nome == form.turno.data).first()

        oraI = session.query(Turni.OraInizio).filter(Turni.Id == turnoId[0]).first()
        oraF = session.query(Turni.OraFine).filter(Turni.Id == turnoId[0]).first()

        new_persTurni = PersonaleTurni(Mail_Dipendente = dipMail[0], Id_Turno = turnoId[0], Data = data, OraInizio = str(oraI[0]), OraFine = str(oraF[0]))
        db.session.add(new_persTurni)
        db.session.commit()

        return redirect(url_for("personale.organizzazioneStaffGestionale"))


    return render_template("gestionale/formTurno.html", form=form)

@personale.route('/turni/<id>')
def tabellaTurni(id):
    turni = PersonaleTurni.query.filter(PersonaleTurni.Mail_Dipendente == id)
    dip = Persone.query.filter(Persone.Mail == id)
    #TODO query per passarmi anche i dati sul turno
    tot = session.query(func.sum(PersonaleTurni.OraFine - PersonaleTurni.OraInizio)).filter(PersonaleTurni.Mail_Dipendente == id).first()
    return render_template("gestionale/turniSingle.html", Dip=list(dip), meseACT="agosto", Turni = list(turni), Tot = list(tot))

