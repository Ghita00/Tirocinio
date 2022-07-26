from flask import Flask, render_template
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from GenDB import *
from flask_fontawesome import FontAwesome
from Utility import Auxcarrello, pages

#blueprint
from Profile import profile
from Ecommerce import ecommerce
from Blog import blog
from Documenti import documenti
from Magazzino import magazzino

#TODO, ATTENZIONE il campo rating va modificato o settato dal manager
app.config['SECRET_KEY'] = 'thisisasecretkey'
fa = FontAwesome(app) #serve per i font
db.create_all() #serve per il db

#registrazione blueprint
app.register_blueprint(profile, url_prefix = "")
app.register_blueprint(ecommerce, url_prefix = "")
app.register_blueprint(blog, url_prefix = "")

#per il login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#sito
@login_manager.user_loader
def load_user(user_id):
    return Persone.query.get(user_id)

@app.route('/')
def home():
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    pages.disattiva(0)
    #ATTENZIONE PER NELLA VARIABILE IMG VA MESSO "{{url_for('static', filename='X')}}" DOVE X E IL RISULTATO QUERY
    #TODO QUERY ARTICOLI IN EVIDENZA
    #TODO QUERY ULTIMO POST BLOG
    return render_template("sito/index.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, img="immagine", testo = "testo articolo", pages = list(pages.pagine), user = utente)

@app.route('/about')
def about():
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    return render_template("sito/about.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = utente)

@app.route('/contact')
def contact():
    pages.disattiva(3)
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    return render_template("sito/contact.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, pages = list(pages.pagine), user = utente)

#gestionale
@app.route('/gestionale/home')
def Ghome():
    return render_template("gestionale/index.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)

if __name__ == "__main__":
    app.run(debug=True)