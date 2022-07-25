from flask import Blueprint, render_template
from flask_login import current_user

magazzino = Blueprint('magazzino', __name__)

@magazzino.route('/prova3')
def index():
    return render_template("sito/about.html", user = current_user.Nome)