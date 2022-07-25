from flask import Blueprint, render_template, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from GenDB import *
from Profile import LoginForm
from Utility import Auxcarrello, pages

ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/shop', methods=['GET', 'POST'])
def shop():
    pages.disattiva(1)
    if request.method == "POST":
        id = request.form['scelta']
        if id == 2:
            Prodotti = Semilavorati.query.order_by(Semilavorati.PrezzoUnitario).all()
        else:
            Prodotti = Semilavorati.query.order_by(Semilavorati.Nome).all()
    else:
        Prodotti = Semilavorati.query.order_by(Semilavorati.Nome).all()
    return render_template("sito/shop.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, Prod = list(Prodotti), lenProd = len(list(Prodotti)), pages = list(pages.pagine), user = current_user.Nome)

@ecommerce.route('/shop-details/<id>', methods=['GET', 'POST'])
def shop_details(id):
    if request.method == "POST":
        quantita = request.form['quantita']
        if Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).filter(Carrello.Id_Semilavorato == id) == None:
            new_cartProd = Carrello(Mail_Cliente = current_user.Mail, Id_Semilavorato = id, QuantitàCarrello = quantita)
            db.session.add(new_cartProd)
        else:
            Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).filter(Carrello.Id_Semilavorato == id).update({"QuantitàCarrello" : quantita})
        db.session.commit()
        return redirect(url_for('ecommerce.shop'))
    else:
        Prodotto = Semilavorati.query.filter(Semilavorati.Id == id).first()
        return render_template("sito/shop-details.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale,
                               id = Prodotto.Id, nome = Prodotto.Nome, prezzo = Prodotto.PrezzoUnitario, incipit = "incipit", categoria = 'categoria', tags = 'tag', descrizione="Prodotto.Preparazione", user = current_user.Nome)

@ecommerce.route('/shoping-cart', methods=['GET', 'POST'])
def shoping_cart():
    if current_user.is_authenticated:
        prod = Semilavorati.query.join(Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(Carrello.Id_Semilavorato == Semilavorati.Id)
        cart = Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).all()
        if Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).first() != None:
            return render_template("sito/shoping-cart.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale,
                                   Prod = list(prod), lenProd = len(list(prod)), Cart = list(cart), user = current_user.Nome)
        else:
            print('ciao broschi')
            flash("Il tuo carrello è attualmente vuoto")
            return render_template("sito/shoping-cart.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale,
                                   Prod = list(prod), lenProd = len(list(prod)), Cart = list(cart), user = current_user.Nome)
    else:
        return redirect(url_for('profile.login'))

@ecommerce.route('/checkout')
@login_required
def checkout():
    return render_template("sito/checkout.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = current_user.Nome)

@ecommerce.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    if current_user.is_authenticated:
        list_wishlist = Semilavorati.query.join(WishList).filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == Semilavorati.Id).all()
        if WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).first() != None:
            return render_template("sito/wishlist.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, product = list(list_wishlist), len_product = len(list(list_wishlist)), user = current_user.Nome)
        else:
            flash("La tua WishList è attualmente vuota")
            return render_template("sito/wishlist.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                                   product=list(list_wishlist), len_product=len(list(list_wishlist)), user=current_user.Nome)
    else:
        return redirect(url_for('profile.login'))

@ecommerce.route('/modifyWishlist/<id>')
@login_required
def modifyWishlist(id):
    new_cartProd = Carrello(Mail_Cliente = current_user.Mail, Id_Semilavorato = id, QuantitàCarrello = 1)
    delete_wishProd = WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == id)
    db.session.add(new_cartProd)
    delete_wishProd.delete()
    db.session.commit()
    return redirect(url_for('ecommerce.shoping_cart'))

@ecommerce.route('/addWishlist/<id>')
@login_required
def addWishlist(id):
    if WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).filter(WishList.Id_Semilavorato == id).first() != None:
        flash('Questo prodotto è già nella tua WishList')
        return redirect(url_for('ecommerce.shop_details', id=id))
    else:
        new_wishProd = WishList(Mail_Cliente=current_user.Mail, Id_Semilavorato=id)
        db.session.add(new_wishProd)
        db.session.commit()
        return redirect(url_for('ecommerce.shop'))

