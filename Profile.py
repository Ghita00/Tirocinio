from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from sqlalchemy import func
from wtforms import StringField, PasswordField, SubmitField, DateField, FileField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from datetime import date

from GenDB import *
from Utility import Auxcarrello, pages

profile = Blueprint('profile', __name__)

class RegisterForm(FlaskForm):
    nome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    cognome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Cognome"})
    datanascita = DateField(validators=[InputRequired()], format='%Y-%m-%d')
    mail = StringField(validators=[InputRequired()], render_kw={"placeholder": "Mail"})
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    password_confirm = PasswordField(validators=[InputRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Repeat Password"})
    telefono = StringField(validators=[InputRequired()], render_kw={"placeholder": "Telefono"})

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@profile.route('/login', methods=['GET', 'POST'])
def login():
    pages.disattiva(0)
    form = LoginForm()
    if form.validate_on_submit():
        user = Persone.query.filter_by(Username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.Password, form.password.data):
                login_user(user)
                if (Persone.query.join(Dipendenti).filter(Persone.Mail == Dipendenti.Mail).filter(Persone.Username == user.Username).first() != None) :
                    print("Dipendente")
                    return render_template('gestionale/index.html', total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, pages = list(pages.pagine))
                else:
                    print("Cliente")
                    cart = session.query(func.sum(Carrello.QuantitàCarrello)).filter(Carrello.Mail_Cliente == current_user.Mail).first()
                    tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(Semilavorati.Id == Carrello.Id_Semilavorato)
                    Auxcarrello.totale = round(float(tot[0].totcar), 2)
                    Auxcarrello.quantità = cart[0]
                    return redirect(url_for('profile.user'))

    utente = ''
    return render_template('sito/login.html', total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, form=form, pages = list(pages.pagine), user = utente)

@profile.route('/user')
@login_required
def user():
    pages.disattiva(0)
    cart = session.query(func.sum(Carrello.QuantitàCarrello)).filter(Carrello.Mail_Cliente == current_user.Mail).first()
    tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(Semilavorati.Id == Carrello.Id_Semilavorato)
    Auxcarrello.totale = round(float(tot[0].totcar),2)
    Auxcarrello.quantità = cart[0]
    return render_template('sito/user.html', total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, nome = current_user.Nome, cognome=current_user.Cognome, mail=current_user.Mail, datanascita=current_user.DataNascita, user = current_user.Nome, pages = list(pages.pagine))

@profile.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@profile.route('/register', methods=['GET', 'POST'])
def register():
    pages.disattiva(0)
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Persone(Mail=form.mail.data, Nome=form.nome.data, Cognome=form.cognome.data, Username=form.username.data, Password=form.password.data, DataNascita=form.datanascita.data, Telefono=form.telefono.data, Rating=0)
        new_client = Clienti(Mail=form.mail.data, DataRegistrazione=date.today())
        db.session.add(new_user)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('profile.login'))

    utente = ''
    return render_template('sito/register.html', total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, form=form, pages = list(pages.pagine), user = utente)

@profile.route('/sendMex', methods=['GET', 'POST'])
def sendMex():
    pages.disattiva(0)
    if current_user.is_authenticated:
        #TODO QUERY DI METTERE IL MESSAGGIO DENTRO
        return redirect(url_for('home'))
    else:
        return redirect(url_for('profile.login'))

@profile.route('/commento', methods=['GET', 'POST'])
def commento():
    return render_template("sito/messaggio.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, pages = list(pages.pagine))

@profile.route('/sendComment', methods=['GET', 'POST'])
def sendComment():
    pages.disattiva(0)
    if current_user.is_authenticated:
        return redirect(url_for('profile.commento'))
    else:
        return redirect(url_for('profile.login'))
