from flask import Flask, render_template

app = Flask(__name__)

lista=(("Speck", "SC1", 2), ("Pesto", "SC2", 1.50), ("Baiocchi", "SC3", 3), ("Pangocciolo", "SC3", 3))

@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/Details")
def detail():
    return render_template("Details.html", lista=lista)

@app.route("/Scaffale/<nScaff>")
def scaffale(nScaff):
    lista2=[]
    for i in lista:
        if i[1]==nScaff:
            lista2.append(i)
    return render_template("Scaffale.html", lista2=lista2, nScaff=nScaff)
   
app.run(debug=True)
