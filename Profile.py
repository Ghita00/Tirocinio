from flask import Blueprint, render_template, redirect, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from GenDB import *


profile = Blueprint('profile', __name__)

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@profile.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Persone.query.filter_by(Username=form.username.data).first()
        print(user)
        if user:
            if bcrypt.check_password_hash(user.Password, form.password.data):
                login_user(user)
                print(Persone.query.join(Dipendenti).filter(Persone.Mail == Dipendenti.Mail))
                if (Persone.query.join(Dipendenti).filter(Persone.Mail == Dipendenti.Mail) != None) :
                    print("sono qui")
                    return render_template('gestionale/index.html')
                else:
                    return render_template('sito/index.html')
    return render_template('sito/login.html', form=form)

@profile.route('/signup')
def signup():
    return render_template('sito/login.html')

@profile.route('/logout')
def logout():
    return render_template('sito/index.html')




