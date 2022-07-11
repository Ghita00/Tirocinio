from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/prova4')
def index():
    return render_template("sito/about.html")