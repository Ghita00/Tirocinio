from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FileField
from wtforms.validators import InputRequired, Length, ValidationError
from datetime import date
from GenDB import *

profile = Blueprint('profile', __name__)

class RegisterForm(FlaskForm):
    nome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nome"})
    cognome = StringField(validators=[InputRequired()], render_kw={"placeholder": "Cognome"})
    datanascita = DateField(validators=[InputRequired()], format='%Y-%m-%d')
    mail = StringField(validators=[InputRequired()], render_kw={"placeholder": "Mail"})
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    telefono = StringField(validators=[InputRequired()], render_kw={"placeholder": "Telefono"})

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

@profile.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Persone.query.filter_by(Username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.Password, form.password.data):
                login_user(user)
                if (Persone.query.join(Dipendenti).filter(Persone.Mail == Dipendenti.Mail).filter(Persone.Username == user.Username).first() != None) :
                    print("Dipendente")
                    return render_template('gestionale/index.html')
                else:
                    print("Cliente")
                    return redirect(url_for('profile.user'))
    return render_template('sito/login.html', form=form)

@profile.route('/user')
@login_required
def user():
    return render_template('sito/user.html', nome = current_user.Nome, cognome=current_user.Cognome, mail=current_user.Mail, datanascita=current_user.DataNascita)

@profile.route('/logout')
@login_required
def logout():
    return render_template('sito/index.html')

@profile.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Persone(Mail=form.mail.data, Nome=form.nome.data, Cognome=form.cognome.data, Username=form.username.data, Password=form.password.data, DataNascita=form.datanascita.data, Telefono=form.telefono.data, Rating=0)
        new_client = Clienti(Mail=form.mail.data, DataRegistrazione=date.today())
        db.session.add(new_user, new_client)
        db.session.commit()
        return redirect(url_for('profile.user'))

    return render_template('sito/register.html', form=form)




