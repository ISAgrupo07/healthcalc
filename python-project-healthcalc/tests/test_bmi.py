import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.BMICategory import BMICategory
from healthcalc.patient import Patient  
from healthcalc.gender import Gender    


class TestBMI:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    def test_bmi_valido(self):
        weight = 70.0
        height = 1.75
        expected_bmi = 70.0 / (1.75 ** 2)

        person = Patient(weight, height, Gender.MALE, 30)
        result = self.health_calc.bmi(person)

        assert result == pytest.approx(expected_bmi, abs=0.01)

    def test_bmi_peso_cero(self):
        person = Patient(0.0, 1.70, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    def test_bmi_altura_cero(self):
        person = Patient(70.0, 0.0, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    def test_bmi_negativos(self):
        person1 = Patient(-70.0, 1.70, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person1)

        person2 = Patient(70.0, -1.70, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person2)


    @pytest.mark.parametrize("weight", [-10.0, 0.0, 0.99], ids=lambda x: f"Peso mínimo inválido: {x}kg")
    def test_peso_minimo_imposible(self, weight: float):
        person = Patient(weight, 1.70, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    @pytest.mark.parametrize("weight", [700.1, 1000.0, 5000.0], ids=lambda x: f"Peso máximo inválido: {x}kg")
    def test_peso_maximo_imposible(self, weight: float):
        person = Patient(weight, 1.70, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    @pytest.mark.parametrize("height", [-0.50, 0.0, 0.29], ids=lambda x: f"Altura mínima inválida: {x}m")
    def test_altura_minima_imposible(self, height: float):
        person = Patient(70.0, height, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        person = Patient(70.0, height, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi(person)

    
    def test_bmi_severe_thinness(self):
        person = Patient(15.5, 1.0, Gender.MALE, 30) 
        assert self.health_calc.bmi_classification(person).name == "SEVERE_THINNESS"

    def test_bmi_moderate_thinness(self):
        person = Patient(16.5, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "MODERATE_THINNESS"

    def test_bmi_mild_thinness(self):
        person = Patient(18.0, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "MILD_THINNESS"

    @pytest.mark.parametrize("bmi", [18.6, 22.0, 24.9, 24.99], ids=lambda x: f"BMI {x} -> Normal weight")
    def test_bmi_normal_weight(self, bmi: float):
        person = Patient(bmi, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "NORMAL"

    @pytest.mark.parametrize("bmi", [25.1, 27.5, 29.9, 29.99], ids=lambda x: f"BMI {x} -> Overweight")
    def test_bmi_overweight(self, bmi: float):
        person = Patient(bmi, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "OVERWEIGHT"

    def test_bmi_obese_class_i(self):
        person = Patient(32.5, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "OBESE_CLASS_I"

    def test_bmi_obese_class_ii(self):
        person = Patient(38.0, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "OBESE_CLASS_II"

    def test_bmi_obese_class_iii(self):
        person = Patient(45.0, 1.0, Gender.MALE, 30)
        assert self.health_calc.bmi_classification(person).name == "OBESE_CLASS_III"


    @pytest.mark.parametrize("bmi", [-50.0, -1.0, -0.01], ids=lambda x: f"BMI negativo: {x}")
    def test_bmi_classification_minimo_imposible(self, bmi: float):
        person = Patient(bmi, 1.0, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(person)

    @pytest.mark.parametrize("bmi", [150.1, 200.0, 500.0], ids=lambda x: f"BMI máximo extremo: {x}")
    def test_bmi_classification_maximo_imposible(self, bmi: float):
        person = Patient(bmi, 1.0, Gender.MALE, 30)
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(person)