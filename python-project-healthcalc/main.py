from flask import Flask, render_template, request
import sys
from healthcalc.health_calc_impl import HealthCalcImpl

app = Flask(__name__)
calc = HealthCalcImpl()
@app.route("/")
def home():
    return render_template(
        "index.html",
        active_tab="bmi",
        altura=None,
        peso=None,
        result=None,
        clasificacion=None,
        error=None
    )


@app.route("/bmi", methods=["GET","POST"])
def bmi():
    altura = None
    peso = None
    result = None
    clasificacion = None
    error = None

    if request.method == "POST":
        try:
            altura = float(request.form["altura"])
            peso = float(request.form["peso"])

            bmi_value = calc.bmi(peso, altura/100)
            result = bmi_value
            clasificacion = calc.bmi_classification(bmi_value)

        except Exception as e:
            error = str(e)

    return render_template("index.html",
                           active_tab="bmi",
                           altura=altura,
                           peso=peso,
                           result=result,
                           clasificacion=clasificacion,
                           error=error)

@app.route("/ibw", methods=["GET","POST"])
def ibw():
    altura = None
    sexo = None
    result = None
    error = None

    if request.method == "POST":
        try:
            altura = float(request.form["altura"])
            sexo = request.form["sexo"]

            if sexo == "hombre":
                sexo = "man"
            else:
                sexo = "woman"

            result = calc.ibw(altura, sexo)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        active_tab="ibw",
        altura=altura,
        sexo=sexo,
        result=result,
        error=error
    )

@app.route("/news2", methods=["GET","POST"])
def news2():
    result = None
    error = None

    if request.method == "POST":
        try:
            resp = int(request.form["frecResp"])
            spo2 = int(request.form["oxSat"])
            supp = "oxSup" in request.form
            sys_bp = int(request.form["preArtSis"])
            hr = int(request.form["frecCard"])
            consc = request.form["consciente"]
            temp = float(request.form["temp"])

            result = calc.news2(resp, spo2, supp, sys_bp, hr, consc, temp)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        active_tab="news2",
        result=result,
        error=error
    )

def print_menu():
    print("\n=== HealthCalc ===")
    print("1. Calculate BMI & Classification")
    print("2. Calculate Ideal Body Weight (IBW)")
    print("3. Calculate NEWS2 Score")
    print("4. Exit")
    print("==================")

def main():
    calc = HealthCalcImpl()
    
    while True:
        print_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))
                bmi_val = calc.bmi(weight, height)
                classification = calc.bmi_classification(bmi_val)
                print(f"\n-> Result: Your BMI is {bmi_val:.2f} ({classification})")
            except Exception as e:
                print(f"\nError: {e}")
                
        elif choice == '2':
            try:
                height = float(input("Enter height (cm): "))
                gender = input("Enter gender (man/woman): ")
                ibw_val = calc.ibw(height, gender)
                print(f"\n-> Result: Your Ideal Body Weight is {ibw_val:.2f} kg")
            except Exception as e:
                print(f"\nError: {e}")
                
        elif choice == '3':
            try:
                resp = int(input("Enter Respiration Rate (bpm): "))
                spo2 = int(input("Enter SpO2 (%): "))
                supp_input = input("Are you on supplemental oxygen? (yes/no): ").strip().lower()
                supp = supp_input in ['yes', 'y', 'true', '1']
                sys_bp = int(input("Enter Systolic BP (mmHg): "))
                hr = int(input("Enter Heart Rate (bpm): "))
                consc = input("Enter Level of Consciousness (alert/cvpu): ")
                temp = float(input("Enter Body Temperature (°C): "))
                
                score = calc.news2(resp, spo2, supp, sys_bp, hr, consc, temp)
                print(f"\n-> Result: Your NEWS2 Score is {score}")
            except Exception as e:
                print(f"\nError: {e}")
                
        elif choice == '4':
            print("Exiting HealthCalc...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    app.run(debug=True)