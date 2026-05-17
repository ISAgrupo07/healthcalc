from healthcalc.health_calc_decorator import HealthCalcDecorator
from healthcalc.exceptions import InvalidHealthDataException

# diccionarios de traduccion
traducciones_bmi = {
    "Severe thinness": "Delgadez severa",
    "Moderate thinness": "Delgadez moderada",
    "Mild thinness": "Delgadez leve",
    "Normal weight": "Peso normal",
    "Overweight": "Sobrepeso",
    "Obesity class I": "Obesidad clase I",
    "Obesity class II": "Obesidad clase II",
    "Obesity class III": "Obesidad clase III",
}

traducciones_errores = {
    "BMI cannot be negative.": "El IMC no puede ser negativo.",
    "BMI must be within a possible biological range [0-150].": "El IMC debe estar entre [0-150].",
    "Weight must be positive.": "El peso debe ser positivo.",
    "Height must be positive.": "La altura debe ser positiva.",
    "Weight must be within a possible biological range [1-700] kg.": "El peso debe estar entre [1-700] kg.",
    "Height must be within a possible biological range [0.30-3.00] m.": "La altura debe estar entre [0.30-3.00] m.",
    "Height must be within a possible biological range [30-300] cm.": "La altura debe estar entre [30-300] cm.",
    "Gender must be 'man' or 'woman'.": "El género debe ser 'hombre' o 'mujer'.",
    "Consciousness level must be 'alert'/'alerta' or 'cvpu'.": "El nivel de consciencia debe ser 'alerta' o 'cvpu'.",
    "Respiratory rate must be between 0 - 100 rpm.": "La frecuencia respiratoria debe estar entre 0 - 100 rpm.",
    "Oxigen saturation rate must be between 0 - 100 %.": "La saturación de oxígeno debe estar entre 0 - 100 %.",
    "Systolic blood pressure must be between 0 - 400 mmHg.": "La presión arterial sistólica debe estar entre 0 - 400 mmHg.",
    "Heart rate rate must be between 0 - 300 lpm.": "La frecuencia cardíaca debe estar entre 0 - 300 lpm.",
    "Oxigen saturation rate must be between 20 - 50 ºC.": "La temperatura debe estar entre 20 - 50 ºC.",
    "Weight must be within a possible biological range [2.20-1543.24] lb.": "El peso debe estar entre [2.20-1543.24] lb.",
    "Height must be within a possible biological range [11.81-118.11] in.": "La altura debe estar entre [11.81-118.11] in.",
    "Temperature must be between 68 - 122 ºF.": "La temperatura debe estar entre 68 - 122 ºF.",
}

class LanguageDecorator(HealthCalcDecorator):
    idioma = "en"

    def traducir(self, texto):
        return texto

    def traducir_error(self, msg):
        return msg

    def bmi(self, weight, height):
        try:
            return self.calc.bmi(weight, height)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(self.traducir_error(str(e)))

    def bmi_classification(self, bmi):
        try:
            res = self.calc.bmi_classification(bmi)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(self.traducir_error(str(e)))
        return self.traducir(res)

    def ibw(self, height_cm, gender):
        try:
            return self.calc.ibw(height_cm, gender)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(self.traducir_error(str(e)))

    def news2(self, frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp):
        try:
            return self.calc.news2(frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp)
        except InvalidHealthDataException as e:
            raise InvalidHealthDataException(self.traducir_error(str(e)))

class EnglishLanguage(LanguageDecorator):
    idioma = "en"

class SpanishLanguage(LanguageDecorator):
    idioma = "es"

    def traducir(self, texto):
        if texto in traducciones_bmi:
            return traducciones_bmi[texto]
        return texto

    def traducir_error(self, msg):
        if msg in traducciones_errores:
            return traducciones_errores[msg]
        return msg
