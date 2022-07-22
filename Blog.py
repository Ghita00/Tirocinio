from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blogRoute():
    return render_template("sito/blog.html")

@blog.route('/blog-details')
def blogDetailsRoute():
    return render_template("sito/blog-details.html")

#gestionale
@blog.route("/gestionale/blog")
def Gblog():
    return render_template("gestionale/")