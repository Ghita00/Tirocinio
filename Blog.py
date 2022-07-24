from flask import Blueprint, render_template
from GenDB import *
from Ecommerce import Auxcarrello

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blogRoute():
    articoli = Articoli.query.all()
    autori = Blog.query.join(Articoli).filter(Articoli.Id == Blog.Id_Articolo).all()
    return render_template("sito/blog.html",total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, artic = list(articoli), len_artic = len(list(articoli)), aut = list(autori), len_aut = len(list(autori)))

@blog.route('/blog-details')
def blogDetailsRoute():
    return render_template("sito/blog-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)

#gestionale
@blog.route("/gestionale/blog")
def Gblog():
    return render_template("gestionale/", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)