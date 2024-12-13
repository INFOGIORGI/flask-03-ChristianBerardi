from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/Details")
def detail():
    return render_template("Details.html")


app.run(debug=True)
