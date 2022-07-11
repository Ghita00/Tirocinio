from flask import Flask, render_template, redirect
from GenDB import *
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app) #serve per i font

db.create_all()

@app.route('/')
def hello_world():
    return render_template("gestionale/table-row-select.html")

if __name__ == "__main__":
    app.run(debug=True)