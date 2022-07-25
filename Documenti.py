from flask import Blueprint, render_template
from flask_login import current_user

documenti = Blueprint('documenti', __name__)

@documenti.route('/prova3')
def index():
    return render_template("sito/about.html", user = current_user.Nome)