from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from GenDB import *

ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/shop/<id>')
def shop(id):
    if id == 1:
        Prodotti = Semilavorati.query.order_by(Semilavorati.Nome).all()
    else:
        Prodotti = Semilavorati.query.order_by(Semilavorati.PrezzoUnitario).all()
    return render_template("sito/shop.html",Prod = list(Prodotti), lenProd = len(list(Prodotti)))

@ecommerce.route('/shop-details')
def shop_details():
    return render_template("sito/shop-details.html")

@ecommerce.route('/shoping-cart')
def shoping_cart():
    return render_template("sito/shoping-cart.html")

@ecommerce.route('/checkout')
def checkout():
    return render_template("sito/checkout.html")

@ecommerce.route('/wishlist')
@login_required
def wishlist():
    #TODO VEDERE SE IL FRA E LOGGATTO
    list_wishlist = Semilavorati.query.join(WishList).filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == Semilavorati.Id).all()
    return render_template("sito/wishlist.html", product = list(list_wishlist), len_product = len(list(list_wishlist)))

@ecommerce.route('/modifyWishlist')
def modifyWishlist():
    #fare la query che modifica
    return redirect(url_for('ecommerce.shop'))

