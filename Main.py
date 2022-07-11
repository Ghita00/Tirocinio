from flask import Flask, render_template, redirect
from GenDB import db
from flask_fontawesome import FontAwesome

#blueprint
from Profile import profile
from Ecommerce import ecommerce
from Blog import blog

app = Flask(__name__)
fa = FontAwesome(app) #serve per i font
db.create_all() #serve per il db

#registrazione blueprint
app.register_blueprint(profile, url_prefix = "")
app.register_blueprint(ecommerce, url_prefix = "")
app.register_blueprint(blog, url_prefix = "")

@app.route('/')
def hello_world():
    return render_template("sito/index.html")

if __name__ == "__main__":
    app.run(debug=True)