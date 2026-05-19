import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender


class TestIBW:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica IBW ---
    def test_ibw_hombre_valido(self):
        """Cálculo de IBW con valores estándar válidos"""
        gender = Gender.MALE
        height = 180.0 # Hemos preferido utilizar centímetros para el cálculo de IBW, ya que es común en esta métrica.
        expected_ibw = (180.0 - 100) - ((180.0 - 150) / 4.0)

        result = self.health_calc.ibw(height, gender)

        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_mujer_valido(self):
        """Cálculo de IBW con valores estándar válidos"""
        gender = Gender.FEMALE
        height = 165.0
        expected_ibw = (165.0 - 100) - ((165.0 - 150) / 2.0)

        result = self.health_calc.ibw(height, gender)

        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_altura_cero(self):
        """Lanzar excepción cuando el peso es cero"""
        gender= Gender.MALE
        height = 0.0
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(height, gender)


    # --- Tests de Límites e Invalidación para el IBW ---
    @pytest.mark.parametrize("height", [-10.0, 0.0, 29.9], ids=lambda x: f"Altura mínima inválida: {x}cm")
    def test_altura_minima_imposible(self, height: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        gender = Gender.FEMALE

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(height, gender)

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        gender = Gender.MALE
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(height, gender)
