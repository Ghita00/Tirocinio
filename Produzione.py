from flask import Blueprint, render_template, request

produzione = Blueprint('produzione', __name__)

@produzione.route('/produzioneGestionale', methods=['GET', 'POST'])
def produzioneGestionale():
    if request.method == "POST":
        giorniSettimana = [] #TODO LISTA GIORNI
        variazione = request.form["settimana"]
        # if(variazione == 1):
            # slider ricevuti avanti di 1
        # if(variazione == -1):
            # slider ricevuti indietro di 1
        return render_template("gestionale/produzioneGiornaliera.html")
    else:
        return render_template("gestionale/produzioneGiornaliera.html")