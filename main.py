from flask import Flask, render_template, request
from calendar import isleap
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/penkis_kartus/<zodis>")
def penkis_kartus(zodis):
    return render_template("penkis_kartus.html", zodis=zodis)

@app.route("/visikeliamieji/")
def visi_keliamieji():
    masyvas = list(filter(isleap, range(1900, 2101)))
    return render_template("visikeliamieji.html", masyvas=masyvas)

if __name__ == "__main__":
    app.run(debug=True)