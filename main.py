from flask import Flask, render_template, redirect
from GenDB import db

app = Flask(__name__)

db.create_all()


@app.route('/')
def hello_world():
    return render_template("sito/about.html")

if __name__ == "__main__":
    app.run(debug=True)