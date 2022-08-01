from flask import Blueprint, render_template
from flask_login import current_user

from GenDB import *
from Utility import Auxcarrello, pages

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blogRoute():
    pages.disattiva(2)
    articoli = Articoli.query.order_by(Articoli.DataPubblicazione).all()
    autori = Blog.query.join(Articoli).filter(Articoli.Id == Blog.Id_Articolo).all()
    post = articoli[0]
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    return render_template("sito/blog.html", ID = post.Id, testo = post, total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, artic = list(articoli), len_artic = len(list(articoli)), aut = list(autori), len_aut = len(list(autori)), user = utente, pages = list(pages.pagine))

@blog.route('/blog-details/<id>')
def blogDetailsRoute(id):
    pages.disattiva(2)
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    articolo = Articoli.query.filter(Articoli.Id == id).first()
    dipendente = Dipendenti.query.join(Blog).filter(Blog.Id_Articolo == id).filter(Dipendenti.Mail == Blog.Mail_Dipendente).first()
    autore = Persone.query.filter(Persone.Mail == dipendente.Mail).first()

    return render_template("sito/blog-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = utente, pages = list(pages.pagine), artic = articolo, aut = autore)

#gestionale
@blog.route('/gBlog')
def Gblog():
    return render_template("gestionale/blog.html")