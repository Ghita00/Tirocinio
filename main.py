from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("/prova")

@app.route("/prova")
def prova():
    return render_template("page-login.html")

if __name__ == "__main__":
    app.run(debug=True)