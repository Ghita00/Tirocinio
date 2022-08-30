from datetime import datetime

from flask import Flask, render_template, session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy import func, extract, desc

from GenDB import *
from flask_fontawesome import FontAwesome
from Utility import Auxcarrello, pages

#blueprint
from Profile import profile
from Ecommerce import ecommerce
from Blog import blog
from Documenti import documenti
from Magazzino import magazzino
from Ordini import ordini
from Personale import personale
from Ricettario import ricettario
from Produzione import produzione

#TODO, ATTENZIONE il campo rating va modificato o settato dal manager
app.config['SECRET_KEY'] = 'thisisasecretkey'
fa = FontAwesome(app) #serve per i font
db.create_all() #serve per il db

#registrazione blueprint
app.register_blueprint(profile, url_prefix = "")
app.register_blueprint(ecommerce, url_prefix = "")
app.register_blueprint(blog, url_prefix = "")
app.register_blueprint(personale, url_prefix = "")
app.register_blueprint(ordini, url_prefix = "")
app.register_blueprint(ricettario, url_prefix = "")
app.register_blueprint(documenti, url_prefix = "")
app.register_blueprint(magazzino, url_prefix = "")
app.register_blueprint(produzione, url_prefix = "")

#per il login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#sito
@login_manager.user_loader
def load_user(user_id):
    return Persone.query.get(user_id)

@app.route('/')
def home():
    pages.disattiva(0)
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    #ATTENZIONE PER NELLA VARIABILE IMG VA MESSO "{{url_for('static', filename='X')}}" DOVE X E IL RISULTATO QUERY
    favorite = list(Semilavorati.query.filter(Semilavorati.Preferito == True))

    personale = session.query(Persone.Mail, Persone.Nome, Persone.Cognome, Immagini.img).\
                join(Immagini, Immagini.Id == Persone.Img).\
                join(Dipendenti, Dipendenti.Mail == Persone.Mail).\
                all()

    post = Articoli.query.order_by(Articoli.DataPubblicazione).first()
    return render_template("sito/index.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, img = "immagine", testo = post,
                           pages = list(pages.pagine), user = utente, prod_fav = favorite, len_prod_fav = len(favorite), personale = personale)

@app.route('/about')
def about():
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    return render_template("sito/about.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, user = utente)

@app.route('/contact')
def contact():
    pages.disattiva(3)
    if current_user.is_authenticated:
        utente = current_user.Nome
    else:
        utente = ''

    return render_template("sito/contact.html", total = Auxcarrello.quantità, totalMoney = Auxcarrello.totale, pages = list(pages.pagine), user = utente)

#gestionale
@app.route('/gestionale/home')
def Ghome():

    #4 quadrati
    incassi_scontriniMerceLordo = session.query(func.sum(
                                ScontriniMerce.Quantità * (((Merce.PrezzoUnitario * Merce.IVA) / 100) + Merce.PrezzoUnitario).label('totale'))). \
                                join(Merce, Merce.Id == ScontriniMerce.Id_Merce).\
                                join(Scontrini, Scontrini.Id == ScontriniMerce.Id_Scontrino).\
                                filter(extract('month', Scontrini.Data)==datetime.now().month).\
                                all()

    incassi_scontriniSemiLordo = session.query(func.sum(ScontriniSemilavorati.Quantità * (
                                ((Semilavorati.PrezzoUnitario * Semilavorati.IVA) / 100) + Semilavorati.PrezzoUnitario).label('totale'))). \
                                join(Semilavorati, Semilavorati.Id == ScontriniSemilavorati.Id_Semilavorato). \
                                join(Scontrini, Scontrini.Id == ScontriniSemilavorati.Id_Scontrino). \
                                filter(extract('month', Scontrini.Data) == datetime.now().month). \
                                all()

    incasso_EcommerceLordo = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * (
                            ((Semilavorati.PrezzoUnitario * Semilavorati.IVA) / 100) + Semilavorati.PrezzoUnitario)).label('totale')). \
                            join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id). \
                            join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id). \
                            filter(FattureVendita.Categoria == 'Ecommerce').\
                            filter(extract('month', FattureVendita.Data) == datetime.now().month).\
                            all()

    incasso_ExtraLordo = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * (
                            ((Semilavorati.PrezzoUnitario * Semilavorati.IVA) / 100) + Semilavorati.PrezzoUnitario)).label('totale')). \
                            join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id). \
                            join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id). \
                            filter(FattureVendita.Categoria == 'Extra'). \
                            filter(extract('month', FattureVendita.Data) == datetime.now().month). \
                            all()
    incassiTotale = 0
    if incassi_scontriniMerceLordo[0][0] != None:
        incassiTotale += incassi_scontriniMerceLordo[0][0]
    if incassi_scontriniSemiLordo[0][0] != None:
        incassiTotale += incassi_scontriniSemiLordo[0][0]
    if incasso_EcommerceLordo[0][0] != None:
        incassiTotale += incasso_EcommerceLordo[0][0]
    if incasso_ExtraLordo[0][0] != None:
        incassiTotale += incasso_ExtraLordo[0][0]

    costiFornitori = session.query(func.sum(ContenutoAcquisto.Quantità * Merce.PrezzoUnitario).label('totale')). \
                    join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce).\
                    join(FattureAcquisto, FattureAcquisto.Id == ContenutoAcquisto.Id_FatturaAcquisto).\
                    filter(extract('month', FattureAcquisto.Data) == datetime.now().month).\
                    all()

    costiPersonale = session.query(func.sum(Stipendi.ImportoNetto)).\
                    filter(extract('month', Stipendi.DataEmissione) == datetime.now().month).\
                    all()

    costiTotale = 0
    if costiFornitori[0][0] != None:
        costiTotale += costiFornitori[0][0]
    if costiPersonale[0][0] != None:
        costiTotale += costiPersonale[0][0]

    clientiTot = Clienti.query.count()

    produzione = Produzione.query.filter(Produzione.Data_Produzione == datetime.now()).count()

    #grafico

    #fatture fornitori
    fatturaAcq = session.query(FattureAcquisto.Status, FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.Mail,
                               DittaFornitrice.NomeDitta, func.sum(ContenutoAcquisto.Quantità * (Merce.PrezzoUnitario + ((Merce.IVA / 100) * Merce.PrezzoUnitario))).label('Totale')). \
        join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore). \
        join(ContenutoAcquisto, ContenutoAcquisto.Id_FatturaAcquisto == FattureAcquisto.Id). \
        join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce). \
        group_by(FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.NomeDitta, DittaFornitrice.Mail). \
        order_by(desc(FattureAcquisto.Data)). \
        all()

    #ordini ricevuti
    list_ricevuti = session.query(FattureVendita.Id, FattureVendita.Mail_Cliente, FattureVendita.Data, FattureVendita.Status). \
                    group_by(FattureVendita.Id, FattureVendita.Mail_Cliente, FattureVendita.Data, FattureVendita.Status).all()

    #planner produzione
    prod = session.query(Semilavorati.Nome, ProduzioneGiornaliera.Data, Produzione.Quantità). \
        join(ProduzioneGiornaliera, Produzione.Data_Produzione == ProduzioneGiornaliera.Data). \
        join(Semilavorati, Semilavorati.Id == Produzione.Id_Semilavorato).all()
    events = []
    for x in prod:
        events.append({
            'Cosa': x.Nome,
            'Quanto': x.Quantità,
            'Quando': x.Data,
        })

    return render_template("gestionale/index.html", incassoTotale=incassiTotale, costiTotale=costiTotale, clientiTot=clientiTot, produzione=produzione,
                           fattureAcq = fatturaAcq,
                           list_ricevuti = list_ricevuti,
                           events = events)

if __name__ == "__main__":
    app.run(debug=True)