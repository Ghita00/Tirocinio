from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from GenDB import *


ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/shop')
def shop():
    Prodotti = Semilavorati.query.all()
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
def wishlist():
    return render_template("sito/wishlist.html")

@ecommerce.route('/modifyWishlist')
def modifyWishlist():
    #fare la query che modifica
    return redirect(url_for('ecommerce.shop'))

