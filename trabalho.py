
import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "minha_carreira_futebol"


@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        treino = request.form.get("treino")
        clube = request.form.get("clube")
        jogo1 = request.form.get("jogo1")
        Jg2 = request.form.get("Jg2")

        # Escolha do treino
        if treino == "1":
            session["mensagem_treino"] = "Você treinou bastante!"

        elif treino == "2":
            session["mensagem_treino"] = (
                "Você descansou para o próximo jogo!"
            )

        # Escolha do clube
        if clube in ["1", "2", "3"]:

            if clube == "1":
                nome_clube = "Cruzeiro"

            elif clube == "2":
                nome_clube = "Corinthians"

            else:
                nome_clube = "Santos"

            session["nome_clube"] = nome_clube
            session["mensagem_clube"] = (
                f"Bem-vindo ao {nome_clube}!"
            )

        # Primeiro jogo
        if jogo1 == "1":
            session["mensagem_jogo1"] = (
                "Você chuta de primeira e marca seu primeiro gol! ⚽"
            )

        elif jogo1 == "2":
            session["mensagem_jogo1"] = (
                "Você dá um passe genial e consegue sua primeira assistência! 🎯"
            )

        elif jogo1 == "3":
            session["mensagem_jogo1"] = (
                "Você recua a bola e seu time perde o ritmo."
            )

        # Jogo importante
        if Jg2 in ["1", "2", "3"]:

            if Jg2 == "1":
                session["mensagem_jogo2"] = (
                    "Você dribla o goleiro e marca um golaço! ⚽"
                )

            elif Jg2 == "2":
                session["mensagem_jogo2"] = (
                    "Você dá um passe decisivo para o atacante! 🎯"
                )

            else:
                session["mensagem_jogo2"] = (
                    "Você recua a bola para organizar a jogada."
                )

            # Placar da partida
            gol_time = random.randint(0, 4)
            gol_rival = random.randint(0, 4)

            session["gol_time"] = gol_time
            session["gol_rival"] = gol_rival

            if gol_time > gol_rival:
                session["resultado_final"] = (
                    "Vitória! Seu time conquistou o título!"
                )

            elif gol_time == gol_rival:
                session["resultado_final"] = (
                    "Empate! A decisão continua."
                )

            else:
                session["resultado_final"] = (
                    "Derrota! Você terá outra chance."
                )

    # mensagem
    return render_template(
        "jogo.html",

        mensagem_treino=session.get("mensagem_treino", ""),
        mensagem_clube=session.get("mensagem_clube", ""),
        mensagem_jogo1=session.get("mensagem_jogo1", ""),
        mensagem_jogo2=session.get("mensagem_jogo2", ""),

        nome_clube=session.get("nome_clube", "Seu time"),
        gol_time=session.get("gol_time", 0),
        gol_rival=session.get("gol_rival", 0),
        resultado_final=session.get("resultado_final", "")
    )


@app.route("/numeros", methods=["GET", "POST"])
def numeros():

    if "gols" not in session:
        session["gols"] = None
        session["assistencias"] = None
        session["jogos"] = None
        session["titulos"] = None

    if request.method == "POST":
        opcao = request.form.get("opcao")

        # Gols
        if opcao == "gols":
            gols = random.randint(20, 1300)
            session["gols"] = gols

            if gols <= 50:
                session["mensagem"] = "😬 Você é um atacante ruim."
            elif gols <= 100:
                session["mensagem"] = "😐 Você é um atacante mediano."
            elif gols < 300:
                session["mensagem"] = "⚽ Você é um bom atacante!"
            elif gols < 500:
                session["mensagem"] = "🔥 Você é um ótimo atacante!"
            elif gols < 600:
                session["mensagem"] = "🌟 Você é um craque!"
            elif gols < 900:
                session["mensagem"] = "🏆 Você é um dos maiores atacantes da história!"
            elif gols < 1000:
                session["mensagem"] = "🐐 Você é uma lenda!"
            else:
                session["mensagem"] = "👑🐐 MELHOR DA HISTÓRIA!! ⚽🔥"

        # Assistências
        elif opcao == "assistencias":
            assistencias = random.randint(10, 500)
            session["assistencias"] = assistencias

            if assistencias <= 10:
                mensagem = "😬 Você quase não deu assistências."
            elif assistencias <= 50:
                mensagem = "😐 Você é um bom companheiro."
            elif assistencias < 100:
                mensagem = "🎯 Você é um ótimo garçom!"
            elif assistencias < 200:
                mensagem = "🔥 Você é um ótimo assistente!"
            elif assistencias < 300:
                mensagem = "🌟 Você é um dos melhores garçons!"
            elif assistencias < 400:
                mensagem = "🏆 Você é um mestre das assistências!"
            else:
                mensagem = "🐐 Você é uma lenda dos passes!"

            session["mensagem_assistencias"] = mensagem

        # Jogos
        elif opcao == "jogos":
            session["jogos"] = random.randint(10, 1300)

        # Títulos
        elif opcao == "titulos":
            titulos = random.randint(0, 50)
            session["titulos"] = titulos

            if titulos == 0:
                mensagem = "😢 Sem título."
            elif titulos <= 3:
                mensagem = "🥉 Poucos títulos!"
            elif titulos <= 10:
                mensagem = "🥈 Você é um jogador vencedor!"
            elif titulos <= 20:
                mensagem = "🥇 Você tem uma carreira vitoriosa!"
            elif titulos <= 30:
                mensagem = "🔥 Você é um campeão histórico!"
            elif titulos <= 40:
                mensagem = "👑 Você é um dos maiores campeões!"
            else:
                mensagem = "🐐🏆 Você é uma lenda do futebol!"

            session["mensagem_titulos"] = mensagem

    return render_template(
        "numeros.html",
        gols=session.get("gols"),
        assistencias=session.get("assistencias"),
        jogos=session.get("jogos"),
        titulos=session.get("titulos"),
        mensagem=session.get("mensagem", ""),
        mensagem_assistencias=session.get(
            "mensagem_assistencias", ""
        ),
        mensagem_titulos=session.get(
            "mensagem_titulos", ""
        )
    )




# Reiniciar a carreira inteira
@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
