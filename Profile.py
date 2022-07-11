from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)

@profile.route('/login')
def login():
    return render_template("sito/login.html")




