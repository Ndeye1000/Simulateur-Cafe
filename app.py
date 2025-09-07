from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def bonjour():
    genre = request.args['g']
    prenom = request.args['p']
    commande = request.args['c']
    return render_template("index.html", genre=genre, prenom=prenom, commande=commande)

if __name__ == '__main__' :
    app.run(debug=True)