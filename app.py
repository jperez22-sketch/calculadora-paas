import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            numero1 = float(request.form["numero1"])
            numero2 = float(request.form["numero2"])
            operacion = request.form["operacion"]

            if operacion == "suma":
                resultado = numero1 + numero2
            elif operacion == "resta":
                resultado = numero1 - numero2
            elif operacion == "multiplicacion":
                resultado = numero1 * numero2
            elif operacion == "division":
                if numero2 == 0:
                    error = "No se puede dividir entre cero."
                else:
                    resultado = numero1 / numero2
        except (ValueError, KeyError):
            error = "Ingresa valores numéricos válidos."

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
