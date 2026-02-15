from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

def gerar_aposta():
    jogos = [
        {"jogo": "Porto vs Braga", "odd": 1.98},
        {"jogo": "Benfica vs Sporting", "odd": 2.05},
        {"jogo": "PSG vs Lyon", "odd": 1.91},
        {"jogo": "Real Madrid vs Sevilla", "odd": 2.02}
    ]

    jogo = random.choice(jogos)

    prob_modelo = round(random.uniform(0.60, 0.75), 2)
    implied_prob = round(1 / jogo["odd"], 2)

    return {
        "data": str(datetime.date.today()),
        "jogo": jogo["jogo"],
        "odd": jogo["odd"],
        "prob_modelo": prob_modelo,
        "value": round(prob_modelo - implied_prob, 3)
    }

@app.route("/")
def home():
    aposta = gerar_aposta()
    return render_template("index.html", aposta=aposta)

@app.route("/api/aposta")
def api_aposta():
    return jsonify(gerar_aposta())

if __name__ == "__main__":
    app.run()
