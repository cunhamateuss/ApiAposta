
from flask import Flask, render_template, jsonify
from scrapers.betano import get_betano_odds
from model import escolher_aposta
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    jogos = get_betano_odds()
    aposta = escolher_aposta(jogos)
    aposta["data"] = str(datetime.date.today())
    return render_template("index.html", aposta=aposta)

@app.route("/api/aposta")
def api_aposta():
    jogos = get_betano_odds()
    aposta = escolher_aposta(jogos)
    aposta["data"] = str(datetime.date.today())
    return jsonify(aposta)

if __name__ == "__main__":
    app.run()
