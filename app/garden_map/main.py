from flask import Flask, jsonify, render_template

app = Flask(__name__)

SERVICES = [
    {
        "name": "Projektowanie ogrodu",
        "lat": 50.0615,
        "lng": 19.9366,
        "description": "Opracowanie projektu i wizualizacji."
    },
    {
        "name": "Zakładanie trawnika",
        "lat": 50.062,
        "lng": 19.937,
        "description": "Kompleksowe zakładanie trawnika."
    },
    {
        "name": "System nawadniania",
        "lat": 50.061,
        "lng": 19.938,
        "description": "Montaż automatycznego nawadniania."
    },
    {
        "name": "Pielęgnacja",
        "lat": 50.0605,
        "lng": 19.935,
        "description": "Regularne prace pielęgnacyjne."
    },
    {
        "name": "Mała architektura",
        "lat": 50.0625,
        "lng": 19.9345,
        "description": "Budowa tarasów i ścieżek."
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/services")
def services():
    return jsonify(SERVICES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
