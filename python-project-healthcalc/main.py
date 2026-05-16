from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_hospital_proxy import HealthHospitalProxy 
from healthcalc. health_hospital_adapter import HealthHospitalAdapter


def print_menu():
    print("\n=== HealthCalc ===")
    print("1. Calculate BMI & Classification")
    print("2. Calculate Ideal Body Weight (IBW)")
    print("3. Calculate NEWS2 Score")
    print("4. SIMULAR SISTEMA HOSPITAL (Patrón Adapter)")
    print("5. VER ESTADÍSTICAS DEL HOSPITAL (Patrón Proxy)")
    print("6. Exit")
    print("==================")

def main():

    calc = HealthCalcImpl.getInstance()
    #hospital_service = HealthHospitalAdapter()
    hospital_service = HealthHospitalProxy()
    while True:
        print_menu()
        choice = input("Select an option (1-6): ")
        
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
            try:
                altura_m = float(input("Hospital - Introduzca altura en cm: "))
                peso_g = int(input("Hospital - Introduzca peso en Kg: "))
                bmi, classification = hospital_service.indiceMasaCorporal(altura_m, peso_g)
                print(f"\n[Hospital API] -> IMC: {bmi:.2f} | Clasificación: {classification}")
            except Exception as e:
                print(f"\nError en la API del Hospital: {e}")

        elif choice == '5':
            print("\n=== ESTADÍSTICAS DEL SISTEMA (HealthStats) ===")
            total_pacientes = hospital_service.numTotalPacientes()
            print(f"Número total de consultas: {total_pacientes}")
            
            if total_pacientes > 0:
                print(f"Altura media de pacientes: {hospital_service.alturaMedia():.2f} cm")
                print(f"Peso medio de pacientes: {hospital_service.pesoMedio():.2f} kg")
                print(f"IMC medio registrado: {hospital_service.imcMedio():.2f}")
                print(f"Cantidad de hombres (H): {hospital_service.numSexoH()}")
                print(f"Cantidad de mujeres (M): {hospital_service.numSexoM()}")
            else:
                print("No hay datos registrados en el historial todavía. Realice consultas en la opción 4 primero.")
            print("==============================================")
        elif choice == '6':
            print("Exiting HealthCalc...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
