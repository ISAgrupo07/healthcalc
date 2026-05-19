from flask import Flask, render_template, request, session, redirect, url_for
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.language_decorator import SpanishLanguage, EnglishLanguage
from healthcalc.unit_decorator import EuropeanUnit, AmericanUnit
from healthcalc.gender import Gender
from healthcalc.BMICategory import BMICategory


app = Flask(__name__)
app.secret_key = "clave-healthcalc"

def get_calc():
    base = HealthCalcImpl.getInstance()
    unidades = session.get("units", "eu")
    idioma = session.get("lang", "es")
    if unidades == "us":
        base = AmericanUnit(base)
    else:
        base = EuropeanUnit(base)
    if idioma == "es":
        return SpanishLanguage(base)
    return EnglishLanguage(base)

def contexto(**extra):
    lang = session.get("lang", "es")
    units = session.get("units", "eu")
    if units == "us":
        u = {"weight": "lb", "height": "in", "temp": "F"}
    else:
        u = {"weight": "kg", "height": "cm", "temp": "C"}
    ctx = {"lang": lang, "units": units, "u": u}
    ctx.update(extra)
    return ctx

@app.route("/settings", methods=["POST"])
def settings():
    lang = request.form.get("lang", "es")
    units = request.form.get("units", "eu")
    if lang in ("es", "en"):
        session["lang"] = lang
    if units in ("eu", "us"):
        session["units"] = units
    return redirect(request.referrer or url_for("home"))

@app.route("/")
def home():
    return render_template("index.html", active_tab="bmi", **contexto())

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
            calc = get_calc()
            # si esta en eu hay que pasar cm a m, en us no
            if session.get("units", "eu") == "eu":
                altura_calc = altura / 100
            else:
                altura_calc = altura
            bmi_value = calc.bmi(peso, altura_calc)
            result = bmi_value
            clasificacion = calc.bmi_classification(bmi_value).name
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="bmi", altura=altura, peso=peso,
                           result=result, clasificacion=clasificacion, error=error,
                           **contexto())

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
            if (sexo=="man") or (sexo=="m") or (sexo=="hombre"):
                sexo = Gender.MALE
            elif (sexo=="woman") or (sexo=="w") or (sexo=="f") or (sexo=="mujer"):
                sexo = Gender.FEMALE
            result = get_calc().ibw(altura, sexo)
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="ibw", altura=altura, sexo=sexo,
                           result=result, error=error, **contexto())

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
            result = get_calc().news2(frecResp, oxSat, oxSup, preArtSis,
                                      frecCard, consciente, temp)
        except Exception as e:
            error = str(e)

    return render_template("index.html", active_tab="news2", frecResp=frecResp, oxSat=oxSat,
                           oxSup=oxSup, preArtSis=preArtSis, frecCard=frecCard,
                           consciente=consciente, temp=temp, result=result, error=error,
                           **contexto())

if __name__ == "__main__":
    app.run(debug=True)
