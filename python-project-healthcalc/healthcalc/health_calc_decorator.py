from healthcalc.health_calc import HealthCalc
from healthcalc.person import Person

class HealthCalcDecorator(HealthCalc):

    def __init__(self, calc):
        self.calc = calc

    def bmi(self, person: Person):
        return self.calc.bmi(person)

    def bmi_classification(self, person: Person):
        return self.calc.bmi_classification(person)

    def ibw(self, person: Person):
        return self.calc.ibw(person)

    def news2(self, frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp):
        return self.calc.news2(frecResp, oxSat, oxSup, preArtSis, frecCard, consciente, temp)
