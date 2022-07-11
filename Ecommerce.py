from flask import Blueprint, render_template

ecommerce = Blueprint('ecommerce', __name__)

@ecommerce.route('/prova3')
def index():
    return render_template("sito/about.html")
