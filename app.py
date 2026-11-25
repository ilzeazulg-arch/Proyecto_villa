from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", titulo="Inicio")

@app.route("/futbol")
def futbol():
    return render_template("futbol.html", titulo="Fútbol")

@app.route("/baloncesto")
def baloncesto():
    return render_template("baloncesto.html", titulo="Baloncesto")

@app.route("/voleibol")
def voleibol():
    return render_template("voleibol.html", titulo="Voleibol")

if __name__ == "__main__":
    app.run(debug=True)
