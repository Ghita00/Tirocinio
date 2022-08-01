from flask import Blueprint, render_template


produzione = Blueprint('produzione', __name__)

@produzione.route('/produzioneGestionale')
def produzioneGestionale():
    return render_template("gestionale/produzioneGiornaliera.html")