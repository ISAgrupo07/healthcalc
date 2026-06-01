from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_hospital import HealthHospital
from healthcalc.gender import Gender
from healthcalc.patient import Patient


class HealthHospitalAdapter(HealthHospital):
    
    def __init__(self):
        self._calculadora = HealthCalcImpl.getInstance()

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        altura_m = altura / 100.0
        peso_kg = float(peso)
        from healthcalc.gender import Gender 
        persona_bmi = Patient(peso_kg, altura_m, Gender.MALE, 30)
        
        bmi_val = self._calculadora.bmi(persona_bmi)
        classification = self._calculadora.bmi_classification(persona_bmi)
        return (bmi_val, classification)

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        altura_m = altura / 100.0  
        from healthcalc.gender import Gender
        enum_gender = Gender.MALE if genero.lower() in ['man', 'hombre', 'h'] else Gender.FEMALE
        
        persona_ibw = Patient(0.0, altura_m, enum_gender, 30)
        ibw_val = self._calculadora.ibw(persona_ibw)
        return int(ibw_val)
