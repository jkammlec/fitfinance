

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    labels = []
    data = []

    if request.method == "POST":
        # Obtener valores de los meses (si está vacío, usar 0)
        meses = [float(request.form.get(f"mes{i}", 0)) for i in range(1, 13)]
        tasa = float(request.form.get("tasa", 0)) / 100

        # Calcular crecimiento acumulado
        acumulado = 0
        for i, aporte in enumerate(meses, start=1):
            acumulado = (acumulado + aporte) * (1 + tasa)
            labels.append(f"Mes {i}")
            data.append(round(acumulado, 2))

        resultado = {
            "total_aportado": round(sum(meses), 2),
            "crecimiento_final": round(acumulado, 2),
            "labels": labels,
            "data": data
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)

