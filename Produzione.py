from flask import Blueprint, render_template, url_for, flash, request

from werkzeug.utils import redirect

from GenDB import *

produzione = Blueprint('produzione', __name__)


@produzione.route('/produzioneGestionale', methods=['GET', 'POST'])
def produzioneGestionale():
    prod = session.query(Semilavorati.Nome, ProduzioneGiornaliera.Data, Produzione.Quantità).\
        join(ProduzioneGiornaliera, Produzione.Data_Produzione == ProduzioneGiornaliera.Data).\
        join(Semilavorati, Semilavorati.Id == Produzione.Id_Semilavorato).all()
    events = []
    for x in prod:
        events.append({
            'Cosa' : x.Nome,
            'Quanto' : x.Quantità,
            'Quando' : x.Data,
        })

    print(events)
    return render_template("gestionale/produzioneGiornaliera.html", events = events)

@produzione.route('/addProduzione', methods=['GET', 'POST'])
def aggiungiProd():
    semi = list(Semilavorati.query.all())
    quantita = 0
    if request.method == "POST":
        if request.form['nascosto'] == '1':
            return render_template("gestionale/formProduzione.html", Semi = semi, Quantita = int(request.form['quantita']))
        else:
            quanti = int(request.form['volte'])

            prod = set()
            for i in range(quanti):
                prod.add(request.form['prodotto-' + str(i)])

            if len(prod) < quanti:
                flash('Hai inserito lo stesso prodotto più volte')
                return render_template("gestionale/formProduzione.html", Semi=semi, Quantita=quantita)
            else:
                if ProduzioneGiornaliera.query.filter(ProduzioneGiornaliera.Data == request.form['data']).first() is None:
                    newProdGio = ProduzioneGiornaliera(Data=request.form['data'], Note=request.form['note'])
                    db.session.add(newProdGio)
                    db.session.commit()

                semi_daProdurre = list(session.query(Produzione.Id_Semilavorato))
                semi_daProdurre = [semi.Id_Semilavorato for semi in semi_daProdurre]

                for i in range(0, quanti):
                    id = request.form['prodotto-'+str(i)]

                    if int(id) not in semi_daProdurre:
                        newProd = Produzione(Data_Produzione=request.form['data'], Id_Semilavorato=id, Quantità=request.form['quantita-'+str(i)])
                        db.session.add(newProd)
                    else:
                        Produzione.query.filter(Produzione.Data_Produzione == request.form['data']).\
                            filter(Produzione.Id_Semilavorato == id).\
                            update({'Quantità' : Produzione.Quantità + request.form['quantita-'+str(i)]})

                db.session.commit()

                return redirect(url_for('produzione.produzioneGestionale'))

    return render_template("gestionale/formProduzione.html", Semi = semi, Quantita = quantita)