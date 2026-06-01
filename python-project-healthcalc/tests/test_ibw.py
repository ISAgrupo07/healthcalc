import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.patient import Patient


class TestIBW:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    def test_ibw_hombre_valido(self):
        """Cálculo de IBW con valores estándar válidos"""
        gender = Gender.MALE
        height_cm = 180.0 
        expected_ibw = (height_cm - 100) - ((height_cm - 150) / 4.0)

        person = Patient(0.0, height_cm / 100, gender, 30)
        result = self.health_calc.ibw(person)

        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_mujer_valido(self):
        """Cálculo de IBW con valores estándar válidos"""
        gender = Gender.FEMALE
        height_cm = 165.0
        expected_ibw = (height_cm - 100) - ((height_cm - 150) / 2.0)

        person = Patient(0.0, height_cm / 100, gender, 30)
        result = self.health_calc.ibw(person)

        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_altura_cero(self):
        """Lanzar excepción cuando el peso es cero"""
        gender = Gender.MALE
        height_m = 0.0
        person = Patient(0.0, height_m, gender, 30)
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(person)


    @pytest.mark.parametrize("height_cm", [-10.0, 0.0, 29.9], ids=lambda x: f"Altura mínima inválida: {x}cm")
    def test_altura_minima_imposible(self, height_cm: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        gender = Gender.FEMALE
        
        person = Patient(0.0, height_cm / 100, gender, 30)

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(person)

    @pytest.mark.parametrize("height_m", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height_m: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        gender = Gender.MALE
        
        person = Patient(0.0, height_m, gender, 30)
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(person)