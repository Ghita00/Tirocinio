from flask import Blueprint, render_template, request

produzione = Blueprint('produzione', __name__)

@produzione.route('/produzioneGestionale', methods=['GET', 'POST'])
def produzioneGestionale():
    return render_template("gestionale/produzioneGiornaliera.html")

@produzione.route('/addProduzione', methods=['GET', 'POST'])
def aggiungiProd():
    return render_template("gestionale/formProduzione.html")