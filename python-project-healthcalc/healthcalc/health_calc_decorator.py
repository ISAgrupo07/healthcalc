from healthcalc.health_calc import HealthCalc

class HealthCalcDecorator(HealthCalc):

    def __init__(self, calc):
        self.calc = calc

    def bmi(self, weight, height):
        return self.calc.bmi(weight, height)

    def bmi_classification(self, bmi):
        return self.calc.bmi_classification(bmi)

    def ibw(self, height_cm, gender):
        return self.calc.ibw(height_cm, gender)

    def news2(self, frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp):
        return self.calc.news2(frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp)
