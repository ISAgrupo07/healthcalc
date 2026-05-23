from healthcalc.health_calc_decorator import HealthCalcDecorator
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.person import Person
from healthcalc.patient import Patient

# factores de conversion
LB_A_KG = 0.45359237
KG_A_LB = 1 / LB_A_KG
IN_A_CM = 2.54
IN_A_M = 0.0254

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

errores_us = {
    "Weight must be within a possible biological range [1-700] kg.":
        "Weight must be within a possible biological range [2.20-1543.24] lb.",
    "Height must be within a possible biological range [0.30-3.00] m.":
        "Height must be within a possible biological range [11.81-118.11] in.",
    "Height must be within a possible biological range [30-300] cm.":
        "Height must be within a possible biological range [11.81-118.11] in.",
    "Oxigen saturation rate must be between 20 - 50 ºC.":
        "Temperature must be between 68 - 122 ºF.",
}

def adaptar_error(msg):
    if msg in errores_us:
        return errores_us[msg]
    return msg

class UnitDecorator(HealthCalcDecorator):
    sistema = "eu"

class EuropeanUnit(UnitDecorator):
    sistema = "eu"

class AmericanUnit(UnitDecorator):
    sistema = "us"

    def bmi(self, person: Person):
        peso_kg = person.weight() * LB_A_KG
        altura_m = person.height() * IN_A_M
        
        paciente_convertido = Patient(peso_kg, altura_m, person.gender(), person.age())
        
        try:
            return self.calc.bmi(paciente_convertido)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(adaptar_error(str(e)))

    def ibw(self, person: Person):
        altura_m = person.height() * IN_A_M
        
        paciente_convertido = Patient(person.weight(), altura_m, person.gender(), person.age())
        
        try:
            resultado_kg = self.calc.ibw(paciente_convertido)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(adaptar_error(str(e)))
        return resultado_kg * KG_A_LB

    def news2(self, frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp):
        temp_c = fahrenheit_a_celsius(temp)
        try:
            return self.calc.news2(frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp_c)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(adaptar_error(str(e)))
