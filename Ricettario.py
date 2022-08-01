from flask import Blueprint, render_template
from flask_login import current_user

ricettario = Blueprint('ricettario', __name__)

@ricettario.route('/ricettarioGestionale')
def ricettarioGestionale():
    return render_template("gestionale/ricettario.html")