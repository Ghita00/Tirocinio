from flask import Blueprint, render_template, request, redirect, url_for
from GenDB import *
from Utility import help

ordini = Blueprint('ordini', __name__)

@ordini.route('/ordiniGestionale', methods=['GET', 'POST'])
def ordiniGestionale():
    list_ricevuti = session.query(FattureVendita.Id, FattureVendita.Mail_Cliente, FattureVendita.Data).\
                group_by(FattureVendita.Id, FattureVendita.Mail_Cliente, FattureVendita.Data).all()

    list_emessi = session.query(FattureAcquisto.Id, DittaFornitrice.NomeDitta, FattureAcquisto.Data).\
        join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore).\
        group_by(FattureAcquisto.Id, DittaFornitrice.NomeDitta, FattureAcquisto.Data).all()

    if request.method == "POST":
        lista_slider = []
        for i in range(1, 3):
            end = help.endSlied(i)
            start = end - 10
            lista_slider.append([start, end])

        if request.form["nascosto"] == '1':
            ricevuti = request.form["ricevuti"]
            print(request.form["ricevuti"])
            help.aggiorna(1, request.form["ricevuti"])
            lista_slider[0][1] = help.endSlied(1)
            lista_slider[0][0] = lista_slider[0][1] - 10
        else:
            emessi = request.form["emessi"]
            print(request.form["emessi"])
            help.aggiorna(2, request.form["emessi"])
            lista_slider[1][1] = help.endSlied(2)
            lista_slider[1][0] = lista_slider[1][1] - 10

        return render_template("gestionale/ordini.html", list_ricevuti = list_ricevuti[lista_slider[0][0]:lista_slider[0][1]], list_emessi = list_emessi[lista_slider[1][0]:lista_slider[1][1]])
    else:
        #passare sempre i primi 10 elementi delle liste
        return render_template("gestionale/ordini.html", list_ricevuti = list_ricevuti[0:10], list_emessi = list_emessi[0:10])


@ordini.route('/ordineSingle/<id>/<categoria>', methods=['GET', 'POST'])
#categoria 0. Ricevuto, 1. Emesso
def ordineSingle(id, categoria):
    if request.method == 'POST':
        data = request.form['dataProd']
        volte = request.form['volte']

        if ProduzioneGiornaliera.query.filter(ProduzioneGiornaliera.Data == data).first() is None:
            newProdGio = ProduzioneGiornaliera(Data=data, Note="nessuna")
            db.session.add(newProdGio)
            db.session.commit()

        semi_daProdurre = list(session.query(Produzione.Id_Semilavorato).filter(Produzione.Data_Produzione == data))
        semi_daProdurre = [semi.Id_Semilavorato for semi in semi_daProdurre]

        for i in range(0, int(volte)):

            prod = request.form["prod-"+str(i)]
            q = request.form["q-"+str(i)]

            if int(prod) not in semi_daProdurre:
                newProd = Produzione(Data_Produzione=data, Id_Semilavorato=int(prod),
                                     Quantità=int(q))
                db.session.add(newProd)
            else:
                Produzione.query.filter(Produzione.Data_Produzione == data). \
                    filter(Produzione.Id_Semilavorato == prod). \
                    update({'Quantità': Produzione.Quantità + q})

            Semilavorati.query.filter(Semilavorati.Id == prod).update(
                {"Quantità": Semilavorati.Quantità + q})
        db.session.commit()

        return redirect(url_for("produzione.produzioneGestionale"))
    else:
        if categoria == '1':
            if ContenutoVenditaMerce.query.filter(ContenutoVenditaMerce.Id_FatturaVendità == id).first() is not None:
                ord = session.query(FattureVendita.Mail_Cliente, Persone.Telefono, Merce.Nome, ContenutoVenditaMerce.Quantità, FattureVendita.Data, Merce.Id).\
                    join(ContenutoVenditaMerce, ContenutoVenditaMerce.Id_FatturaVendità == FattureVendita.Id).\
                    join(Merce, ContenutoVenditaMerce.Id_Merce == Merce.Id).\
                    join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente).\
                    join(Persone, Clienti.Mail == Persone.Mail).\
                    filter(FattureVendita.Id == id).all()
            else:
                ord = session.query(FattureVendita.Mail_Cliente, Persone.Telefono, Semilavorati.Id,
                                    Semilavorati.Nome, ContenutoVenditaSemilavorati.Quantità, FattureVendita.Data). \
                    join(ContenutoVenditaSemilavorati, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id). \
                    join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id). \
                    join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente). \
                    join(Persone, Clienti.Mail == Persone.Mail). \
                    filter(FattureVendita.Id == id).all()

            dati = []
            prod = []

            for ordine in range(1):
                d = {
                    'Telefono': ord[ordine].Telefono,
                    'Mail' : ord[ordine].Mail_Cliente,
                    'Data': ord[ordine].Data,
                }
                dati.append(d)

            for ordine in ord:
                p = {
                    'Nome': ordine.Nome,
                    'Quantita': ordine.Quantità,
                    'Id' : ordine.Id,
                }
                prod.append(p)

        else:
            ord = session.query(FattureAcquisto.Id_Fornitore, DittaFornitrice.NomeDitta,
                                    Merce.Nome, ContenutoAcquisto.Quantità, FattureAcquisto.Data). \
                    join(ContenutoAcquisto, ContenutoAcquisto.Id_FatturaAcquisto == FattureAcquisto.Id). \
                    join(Merce, ContenutoAcquisto.Id_Merce == Merce.Id). \
                    join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore). \
                    filter(FattureAcquisto.Id == id).all()

            dati = []
            prod = []

            for ordine in range(1):
                d = {
                    'PartitaIVA': ord[ordine].Id_Fornitore,
                    'Nome': ord[ordine].NomeDitta,
                    'Data': ord[ordine].Data,
                }
                dati.append(d)

            for ordine in ord:
                p = {
                    'Nome': ordine.Nome,
                    'Quantita': ordine.Quantità,
                }
                prod.append(p)
        return render_template("gestionale/ordineSingle.html", id = id, categoria = categoria, dati = dati, prod = prod)