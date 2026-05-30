from abc import ABC, abstractmethod
from healthcalc.person import Person
from healthcalc.BMICategory import BMICategory



class BasalMetabolicIndex(ABC):

    @abstractmethod
    def bmi(self, person: Person) -> float:
        pass

    @abstractmethod
    def bmi_classification(self, person: Person) -> BMICategory:
        pass