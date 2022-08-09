from datetime import date

from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, \
    validators, TimeField, TextAreaField, FloatField, FieldList, Form, FormField, IntegerField, DateField, \
    PasswordField, TelField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from GenDB import *

personale = Blueprint('personale', __name__)

@personale.route('/personaleGestionale')
def personaleGestionale():
    dip_data = session.query(Dipendenti.DataAssunzione).all()
    dip = Persone.query.join(Dipendenti).filter(Dipendenti.Mail == Persone.Mail).all()

    if dip == None:
        flash("Non hai dipendenti")
        return render_template("gestionale/dipendenti.html", len_Dip=0)


    return render_template("gestionale/dipendenti.html", Dip=list(dip), len_Dip=len(list(dip)), Dip_Data=list(dip_data), len_Dip_Data=len(list(dip_data)))

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

@personale.route('/turni/<id>')
def tabellaTurni(id):
    return render_template("gestionale/turniSingle.html", nome="luca", meseACT="agosto")

