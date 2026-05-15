from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_hospital import HealthHospital

class HealthHospitalAdapter(HealthHospital):
    
    def __init__(self):
        self._calculadora = HealthCalcImpl.getInstance()

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        altura_m = altura / 100.0
        peso_kg = float(peso)
        bmi_val = self._calculadora.bmi(peso_kg, altura_m)
        classification = self._calculadora.bmi_classification(bmi_val)
        return (bmi_val, classification)

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        ibw_val = self._calculadora.ibw(altura, genero)
        return int(ibw_val)
