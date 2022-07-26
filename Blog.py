from flask import Blueprint, render_template
from flask_login import current_user

from GenDB import *
from Utility import Auxcarrello

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blogRoute():
    articoli = Articoli.query.all()
    autori = Blog.query.join(Articoli).filter(Articoli.Id == Blog.Id_Articolo).all()
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = None

    return render_template("sito/blog.html",total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, artic = list(articoli), len_artic = len(list(articoli)), aut = list(autori), len_aut = len(list(autori)), user = utente)

@blog.route('/blog-details')
def blogDetailsRoute():
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = None

    return render_template("sito/blog-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = utente)

#gestionale
@blog.route("/gestionale/blog")
def Gblog():
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = None
    return render_template("gestionale/", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = utente)