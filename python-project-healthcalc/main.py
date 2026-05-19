from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_hospital_proxy import HealthHospitalProxy
from healthcalc.health_hospital_adapter import HealthHospitalAdapter
from healthcalc.language_decorator import SpanishLanguage, EnglishLanguage
from healthcalc.unit_decorator import EuropeanUnit, AmericanUnit
from healthcalc.gender import Gender
from healthcalc.BMICategory import BMICategory



def crear_calc(idioma, unidades):
    base = HealthCalcImpl.getInstance()
    if unidades == "us":
        base = AmericanUnit(base)
    else:
        base = EuropeanUnit(base)
    if idioma == "es":
        return SpanishLanguage(base)
    else:
        return EnglishLanguage(base)

def unidades_str(unidades):
    if unidades == "us":
        return {"peso": "lb", "altura": "in", "temp": "F"}
    return {"peso": "kg", "altura": "cm", "temp": "C"}

def print_menu(idioma, unidades):
    print("\n=== HealthCalc ===")
    print(f"[idioma={idioma} | unidades={unidades}]")
    if idioma == "es":
        print("1. Calcular IMC y Clasificación")
        print("2. Calcular Peso Corporal Ideal (IBW)")
        print("3. Calcular NEWS2")
        print("4. Simular sistema Hospital (Adapter)")
        print("5. Ver estadísticas Hospital (Proxy)")
        print("6. Cambiar idioma")
        print("7. Cambiar unidades")
        print("8. Salir")
    else:
        print("1. Calculate BMI & Classification")
        print("2. Calculate Ideal Body Weight (IBW)")
        print("3. Calculate NEWS2 Score")
        print("4. Hospital System Simulation (Adapter)")
        print("5. View Hospital Statistics (Proxy)")
        print("6. Change language")
        print("7. Change unit system")
        print("8. Exit")
    print("==================")

def main():
    idioma = "es"
    unidades = "eu"
    calc = crear_calc(idioma, unidades)
    hospital = HealthHospitalProxy()

    while True:
        u = unidades_str(unidades)
        print_menu(idioma, unidades)
        opcion = input("Opción: ")

        if opcion == "1":
            try:
                peso = float(input(f"Peso ({u['peso']}): "))
                altura = float(input(f"Altura ({u['altura'] if unidades == 'us' else 'm'}): "))
                # en EU pedimos metros igual que antes
                bmi_val = calc.bmi(peso, altura)
                clas = calc.bmi_classification(bmi_val).name
                print(f"\n-> BMI: {bmi_val:.2f} ({clas})")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "2":
            try:
                altura = float(input(f"Altura ({u['altura']}): "))
                genero = input("Género (hombre/mujer): ")
                if (genero=="man") or (genero=="m") or (genero=="hombre"):
                    genero = Gender.MALE
                elif (genero=="woman") or (genero=="w") or (genero=="f") or (genero=="mujer"):
                    genero = Gender.FEMALE
                ibw_val = calc.ibw(altura, genero)
                print(f"\n-> IBW: {ibw_val:.2f} {u['peso']}")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "3":
            try:
                resp = int(input("Frecuencia respiratoria (rpm): "))
                spo2 = int(input("SpO2 (%): "))
                supp_in = input("¿Oxígeno suplementario? (s/n): ").strip().lower()
                supp = supp_in in ["s", "si", "sí", "y", "yes", "1"]
                sis = int(input("Presión sistólica (mmHg): "))
                hr = int(input("Frecuencia cardiaca (lpm): "))
                consc = input("Consciencia (alerta/cvpu): ")
                temp = float(input(f"Temperatura ({u['temp']}): "))
                score = calc.news2(resp, spo2, supp, sis, hr, consc, temp)
                print(f"\n-> NEWS2: {score}")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "4":
            try:
                print("\n--- Hospital ---")
                print("1. Hospital BMI")
                print("2. Hospital IBW")
                sub = input("Opción (1-2): ").strip()
                if sub == "1":
                    altura = float(input("Altura en cm: "))
                    peso = int(input("Peso en Kg: "))
                    bmi, clas = hospital.indiceMasaCorporal(altura, peso)
                    print(f"\n[Hospital] IMC: {bmi:.2f} | {clas}")
                elif sub == "2":
                    genero = input("Género (man/woman): ")
                    altura = float(input("Altura en cm: "))
                    ibw_val = hospital.pesoCorporalIdeal(genero, altura)
                    print(f"\n[Hospital] IBW: {ibw_val} kg")
                else:
                    print("Opción inválida.")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "5":
            print("\n=== Estadísticas Hospital ===")
            total = hospital.numTotalPacientes()
            print(f"Total consultas: {total}")
            if total > 0:
                print(f"Altura media: {hospital.alturaMedia():.2f} cm")
                print(f"Peso medio: {hospital.pesoMedio():.2f} kg")
                print(f"IMC medio: {hospital.imcMedio():.2f}")
                print(f"Hombres: {hospital.numSexoH()}")
                print(f"Mujeres: {hospital.numSexoM()}")
            else:
                print("No hay datos todavía.")
            print("==============================")

        elif opcion == "6":
            nuevo = input("Idioma (es/en): ").strip().lower()
            if nuevo in ("es", "en"):
                idioma = nuevo
                calc = crear_calc(idioma, unidades)

        elif opcion == "7":
            nuevo = input("Unidades (eu/us): ").strip().lower()
            if nuevo in ("eu", "us"):
                unidades = nuevo
                calc = crear_calc(idioma, unidades)

        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
