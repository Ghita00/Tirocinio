from flask import Blueprint, render_template, request
from sqlalchemy import func, desc

from GenDB import *
from Utility import help


documenti = Blueprint('documenti', __name__)

@documenti.route('/documentiGestionale', methods=['GET', 'POST'])
def documentiGestionale():
    fatturaAcq = session.query(FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.NomeDitta, func.sum(ContenutoAcquisto.Quantità * (Merce.PrezzoUnitario + ((Merce.IVA / 100) * Merce.PrezzoUnitario))).label('Totale')).\
        join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore).\
        join(ContenutoAcquisto, ContenutoAcquisto.Id_FatturaAcquisto == FattureAcquisto.Id).\
        join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce).\
        group_by(FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.NomeDitta).\
        order_by(desc(FattureAcquisto.Data)).\
        all()


    fattureVen = session.query(FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente, func.sum(ContenutoVenditaSemilavorati.Quantità * (Semilavorati.PrezzoUnitario + ((Semilavorati.IVA / 100) * Semilavorati.PrezzoUnitario))).label('Totale')).\
        join(ContenutoVenditaSemilavorati, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id, isouter=True).\
        join(Semilavorati, Semilavorati.Id == ContenutoVenditaSemilavorati.Id_Semilavorato, isouter=True). \
        group_by(FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente).\
        order_by(desc(FattureVendita.Data)).\
        all()

    ddt = DDT.query.order_by(desc(DDT.DataEmissione)).all()

    scontriniMerce = session.query(Scontrini.Data, Scontrini.Id, func.sum(ScontriniMerce.Quantità * ((Merce.IVA / 100) * Merce.PrezzoUnitario) + Merce.PrezzoUnitario).label('Totale')).\
        join(ScontriniMerce, Scontrini.Id == ScontriniMerce.Id_Scontrino).\
        join(Merce, ScontriniMerce.Id_Merce == Merce.Id).\
        group_by(Scontrini.Data, Scontrini.Id).\
        order_by(desc(Scontrini.Data)).\
        all()

    scontriniSemi = session.query(Scontrini.Data, Scontrini.Id, func.sum(
        ScontriniSemilavorati.Quantità * ((Semilavorati.IVA / 100) * Semilavorati.PrezzoUnitario) + Semilavorati.PrezzoUnitario).label('Totale')). \
        join(ScontriniSemilavorati, Scontrini.Id == ScontriniSemilavorati.Id_Scontrino). \
        join(Semilavorati, ScontriniSemilavorati.Id_Semilavorato == Semilavorati.Id). \
        group_by(Scontrini.Data, Scontrini.Id).\
        order_by(desc(Scontrini.Data)).\
        all()

    scontrini = scontriniMerce + scontriniSemi

    if request.method == "POST":
        lista_slider = []
        for i in range(3,7):
            end = help.endSlied(i)
            start = end - 10
            lista_slider.append([start,end])

        nascosto = request.form["nascosto"]
        if nascosto == '1':
            print(request.form["fattureAcq"])
            help.aggiorna(3, request.form["fattureAcq"])
            lista_slider[0][1] = help.endSlied(3)
            lista_slider[0][0] = lista_slider[0][1] - 10
        if nascosto == '2':
            print(request.form["fattureVen"])
            help.aggiorna(4, request.form["fattureVen"])
            lista_slider[1][1] = help.endSlied(4)
            lista_slider[1][0] = lista_slider[1][1] - 10
        if nascosto == '3':
            print(request.form["DDT"])
            help.aggiorna(5, request.form["DDT"])
            lista_slider[2][1] = help.endSlied(5)
            lista_slider[2][0] = lista_slider[2][1] - 10
        if nascosto == '4':
            print(request.form["scontrini"])
            help.aggiorna(6, request.form["scontrini"])
            lista_slider[3][1] = help.endSlied(6)
            lista_slider[3][0] = lista_slider[3][1] - 10

        return render_template("gestionale/documenti.html", FAcquisto = fatturaAcq[lista_slider[0][0]:lista_slider[0][1]], FVendita = fattureVen[lista_slider[1][0]:lista_slider[1][1]], listDDT = ddt[lista_slider[2][0]:lista_slider[2][1]], listScontrini = scontrini[lista_slider[3][0]:lista_slider[3][1]])
    else:
        return render_template("gestionale/documenti.html", FAcquisto = fatturaAcq[0:10], FVendita = fattureVen[0:10], listDDT = ddt[0:10], listScontrini = scontrini[0:10])

@documenti.route('/docSingle/<id>/<categoria>')
#categoria 0. fatture di acquisto, 1. fatture di vendita, 2. ddt, 3. scontrini
def docSingle(id, categoria):

    if categoria == '0':
        doc = session.query(FattureAcquisto.Data, FattureAcquisto.Status, DittaFornitrice.NomeDitta, DittaFornitrice.PartitaIVA,
                            Merce.Nome, Merce.PrezzoUnitario, ContenutoAcquisto.Quantità).\
            join(FattureAcquisto, FattureAcquisto.Id == ContenutoAcquisto.Id_FatturaAcquisto).\
            join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce).\
            join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore).\
            filter(FattureAcquisto.Id == id).all()

        dati = []
        prod = []

        for documento in range(1):
            d = {
                'Data': doc[documento].Data,
                'Status': doc[documento].Status,
                'Nome': doc[documento].NomeDitta,
                'Contatto': doc[documento].PartitaIVA,
            }
            dati.append(d)

        for documento in doc:
            p = {
                'Prodotto' : documento.Nome,
                'Prezzo' : documento.PrezzoUnitario,
                'Quantita' : documento.Quantità,
            }
            prod.append(p)

    if categoria == '1':
        if ContenutoVenditaMerce.query.filter(ContenutoVenditaMerce.Id_FatturaVendità == id).first() is not None:
            doc = session.query(FattureVendita.Data, FattureVendita.Status, Clienti.Mail, Persone.Telefono,
                                Merce.Nome, Merce.PrezzoUnitario, ContenutoVenditaMerce.Quantità). \
                join(FattureVendita, FattureVendita.Id == ContenutoVenditaMerce.Id_FatturaVendità). \
                join(Merce, Merce.Id == ContenutoVenditaMerce.Id_Merce). \
                join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente). \
                join(Persone, Persone.Mail == Clienti.Mail).\
                filter(FattureVendita.Id == id).all()
        else:
            doc = session.query(FattureVendita.Data, FattureVendita.Status, Clienti.Mail, Persone.Telefono,
                                Semilavorati.Nome, Semilavorati.PrezzoUnitario, ContenutoVenditaSemilavorati.Quantità). \
                join(FattureVendita, FattureVendita.Id == ContenutoVenditaSemilavorati.Id_FatturaVendità). \
                join(Semilavorati, Semilavorati.Id == ContenutoVenditaSemilavorati.Id_Semilavorato). \
                join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente). \
                join(Persone, Persone.Mail == Clienti.Mail).\
                filter(FattureVendita.Id == id).all()

        dati = []
        prod = []

        for documento in range(1):
            d = {
                'Data': doc[documento].Data,
                'Status': doc[documento].Status,
                'Nome': doc[documento].Mail,
                'Contatto': doc[documento].Telefono,
            }
            dati.append(d)

        for documento in doc:
            p = {
                'Prodotto': documento.Nome,
                'Prezzo': documento.PrezzoUnitario,
                'Quantita': documento.Quantità,
            }
            prod.append(p)

    if categoria == '2':
        doc = session.query(DDT.DataEmissione, DDT.Status, DittaFornitrice.NomeDitta, DittaFornitrice.PartitaIVA, DDT.Peso, DDT.Colli, DDT.Importo).\
            join(DittaFornitrice, DittaFornitrice.PartitaIVA == DDT.Id_Fornitore).\
            filter(DDT.Id == id).all()

        dati = []
        prod = []

        for documento in range(1):
            d = {
                'Data': doc[documento].DataEmissione,
                'Status': doc[documento].Status,
                'Nome': doc[documento].NomeDitta,
                'Contatto': doc[documento].PartitaIVA,
            }
            dati.append(d)

        for documento in doc:
            p = {
                'Prodotto': documento.Peso,
                'Prezzo': documento.Importo,
                'Quantita': documento.Colli,
            }
            prod.append(p)

    if categoria == '3':
        if ScontriniMerce.query.filter(ScontriniMerce.Id_Scontrino == id).first() is not None:
            doc = session.query(Scontrini.Data, Merce.Nome, ScontriniMerce.Quantità, Merce.PrezzoUnitario,
                                Merce.IVA). \
                join(ScontriniMerce, ScontriniMerce.Id_Scontrino == Scontrini.Id). \
                join(Merce, Merce.Id == ScontriniMerce.Id_Merce).\
                filter(Scontrini.Id == id).all()
        else:
            doc = session.query(Scontrini.Data, Semilavorati.Nome, ScontriniSemilavorati.Quantità, Semilavorati.PrezzoUnitario,
                                Semilavorati.IVA). \
                join(ScontriniSemilavorati, ScontriniSemilavorati.Id_Scontrino == Scontrini.Id). \
                join(Semilavorati, Semilavorati.Id == ScontriniSemilavorati.Id_Semilavorato).\
                filter(Scontrini.Id == id).all()

        dati = []
        prod = []

        for documento in range(1):
            d = {
                'Data': doc[documento].Data,
            }
            dati.append(d)

        for documento in doc:
            p = {
                'Prodotto': documento.Nome,
                'Prezzo': documento.PrezzoUnitario,
                'Quantita': documento.Quantità,
                'IVA': documento.IVA,
            }
            prod.append(p)



    return render_template("gestionale/docSingle.html", doc = dati, prod = prod, id = id, categoria = categoria)

@documenti.route('/addDoc', methods=['GET', 'POST'])
def addDoc():

    return render_template("gestionale/formDocumento.html")

@documenti.route('/bilancioGestionale')
def bilancioGestionale():
    return render_template("gestionale/bilancio.html")

@documenti.route('/bilancioCosti')
def bilancioCosti():
    return render_template("gestionale/")

@documenti.route('/bilancioRicavi')
def bilancioRicavi():
    return render_template("gestionale/")

@documenti.route('/ricevuti')
def ricevuti():
    return render_template("gestionale/")

@documenti.route('/emessi')
def emessi():
    return render_template("gestionale/")

@documenti.route('/cassa')
def cassa():
    return render_template("gestionale/")
