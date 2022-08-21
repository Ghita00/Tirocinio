from flask import Blueprint, render_template, request
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

    print(list_emessi)
    print(list_ricevuti)

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


@ordini.route('/ordineSingle/<id>/<categoria>')
#categoria 0. Ricevuto, 1. Emesso
def ordineSingle(id, categoria):
    ord = []
    if categoria == '1':
        if ContenutoVenditaMerce.query.filter(ContenutoVenditaMerce.Id_FatturaVendità == id).first() is not None:
            ord = session.query(FattureVendita.Mail_Cliente, Persone.Telefono, Merce.Nome, ContenutoVenditaMerce.Quantità, FattureVendita.Data).\
                join(ContenutoVenditaMerce, ContenutoVenditaMerce.Id_FatturaVendità == FattureVendita.Id).\
                join(Merce, ContenutoVenditaMerce.Id_Merce == Merce.Id).\
                join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente).\
                join(Persone, Clienti.Mail == Persone.Mail).\
                group_by(FattureVendita.Mail_Cliente, Persone.Telefono, Persone.Nome, Persone.Cognome, Merce.Nome, ContenutoVenditaMerce.Quantità, FattureVendita.Data).all()
        else:
            ord = session.query(FattureVendita.Mail_Cliente, Persone.Telefono,
                                Semilavorati.Nome, ContenutoVenditaSemilavorati.Quantità, FattureVendita.Data). \
                join(ContenutoVenditaSemilavorati, ContenutoVenditaSemilavorati.Id_FatturaVendità == FattureVendita.Id). \
                join(Semilavorati, ContenutoVenditaSemilavorati.Id_Semilavorato == Semilavorati.Id). \
                join(Clienti, Clienti.Mail == FattureVendita.Mail_Cliente). \
                join(Persone, Clienti.Mail == Persone.Mail). \
                group_by(FattureVendita.Mail_Cliente, Persone.Telefono, Persone.Nome, Persone.Cognome,
                                Semilavorati.Nome, ContenutoVenditaSemilavorati.Quantità, FattureVendita.Data).all()

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
            }
            prod.append(p)

        print(dati)
        print(prod)
    else:
        ord = session.query(FattureAcquisto.Id_Fornitore, DittaFornitrice.NomeDitta,
                                Merce.Nome, ContenutoAcquisto.Quantità, FattureAcquisto.Data). \
                join(ContenutoAcquisto, ContenutoAcquisto.Id_FatturaAcquisto == FattureAcquisto.Id). \
                join(Merce, ContenutoAcquisto.Id_Merce == Merce.Id). \
                join(DittaFornitrice, DittaFornitrice.PartitaIVA == FattureAcquisto.Id_Fornitore). \
                group_by(FattureAcquisto.Id_Fornitore, DittaFornitrice.NomeDitta,
                                Merce.Nome, ContenutoAcquisto.Quantità, FattureAcquisto.Data).all()

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