from flask import Blueprint, render_template

ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/shop')
def shop():
    return render_template("sito/shop.html")

@ecommerce.route('/shop-details')
def shop_details():
    return render_template("sito/shop-details.html")

@ecommerce.route('/shoping-cart')
def shoping_cart():
    return render_template("sito/shoping-cart.html")

@ecommerce.route('/checkout')
def checkout():
    return render_template("sito/checkout.html")

@ecommerce.route('/wisslist')
def wisslist():
    return render_template("sito/wisslist.html")

