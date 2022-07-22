from flask import Flask, render_template
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from GenDB import *
from flask_fontawesome import FontAwesome

#blueprint
from Profile import profile
from Ecommerce import ecommerce
from Blog import blog
from Documenti import documenti
from Magazzino import magazzino

#TODO, ATTENZIONE il campo rating va modificato o settato dal manager

#TODO per gio, bisogna aggiungere un cuoricino dove ci stanno i semilavorati (shop) che andrà collegato alla query di insert nella wishlist

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
    return render_template("sito/index.html")

@app.route('/about')
def about():
    return render_template("sito/about.html")

@app.route('/contact')
def contact():
    return render_template("sito/contact.html")

#gestionale
@app.route('/gestionale/home')
def Ghome():
    return render_template("gestionale/index.html")

if __name__ == "__main__":
    app.run(debug=True)