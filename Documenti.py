from datetime import date
from datetime import datetime

from flask import Blueprint, render_template, request, url_for, flash
from sqlalchemy import func, desc
from werkzeug.utils import redirect

from GenDB import *
from Utility import help

documenti = Blueprint('documenti', __name__)

@documenti.route('/documentiGestionale', methods=['GET', 'POST'])
def documentiGestionale():
    fatturaAcq = session.query(FattureAcquisto.Status, FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.NomeDitta, func.sum(ContenutoAcquisto.Quantità * (Merce.PrezzoUnitario + ((Merce.IVA / 100) * Merce.PrezzoUnitario))).label('Totale')).\
        join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore).\
        join(ContenutoAcquisto, ContenutoAcquisto.Id_FatturaAcquisto == FattureAcquisto.Id).\
        join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce).\
        group_by(FattureAcquisto.Id, FattureAcquisto.Data, DittaFornitrice.NomeDitta).\
        order_by(desc(FattureAcquisto.Data)).\
        all()


    fattureVenSemi = session.query(FattureVendita.Status, FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente, func.sum(ContenutoVenditaSemilavorati.Quantità * (Semilavorati.PrezzoUnitario + ((Semilavorati.IVA / 100) * Semilavorati.PrezzoUnitario))).label('Totale')).\
        join(ContenutoVenditaSemilavorati, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id).\
        join(Semilavorati, Semilavorati.Id == ContenutoVenditaSemilavorati.Id_Semilavorato). \
        group_by(FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente).\
        order_by(desc(FattureVendita.Data)).\
        all()

    fattureVenMerci = session.query(FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente, func.sum(
        ContenutoVenditaMerce.Quantità * (Merce.PrezzoUnitario + ((Merce.IVA / 100) * Merce.PrezzoUnitario))).label('Totale')). \
        join(ContenutoVenditaMerce, ContenutoVenditaMerce.Id_FatturaVendità == FattureVendita.Id). \
        join(Merce, Merce.Id == ContenutoVenditaMerce.Id_Merce). \
        group_by(FattureVendita.Id, FattureVendita.Data, FattureVendita.Mail_Cliente). \
        order_by(desc(FattureVendita.Data)). \
        all()

    fattureVen = fattureVenSemi + fattureVenMerci

    ddt = DDT.query.order_by(desc(DDT.DataEmissione)).all()

    scontriniMerce = session.query(Scontrini.Data, Scontrini.Id, func.sum(ScontriniMerce.Quantità * (((Merce.IVA / 100) * Merce.PrezzoUnitario) + Merce.PrezzoUnitario)).label('Totale')).\
        join(ScontriniMerce, Scontrini.Id == ScontriniMerce.Id_Scontrino).\
        join(Merce, ScontriniMerce.Id_Merce == Merce.Id).\
        group_by(Scontrini.Data, Scontrini.Id).\
        order_by(desc(Scontrini.Data)).\
        all()

    scontriniSemi = session.query(Scontrini.Data, Scontrini.Id, func.sum(
        ScontriniSemilavorati.Quantità * (((Semilavorati.IVA / 100) * Semilavorati.PrezzoUnitario) + Semilavorati.PrezzoUnitario)).label('Totale')). \
        join(ScontriniSemilavorati, Scontrini.Id == ScontriniSemilavorati.Id_Scontrino). \
        join(Semilavorati, ScontriniSemilavorati.Id_Semilavorato == Semilavorati.Id). \
        group_by(Scontrini.Data, Scontrini.Id).\
        order_by(desc(Scontrini.Data)).\
        all()

    scontrini = scontriniMerce + scontriniSemi

    stipendio = True
    if datetime.now().day == 28 and Stipendi.query.filter(Stipendi.DataEmissione == date.today()).first() is None:
        stipendio = True
    else:
        stipendio = False

    if request.method == "POST":
        lista_slider = []
        for i in range(3,7):
            end = help.endSlied(i)
            start = end - 5
            lista_slider.append([start,end])

        nascosto = request.form["nascosto"]
        if nascosto == '1':
            print(request.form["fattureAcq"])
            help.aggiorna(3, request.form["fattureAcq"])
            lista_slider[0][1] = help.endSlied(3)
            lista_slider[0][0] = lista_slider[0][1] - 5
        if nascosto == '2':
            print(request.form["fattureVen"])
            help.aggiorna(4, request.form["fattureVen"])
            lista_slider[1][1] = help.endSlied(4)
            lista_slider[1][0] = lista_slider[1][1] - 5
        if nascosto == '3':
            print(request.form["DDT"])
            help.aggiorna(5, request.form["DDT"])
            lista_slider[2][1] = help.endSlied(5)
            lista_slider[2][0] = lista_slider[2][1] - 5
        if nascosto == '4':
            print(request.form["scontrini"])
            help.aggiorna(6, request.form["scontrini"])
            lista_slider[3][1] = help.endSlied(6)
            lista_slider[3][0] = lista_slider[3][1] - 5

        return render_template("gestionale/documenti.html", FAcquisto = fatturaAcq[lista_slider[0][0]:lista_slider[0][1]], FVendita = fattureVen[lista_slider[1][0]:lista_slider[1][1]],
                               listDDT = ddt[lista_slider[2][0]:lista_slider[2][1]], listScontrini = scontrini[lista_slider[3][0]:lista_slider[3][1]], stip = stipendio)
    else:
        return render_template("gestionale/documenti.html", FAcquisto = fatturaAcq[0:5], FVendita = fattureVen[0:5], listDDT = ddt[0:5], listScontrini = scontrini[0:5], stip = stipendio)

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
    if request.method == 'POST':
        if request.form['nascosto'] == '1':
            tipo = request.form['Documento']
            sottotipo = None
            prodotti = []
            volte = int(request.form['Quantita'])
            clienti = Clienti.query.all()
            fornitore = DittaFornitrice.query.all()
            if tipo == 'Fatturavendita':
                sottotipo = request.form['TipoFattura']
                if sottotipo == 'Merce':
                    prodotti = Merce.query.filter(Merce.MateriaPrima == False).all()
                else:
                    prodotti = Semilavorati.query.all()
            if tipo == 'Scontrino':
                sottotipo = request.form['TipoScontrino']
                if sottotipo == 'Merce':
                    prodotti = Merce.query.filter(Merce.MateriaPrima == False).all()
                else:
                    prodotti = Semilavorati.query.all()

            if tipo == 'DDT':
                volte = 1
                prodotti = Merce.query.all()
            if tipo == 'Fatturaacquisto':
                prodotti = Merce.query.all()

            return render_template("gestionale/formDocumento.html", volte=volte, tipo = tipo, sottotipo = sottotipo, Prod = prodotti, Clienti = clienti, Fornitori = fornitore)

        if request.form['nascosto'] == '2':
            tipo = request.form['tipo']
            sottotipo = request.form['sottotipo']

            if tipo == 'Fatturavendita':
                if sottotipo == 'Merce':
                    if FattureVendita.query.filter(FattureVendita.Mail_Cliente == request.form['Mail']).filter(FattureVendita.NumDocumento == request.form['NumDocumento']).first() is None:
                        new_fat = FattureVendita(Mail_Cliente=request.form['Mail'], NumDocumento=request.form['NumDocumento'], Data=request.form['Data'], Categoria=request.form['Categoria'])
                        db.session.add(new_fat)
                        db.session.commit()

                        fat = session.query(FattureVendita.Id).filter(
                            FattureVendita.Mail_Cliente == request.form['Mail']).filter(
                            FattureVendita.NumDocumento == request.form['NumDocumento']).first()

                        fat = fat[0]

                        for i in range(int(request.form['volte'])):
                            id = int(request.form['Prodotto-' + str(i)])
                            quanti = session.query(Merce.Quantità).filter(Merce.Id == id).first()
                            if int(quanti[0]) > int(request.form['q-' + str(i)]):
                                contenutoFat = ContenutoVenditaMerce(Id_FatturaVendità=fat, Id_Merce=id, Quantità=request.form['q-' + str(i)])
                                Merce.query.filter(Merce.Id == id).update({"Quantità": Merce.Quantità - request.form['q-' + str(i)]})
                                db.session.add(contenutoFat)
                            else:
                                flash('Non hai abbastanza prodotti in magazzino')
                                print('Non hai abbastanza prodotti in magazzino')

                        FattureVendita.query.filter(FattureVendita.Id == fat).update(
                            {"Status": bool(request.form['Status'])})

                        db.session.commit()

                    else:
                        flash('Esiste già una fattura a nome di questo cliente con questo numero di documento')
                        print('Esiste già una fattura a nome di questo cliente con questo numero di documento')

                else:
                    if FattureVendita.query.filter(FattureVendita.Mail_Cliente == request.form['Mail']).filter(FattureVendita.NumDocumento == request.form['NumDocumento']).first() is None:
                        new_fat = FattureVendita(Mail_Cliente=request.form['Mail'], NumDocumento=request.form['NumDocumento'], Data=request.form['Data'], Categoria=request.form['categoria'])
                        db.session.add(new_fat)
                        db.session.commit()

                        fat = session.query(FattureVendita.Id).filter(
                            FattureVendita.Mail_Cliente == request.form['Mail']).filter(
                            FattureVendita.NumDocumento == request.form['NumDocumento']).first()

                        fat = fat[0]

                        for i in range(int(request.form['volte'])):
                            id = int(request.form['Prodotto-' + str(i)])
                            quanti = session.query(Semilavorati.Quantità).filter(Semilavorati.Id == id).first()
                            if int(quanti[0]) > int(request.form['q-' + str(i)]):
                                contenutoFat = ContenutoVenditaSemilavorati(Id_FatturaVendità=fat, Id_Semilavorato=id, Quantità=request.form['q-' + str(i)])
                                Semilavorati.query.filter(Semilavorati.Id == id).update({"Quantità": Semilavorati.Quantità - request.form['q-' + str(i)]})
                                db.session.add(contenutoFat)
                            else:
                                flash('Non hai abbastanza prodotti in magazzino')
                                print('Non hai abbastanza prodotti in magazzino')
                        FattureVendita.query.filter(FattureVendita.Id == fat).update(
                            {"Status": bool(request.form['Status'])})

                        db.session.commit()
                    else:
                        flash('Esiste già una fattura a nome di questo cliente con questo numero di documento')
                        print('Esiste già una fattura a nome di questo cliente con questo numero di documento')

            if tipo == 'Scontrino':
                if sottotipo == 'Merce':
                    new_sc = Scontrini(Data=request.form['Data'])
                    db.session.add(new_sc)
                    db.session.commit()

                    sc = session.query(Scontrini.Id).filter(Scontrini.Data == request.form['Data']).order_by(desc(Scontrini.Id)).first()
                    sc = sc[0]

                    for i in range(int(request.form['volte'])):
                        id = int(request.form['Prodotto-' + str(i)])
                        quanti = session.query(Merce.Quantità).filter(Merce.Id == id).first()
                        if quanti[0] > int(request.form['q-' + str(i)]):
                            contenutoSc = ScontriniMerce(Id_Scontrino=sc, Id_Merce=id, Quantità=request.form['q-' + str(i)])
                            Merce.query.filter(Merce.Id == id).update({"Quantità": Merce.Quantità - request.form['q-' + str(i)]})
                            db.session.add(contenutoSc)
                        else:
                            flash('Non hai abbastanza prodotti in magazzino')
                            print('Non hai abbastanza prodotti in magazzino')

                    db.session.commit()
                else:
                    new_sc = Scontrini(Data=request.form['Data'])
                    db.session.add(new_sc)
                    db.session.commit()

                    sc = session.query(Scontrini.Id).filter(Scontrini.Data == request.form['Data']).order_by(
                        desc(Scontrini.Id)).first()
                    sc = sc[0]

                    for i in range(int(request.form['volte'])):
                        id = int(request.form['Prodotto-' + str(i)])
                        quanti = session.query(Semilavorati.Quantità).filter(Semilavorati.Id == id).first()
                        if quanti[0] > int(request.form['q-' + str(i)]):
                            contenutoSc = ScontriniSemilavorati(Id_Scontrino=sc, Id_Semilavorato=id, Quantità=request.form['q-' + str(i)])
                            Semilavorati.query.filter(Semilavorati.Id == id).update({"Quantità": Semilavorati.Quantità - request.form['q-' + str(i)]})
                            db.session.add(contenutoSc)
                        else:
                            flash('Non hai abbastanza prodotti in magazzino')
                            print('Non hai abbastanza prodotti in magazzino')

                    db.session.commit()

            if tipo == 'DDT':
                newDDT = DDT(Id_Fornitore=request.form['PartitaIVA'], DataEmissione=request.form['Data'], Note=request.form['Note'],
                             Importo=request.form['Importo'], Peso=request.form['Peso'], Colli=request.form['Colli'], NumDocumento=request.form['NumDocumento'])

                db.session.add(newDDT)
                db.session.commit()

            if tipo == 'Fatturaacquisto':
                ditta = DittaFornitrice.query.filter(DittaFornitrice.Mail == request.form['Mail']).first()
                if FattureAcquisto.query.filter(FattureAcquisto.Id_Fornitore == ditta.PartitaIVA).filter(FattureAcquisto.NumDocumento == request.form['NumDocumento']).first() is None:
                    new_fat = FattureAcquisto(Id_Fornitore=ditta.PartitaIVA, NumDocumento=request.form['NumDocumento'], Data=request.form['Data'])
                    db.session.add(new_fat)
                    db.session.commit()

                    fat = session.query(FattureAcquisto.Id).filter(FattureAcquisto.Id_Fornitore == ditta.PartitaIVA).filter(FattureAcquisto.NumDocumento == request.form['NumDocumento']).first()
                    fat = fat[0]

                    for i in range(int(request.form['volte'])):
                        id = int(request.form['Prodotto-' + str(i)])
                        contenutoFat = ContenutoAcquisto(Id_FatturaAcquisto = fat, Id_Merce = id, Quantità = request.form['q-'+str(i)])
                        Merce.query.filter(Merce.Id == id).update({"Quantità": Merce.Quantità + request.form['q-' + str(i)]})
                        db.session.add(contenutoFat)

                    FattureAcquisto.query.filter(FattureAcquisto.Id == fat).update({"Status" : bool(request.form['Status'])})

                    db.session.commit()
                else:
                    print('Esiste già una fattura a nome di questo fornitore con questo numero di documento')
                    flash('Esiste già una fattura a nome di questo fornitore con questo numero di documento')

            return redirect(url_for("documenti.documentiGestionale"))

    return render_template("gestionale/formDocumento.html", volte=0, tipo = None, sottotipo = None, Prod = None)

@documenti.route('/bilancioGestionale')
def bilancioGestionale():
    incassi_scontriniMerceNetto = session.query(func.sum(ScontriniMerce.Quantità * Merce.PrezzoUnitario).label('totale')).\
        join(Merce, Merce.Id == ScontriniMerce.Id_Merce).all()
    incassi_scontriniSemiNetto = session.query(func.sum(ScontriniSemilavorati.Quantità * Semilavorati.PrezzoUnitario).label('totale')). \
        join(Semilavorati, Semilavorati.Id == ScontriniSemilavorati.Id_Semilavorato).all()
    incasso_ScontriniNetto = int(incassi_scontriniMerceNetto[0][0]) + int(incassi_scontriniSemiNetto[0][0])

    incassi_scontriniMerceLordo = session.query(func.sum(ScontriniMerce.Quantità * (((Merce.PrezzoUnitario * Merce.IVA)/100) + Merce.PrezzoUnitario).label('totale'))).\
        join(Merce, Merce.Id == ScontriniMerce.Id_Merce).all()
    incassi_scontriniSemiLordo = session.query(func.sum(ScontriniSemilavorati.Quantità * (((Semilavorati.PrezzoUnitario * Semilavorati.IVA)/100) + Semilavorati.PrezzoUnitario).label('totale'))). \
        join(Semilavorati, Semilavorati.Id == ScontriniSemilavorati.Id_Semilavorato).all()
    incasso_ScontriniLordo = int(incassi_scontriniMerceLordo[0][0]) + int(incassi_scontriniSemiLordo[0][0])

    incasso_EcommerceNetto = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * Semilavorati.PrezzoUnitario).label('totale')).\
        join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id).\
        join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id).\
        filter(FattureVendita.Categoria == 'Ecommerce').all()

    incasso_EcommerceLordo = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * (((Semilavorati.PrezzoUnitario * Semilavorati.IVA)/100) + Semilavorati.PrezzoUnitario)).label('totale')).\
        join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id).\
        join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id).\
        filter(FattureVendita.Categoria == 'Ecommerce').all()

    incasso_ExtraNetto = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * Semilavorati.PrezzoUnitario).label('totale')).\
        join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id).\
        join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id).\
        filter(FattureVendita.Categoria == 'Extra').all()

    incasso_ExtraLordo = session.query(func.sum(ContenutoVenditaSemilavorati.Quantità * (((Semilavorati.PrezzoUnitario * Semilavorati.IVA)/100) + Semilavorati.PrezzoUnitario)).label('totale')).\
        join(FattureVendita, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id).\
        join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id).\
        filter(FattureVendita.Categoria == 'Extra').all()

    costiFornitori = session.query(func.sum(ContenutoAcquisto.Quantità * Merce.PrezzoUnitario).label('totale')).\
        join(Merce, Merce.Id == ContenutoAcquisto.Id_Merce).all()

    costiPersonale = session.query(func.sum(Stipendi.ImportoNetto)).all()

    if incasso_ExtraNetto[0][0] == None:
        print(1)
        incasso_ExtraNetto = [(0,)]
    if incasso_ExtraLordo[0][0] == None:
        print(2)
        incasso_ExtraLordo = [(0,)]
    if incasso_EcommerceLordo[0][0] == None:
        print(3)
        incasso_EcommerceLordo = [(0,)]
    if incasso_EcommerceNetto[0][0] == None:
        print(5)
        incasso_EcommerceNetto = [(0,)]
    if incassi_scontriniMerceLordo[0][0] == None:
        print(6)
        incassi_scontriniMerceLordo = [(0,)]
    if incassi_scontriniMerceNetto[0][0] == None:
        print(7)
        incassi_scontriniMerceNetto = [(0,)]
    if incasso_ScontriniNetto == None: ###
        print(8)
        incasso_ScontriniNetto = 0
    if incasso_ScontriniLordo == None: ###
        print(9)
        incassi_scontriniMerceLordo = 0
    if incassi_scontriniSemiLordo[0][0] == None:
        print(10)
        incassi_scontriniMerceLordo = [(0,)]
    if incassi_scontriniSemiNetto[0][0] == None:
        print(11)
        incassi_scontriniMerceNetto = [(0,)]

    indici = []     #0. Rapposrto costi guadagni, 1. Incisione costi, 2. Incisione ricavi, 3. spesa più incisiva, 3. ricavo più incisivo

    #Rapporto tra i guadagni e le spese
    guadagni_netti = int(incassi_scontriniMerceNetto[0][0]) + int(incassi_scontriniSemiNetto[0][0]) + int(incasso_ExtraNetto[0][0]) + int(incasso_EcommerceNetto[0][0])
    costi_netti = int(costiPersonale[0][0]) + int(costiFornitori[0][0])

    indici.append(guadagni_netti - costi_netti)

    #Quanto incidono le spese nel quadro complessivo
    percCosti = (100 * costi_netti) / (costi_netti + guadagni_netti)

    indici.append(percCosti)

    #Quanto incidono gli incassi nel quadro complessivo
    percRicavi = (100 * guadagni_netti) / (costi_netti + guadagni_netti)

    indici.append(percRicavi)

    #La spesa che incide di più nella situazione globale
    min = -1

    if int(costiPersonale[0][0]) > int(costiFornitori[0][0]):
        min = int(costiPersonale[0][0])
    else:
        min = int(costiFornitori[0][0])

    indici.append(min)

    #Il ricavo che incide di più nella situazione globale
    max = -1
    scontrini = int(incassi_scontriniSemiNetto[0][0]) + int(incassi_scontriniMerceNetto[0][0])

    if scontrini > int(incasso_EcommerceNetto[0][0]):
        max = scontrini
    else:
        max = int(incasso_EcommerceNetto[0][0])

    if max < int(incasso_ExtraNetto[0][0]):
        max = int(incasso_ExtraNetto[0][0])

    indici.append(max)

    return render_template("gestionale/bilancio.html", scontriniNetto = incasso_ScontriniNetto, scontriniLordo = incasso_ScontriniLordo,
                           EcommerceNetto = int(incasso_EcommerceNetto[0][0]), EcommerceLordo=int(incasso_EcommerceLordo[0][0]), ExtraNetto=int(incasso_ExtraNetto[0][0]),
                           ExtraLordo=int(incasso_ExtraLordo[0][0]), CostiFornitori=int(costiFornitori[0][0]), CostiPersonale=int(costiPersonale[0][0]),
                           indici=indici)


