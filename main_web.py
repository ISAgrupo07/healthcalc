from flask import Flask, render_template, request
from healthcalc.health_calc_impl import HealthCalcImpl

app = Flask(__name__)
calc = HealthCalcImpl.getInstance()

# Ruta principal (BMI por defecto)
@app.route("/")
def home():
    return render_template("index.html", active_tab="bmi")

# Ruta para BMI
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    result = None
    clasificacion = None
    error = None
    altura = None
    peso = None

    if request.method == "POST":
        try:
            altura = float(request.form["altura"])
            peso = float(request.form["peso"])
            bmi_value = calc.bmi(peso, altura / 100)
            result = bmi_value
            clasificacion = calc.bmi_classification(bmi_value)
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="bmi", altura=altura, peso=peso, result=result,
                           clasificacion=clasificacion, error=error)

# Ruta para IBW
@app.route("/ibw", methods=["GET", "POST"])
def ibw():
    result = None
    error = None
    altura = None
    sexo = None

    if request.method == "POST":
        try:
            altura = float(request.form["altura"])
            sexo = request.form["sexo"]
            result = calc.ibw(altura, sexo)
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="ibw", altura=altura, sexo=sexo, result=result, error=error)

# Ruta para NEWS2
@app.route("/news2", methods=["GET", "POST"])
def news2():
    result = None
    error = None
    frecResp = None
    oxSat = None
    oxSup = False
    preArtSis = None
    frecCard = None
    consciente = "alerta"
    temp = None

    if request.method == "POST":
        try:
            frecResp = int(request.form["frecResp"])
            oxSat = int(request.form["oxSat"])
            oxSup = "oxSup" in request.form
            preArtSis = int(request.form["preArtSis"])
            frecCard = int(request.form["frecCard"])
            consciente = request.form["consciente"]
            temp = float(request.form["temp"])

            result = calc.news2(frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp)
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="news2", frecResp=frecResp, oxSat=oxSat, oxSup=oxSup,
                           preArtSis=preArtSis, frecCard=frecCard, consciente=consciente, temp=temp, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)