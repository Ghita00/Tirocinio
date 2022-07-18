from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blogRoute():
    return render_template("sito/blog.html")

@blog.route('/blog_details')
def blog_details():
    return render_template("sito/blog-details.html")