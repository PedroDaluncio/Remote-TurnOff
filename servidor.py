import subprocess
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def html():
    """
    Função que renderiza o html inicial e serve como um GET.
    """
    return render_template("index.html")

@app.get("/turn_off")
def turn_off():
    """
    Função que espera uma requisição GET no caminho "turn_off". Ao receber
    a requisição, inicia o processo de desligar o computador.
    """
    if request.method == 'GET':
        return subprocess.run(["shutdown","-s"], check=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
