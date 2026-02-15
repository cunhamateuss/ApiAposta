
import random

ODD_MIN = 1.80
ODD_MAX = 2.20

def escolher_aposta(jogos):
    candidatos = []

    for jogo in jogos:
        odd = jogo["odd1"]

        if ODD_MIN <= odd <= ODD_MAX:
            prob_modelo = round(random.uniform(0.60, 0.75), 2)
            implied_prob = round(1 / odd, 2)
            value = round(prob_modelo - implied_prob, 3)

            candidatos.append({
                "jogo": jogo["jogo"],
                "aposta": jogo["equipa1"],
                "odd": odd,
                "prob_modelo": prob_modelo,
                "value": value
            })

    if not candidatos:
        return {"mensagem": "Nenhuma aposta com valor hoje."}

    candidatos.sort(key=lambda x: x["value"], reverse=True)
    return candidatos[0]
