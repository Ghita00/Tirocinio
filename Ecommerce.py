from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from GenDB import *

ecommerce = Blueprint('ecommerce', __name__)

class Auxcarrello():
    quantità = 0
    totale = 0

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
        #Prodotto = Semilavorati.query
        return render_template("sito/shop-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale,
                                                    nome = "prodotto", prezzo = "prezzo", incipit = "incipit", categoria = 'categoria', tags = 'tag', descrizione="descrizione")

@ecommerce.route('/shoping-cart')
def shoping_cart():
    # TODO VEDERE SE IL FRA E LOGGATTO
    return render_template("sito/shoping-cart.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)

@ecommerce.route('/checkout')
def checkout():
    return render_template("sito/checkout.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale)

@ecommerce.route('/wishlist')
@login_required
def wishlist():
    #TODO VEDERE SE IL FRA E LOGGATTO
    list_wishlist = Semilavorati.query.join(WishList).filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == Semilavorati.Id).all()
    return render_template("sito/wishlist.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, product = list(list_wishlist), len_product = len(list(list_wishlist)))

@ecommerce.route('/modifyWishlist')
def modifyWishlist():
    #TODO query che aggiunge al carrello fe rimuove dalla whislist + aggiunta campo in stock
    return redirect(url_for('ecommerce.shop'))

@ecommerce.route('/addWishlist')
def addWishlist():
    #TODO QUERY CHE AGGIUNGE UN ELEMENTO ALLA WISHLIST
    return redirect(url_for('ecommerce.shop'))

