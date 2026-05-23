from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.person import Person
from healthcalc.BMICategory import BMICategory



class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi_classification(self, person: Person) -> BMICategory:
        """Calculate the BMI classification of a person."""
        pass

    @abstractmethod
    def bmi(self, person: Person) -> float:
        """Calculate the Body Mass Index (BMI)."""
        pass

    @abstractmethod
    def ibw(self, person: Person) -> float:
        """Calculate the Ideal Body Weight (IBW) based on Lorentz Formula."""
        pass

    @abstractmethod
    def news2(self, frecResp: float, oxSat: float, oxSup: bool, preArtSis: float, frecCard: float, consciente: str, temp: float) -> float:
        """Calculate NEWS2 score.
        
        :param frecResp: Respiratory rate (per minute)
        :param oxSat: Oxigen saturation (%)
        :param oxSup: Oxigen support (True/False)
        :param preArtSis: Systolic blood pressure (mmHg)
        :param frecCard: Heart rate (per minute)
        :param consciente: Concience level (cvpu/alert)
        :param temp: Temperature (ºC)
        :return: NEWS2 score
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
