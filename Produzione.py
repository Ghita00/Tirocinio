from flask import Blueprint, render_template, request

produzione = Blueprint('produzione', __name__)

@produzione.route('/produzioneGestionale', methods=['GET', 'POST'])
def produzioneGestionale():

    return render_template("gestionale/produzioneGiornaliera.html")