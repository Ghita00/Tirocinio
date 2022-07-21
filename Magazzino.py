from flask import Blueprint, render_template

magazzino = Blueprint('magazzino', __name__)

@magazzino.route('/prova3')
def index():
    return render_template("sito/about.html")