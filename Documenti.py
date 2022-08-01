from flask import Blueprint, render_template
from flask_login import current_user

documenti = Blueprint('documenti', __name__)

@documenti.route('/documentiGestionale')
def documentiGestionale():
    return render_template("gestionale/documenti.html")

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
