from flask import Blueprint, render_template

documenti = Blueprint('documenti', __name__)

@documenti.route('/prova3')
def index():
    return render_template("sito/about.html")