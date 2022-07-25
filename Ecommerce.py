from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from GenDB import *
from Profile import LoginForm
from Utility import Auxcarrello

ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == "POST":
        id = request.form['scelta']
        if id == 2:
            Prodotti = Semilavorati.query.order_by(Semilavorati.PrezzoUnitario).all()
        else:
            Prodotti = Semilavorati.query.order_by(Semilavorati.Nome).all()
    else:
        Prodotti = Semilavorati.query.order_by(Semilavorati.Nome).all()
    return render_template("sito/shop.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, Prod = list(Prodotti), lenProd = len(list(Prodotti)))

@ecommerce.route('/shop-details/<id>', methods=['GET', 'POST'])
def shop_details(id):
    #TODO QUERY PER OTTENERE IL PRODOTTO
    if request.method == "POST":
        quantita = request.form['quantita']
        #TODO QUERY CHE AGGIUNGE IL PRODOTTO AL CARRELLO OPPURE AGGIORNA LA QUANTITA
        return redirect(url_for('ecommerce.shop'))
    else:
        Prodotto = Semilavorati.query.filter(Semilavorati.Id == id).first()
        return render_template("sito/shop-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale,
                                                    nome = Prodotto.Nome, prezzo = Prodotto.PrezzoUnitario, incipit = "incipit", categoria = 'categoria', tags = 'tag', descrizione="Prodotto.Preparazione")

@ecommerce.route('/shoping-cart')
def shoping_cart():
    if current_user.is_authenticated:
        return render_template("sito/shoping-cart.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)
    else:
        return render_template("sito/login.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, form=LoginForm())

@ecommerce.route('/checkout')
@login_required
def checkout():
    return render_template("sito/checkout.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)

@ecommerce.route('/wishlist')
def wishlist():
    if current_user.is_authenticated:
        list_wishlist = Semilavorati.query.join(WishList).filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == Semilavorati.Id).all()
        return render_template("sito/wishlist.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, product = list(list_wishlist), len_product = len(list(list_wishlist)), nome = current_user.Nome)
    else:
        return render_template("sito/login.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, form = LoginForm())

@ecommerce.route('/modifyWishlist')
@login_required
def modifyWishlist():
    #TODO query che aggiunge al carrello fe rimuove dalla whislist + aggiunta campo in stock
    return redirect(url_for('ecommerce.shop'))

@ecommerce.route('/addWishlist')
@login_required
def addWishlist():
    #TODO QUERY CHE AGGIUNGE UN ELEMENTO ALLA WISHLIST
    return redirect(url_for('ecommerce.shop'))

