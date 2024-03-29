from flask import Blueprint, render_template, url_for, request, flash
from flask_login import login_required, current_user
from sqlalchemy import func
from werkzeug.utils import redirect
from GenDB import *
from Utility import Auxcarrello, pages
from datetime import date

ecommerce = Blueprint('ecommerce', __name__)


@ecommerce.route('/shop', methods=['GET', 'POST'])
def shop():
    pages.disattiva(1)
    if current_user.is_authenticated:
        utente = current_user.Nome
        cart = session.query(func.sum(Carrello.QuantitàCarrello)).filter(
            Carrello.Mail_Cliente == current_user.Mail).first()
        tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(
            Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(
            Semilavorati.Id == Carrello.Id_Semilavorato)
        if cart[0] == None and tot[0].totcar == None:
            Auxcarrello.totale = 0
            Auxcarrello.quantità = 0
        else:
            Auxcarrello.totale = round(float(tot[0].totcar), 2)
            Auxcarrello.quantità = cart[0]
    else:
        utente = ''
        Auxcarrello.totale = 0
        Auxcarrello.quantità = 0

    if request.method == "POST":
        if request.form['hidden'] == '2':
            id = request.form['scelta']
            if id == '2':
                Prodotti = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria,
                                         Semilavorati.PrezzoUnitario,
                                         Immagini.img). \
                    join(Immagini, ImmaginiSemilavorati.Id_Img == Immagini.Id). \
                    join(Semilavorati, Semilavorati.Id == ImmaginiSemilavorati.Id_Semilavorato). \
                    order_by(Semilavorati.PrezzoUnitario).all()
            else:
                Prodotti = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria,
                                         Semilavorati.PrezzoUnitario,
                                         Immagini.img). \
                    join(Immagini, ImmaginiSemilavorati.Id_Img == Immagini.Id). \
                    join(Semilavorati, Semilavorati.Id == ImmaginiSemilavorati.Id_Semilavorato). \
                    order_by(Semilavorati.Nome).all()
        else:
            cat = request.form["cat"]
            if (cat == "all"):
                Prodotti = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria,
                                         Semilavorati.PrezzoUnitario,
                                         Immagini.img). \
                    join(Immagini, ImmaginiSemilavorati.Id_Img == Immagini.Id). \
                    join(Semilavorati, Semilavorati.Id == ImmaginiSemilavorati.Id_Semilavorato). \
                    order_by(Semilavorati.Nome).all()
            else:
                Prodotti = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria,
                                         Semilavorati.PrezzoUnitario,
                                         Immagini.img). \
                    join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
                    join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
                    filter(Semilavorati.Categoria == cat). \
                    order_by(Semilavorati.Nome).all()
    else:
        Prodotti = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria,
                                 Semilavorati.PrezzoUnitario, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
            order_by(Semilavorati.Nome). \
            all()

    return render_template("sito/shop.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                           Prod=Prodotti, lenProd=len(Prodotti), pages=list(pages.pagine), user=utente)


@ecommerce.route('/shop-details/<id>', methods=['GET', 'POST'])
def shop_details(id):
    pages.disattiva(1)
    if current_user.is_authenticated:
        utente = current_user.Nome
        Prodotto = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                                 Semilavorati.Descrizione, Semilavorati.PrezzoUnitario, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
            filter(Semilavorati.Id == id).first()

        AllProd = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                                 Semilavorati.Descrizione, Semilavorati.PrezzoUnitario, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img).\
            all()


    else:
        utente = ''
        Prodotto = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                                 Semilavorati.Descrizione, Semilavorati.PrezzoUnitario, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
            filter(Semilavorati.Id == id).first()

        AllProd = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.Categoria, Semilavorati.Incipit,
                                 Semilavorati.Descrizione, Semilavorati.PrezzoUnitario, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img).\
            all()

    if request.method == "POST":
        if current_user.is_authenticated:
            quantita = request.form['quantita']
            if Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).filter(
                    Carrello.Id_Semilavorato == id).first() == None:
                new_cartProd = Carrello(Mail_Cliente=current_user.Mail, Id_Semilavorato=id, QuantitàCarrello=quantita)
                db.session.add(new_cartProd)
                db.session.commit()
            else:
                if int(quantita) > 0:
                    Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).filter(
                        Carrello.Id_Semilavorato == id).update({"QuantitàCarrello": quantita})
                else:
                    delete_prod = Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).filter(
                        Carrello.Id_Semilavorato == id)
                    delete_prod.delete()

                db.session.commit()

            return redirect(url_for('ecommerce.shop'))
        else:
            flash('Devi prima autenticarti')
            return redirect(url_for('profile.login'))
    else:
        print(AllProd)
        return render_template("sito/shop-details.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                               prod=Prodotto, user=utente, pages=list(pages.pagine), id=id, AllProd=AllProd)


@ecommerce.route('/shoping-cart', methods=['GET', 'POST'])
def shoping_cart():
    pages.disattiva(1)
    if current_user.is_authenticated:
        utente = current_user.Nome
        prod = Semilavorati.query.join(Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(
            Carrello.Id_Semilavorato == Semilavorati.Id).order_by(Carrello.Id_Semilavorato)
        cart = Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).order_by(
            Carrello.Id_Semilavorato).all()
        tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(
            Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(
            Semilavorati.Id == Carrello.Id_Semilavorato)

        if Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail).first() != None:
            return render_template("sito/shoping-cart.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                                   Prod=list(prod), lenProd=len(list(prod)), Cart=list(cart), user=utente,
                                   pages=list(pages.pagine), totale=round(float(tot[0].totcar), 2))
        else:
            flash("Il tuo carrello è attualmente vuoto")
            return render_template("sito/shoping-cart.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                                   Prod=list(prod), lenProd=len(list(prod)), Cart=list(cart), user=utente,
                                   pages=list(pages.pagine))
    else:
        return redirect(url_for('profile.login'))


@ecommerce.route('/checkout')
@login_required
def checkout():
    pages.disattiva(1)
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    if Carrello.query.count() > 0:
        Cart = session.query(Semilavorati.Id, Carrello.QuantitàCarrello). \
            join(Semilavorati, Semilavorati.Id == Carrello.Id_Semilavorato). \
            filter(Carrello.Mail_Cliente == current_user.Mail).all()

        # emmissione fattura di vendita
        num = FattureVendita.query.count()
        newFat = FattureVendita(Mail_Cliente=current_user.Mail, NumDocumento=num + 1, Data=date.today(), Categoria='Ecommerce')
        db.session.add(newFat)
        db.session.commit()

        id = session.query(FattureVendita.Id).filter(FattureVendita.Mail_Cliente == current_user.Mail).filter(
            FattureVendita.Data == date.today()).first()

        for prod in Cart:
            newCont = ContenutoVenditaSemilavorati(Id_FatturaVendità=id[0], Id_Semilavorato=prod[0], Quantità=prod[1])
            db.session.add(newCont)

            Semilavorati.query.filter(Semilavorati.Id == prod[0]).update({'Quantità': Semilavorati.Quantità - prod[1]})

        db.session.commit()

        delete_cart = Carrello.query.filter(Carrello.Mail_Cliente == current_user.Mail)
        delete_cart.delete()

        db.session.commit()

    Auxcarrello.totale = 0
    Auxcarrello.quantità = 0

    flash("Pagamento avvenuto con successo")

    return redirect(url_for('home'))


@ecommerce.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    pages.disattiva(1)
    if current_user.is_authenticated:
        utente = current_user.Nome
        list_wishlist = session.query(Semilavorati.Id, Semilavorati.Nome, Semilavorati.PrezzoUnitario, Semilavorati.Quantità, Immagini.img). \
            join(ImmaginiSemilavorati, ImmaginiSemilavorati.Id_Semilavorato == Semilavorati.Id). \
            join(Immagini, Immagini.Id == ImmaginiSemilavorati.Id_Img). \
            join(WishList, WishList.Id_Semilavorato == Semilavorati.Id). \
            filter(WishList.Mail_Cliente == current_user.Mail).all()

        if WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).first() != None:
            return render_template("sito/wishlist.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                                   product=list_wishlist, user=utente, pages=list(pages.pagine))
        else:
            flash("La tua WishList è attualmente vuota")
            return render_template("sito/wishlist.html", total=Auxcarrello.quantità, totalMoney=Auxcarrello.totale,
                                   product=list_wishlist, user=utente, pages=list(pages.pagine))
    else:
        return redirect(url_for('profile.login'))


@ecommerce.route('/modifyWishlist/<id>')
@login_required
def modifyWishlist(id):
    new_cartProd = Carrello(Mail_Cliente=current_user.Mail, Id_Semilavorato=id, QuantitàCarrello=1)
    delete_wishProd = WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).filter(
        WishList.Id_Semilavorato == id)
    db.session.add(new_cartProd)
    delete_wishProd.delete()
    db.session.commit()

    cart = session.query(func.sum(Carrello.QuantitàCarrello)).filter(Carrello.Mail_Cliente == current_user.Mail).first()
    tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(
        Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(Semilavorati.Id == Carrello.Id_Semilavorato)

    if cart[0] == None and tot[0].totcar == None:
        Auxcarrello.totale = 0
        Auxcarrello.quantità = 0
    else:
        Auxcarrello.totale = round(float(tot[0].totcar), 2)
        Auxcarrello.quantità = cart[0]

    return redirect(url_for('ecommerce.shoping_cart'))


@ecommerce.route('/deleteWishlist/<id>')
@login_required
def deleteWishlist(id):
    delete_wishProd = WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).filter(
        WishList.Id_Semilavorato == id)
    delete_wishProd.delete()
    db.session.commit()

    cart = session.query(func.sum(Carrello.QuantitàCarrello)).filter(Carrello.Mail_Cliente == current_user.Mail).first()
    tot = session.query(func.sum(Semilavorati.PrezzoUnitario * Carrello.QuantitàCarrello).label('totcar')).join(
        Carrello).filter(Carrello.Mail_Cliente == current_user.Mail).filter(Semilavorati.Id == Carrello.Id_Semilavorato)

    if cart[0] == None and tot[0].totcar == None:
        Auxcarrello.totale = 0
        Auxcarrello.quantità = 0
    else:
        Auxcarrello.totale = round(float(tot[0].totcar), 2)
        Auxcarrello.quantità = cart[0]

    return redirect(url_for('ecommerce.wishlist'))


@ecommerce.route('/addWishlist/<id>')
@login_required
def addWishlist(id):
    if WishList.query.filter(WishList.Mail_Cliente == current_user.Mail).filter(
            WishList.Id_Semilavorato == id).first() != None:
        flash('Questo prodotto è già nella tua WishList')
        return redirect(url_for('ecommerce.shop_details', id=id))
    else:
        new_wishProd = WishList(Mail_Cliente=current_user.Mail, Id_Semilavorato=id)
        db.session.add(new_wishProd)
        db.session.commit()
        return redirect(url_for('ecommerce.wishlist'))
