import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestNEWS2:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica NEWS2 ---
    def test_news2_paciente_sano(self):
        """Cálculo de NEWS2 con valores estándar válidos de paciente sano"""
        respiratory_rate = 16
        oxygen_saturation = 98
        oxygen_support = False
        systolic_blood_pressure = 120
        heart_rate = 70
        level_of_consciousness = "alert"
        temperature = 37.0

        result = self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
            systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

        assert result == 0

    def test_news2_paciente_observacion(self):
        """Cálculo de NEWS2 para paciente en observación"""
        respiratory_rate = 22
        oxygen_saturation = 94
        oxygen_support = False
        systolic_blood_pressure = 105
        heart_rate = 115
        level_of_consciousness = "alert"
        temperature = 37.0

        result = self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
            systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

        assert result == 6

    def test_news2_paciente_observacion_alternativo(self):
        """Cálculo de NEWS2 para paciente en observación (hecho para cubrir 100% de los casos)"""
        respiratory_rate = 10
        oxygen_saturation = 92
        oxygen_support = False
        systolic_blood_pressure = 95
        heart_rate = 45
        level_of_consciousness = "alert"
        temperature = 35.5

        result = self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
            systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

        assert result == 7
    
    
    def test_news2_paciente_critico(self):
        """Cálculo de NEWS2 con valores estándar válidos de paciente crítico"""
        respiratory_rate = 5
        oxygen_saturation = 85
        oxygen_support = True
        systolic_blood_pressure = 80
        heart_rate = 35
        level_of_consciousness = "cvpu"
        temperature = 34.5

        result = self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
            systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

        assert result == 20

    # --- Tests de Límites e Invalidación para NEWS2 ---
    @pytest.mark.parametrize("respiration_rate", [-10, -1, 101, 150], ids=lambda x: f"Frecuencia respiratoria inválida: {x} rpm")
    def test_frecuencia_respiratoria_imposible(self, respiration_rate: int):
        """Lanzar excepción cuando la frecuencia respiratoria está fuera del rango 0-100."""
        oxygen_saturation = 98
        oxygen_support = False
        systolic_blood_pressure = 120
        heart_rate = 70
        level_of_consciousness = "alert"
        temperature = 37.0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiration_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

    @pytest.mark.parametrize("oxygen_saturation", [-5, -1, 101, 200], ids=lambda x: f"SpO2 inválido: {x}%")
    def test_saturacion_oxigeno_imposible(self, oxygen_saturation: int):
        """Lanzar excepción cuando la saturación de oxígeno está fuera del rango 0-100."""
        respiratory_rate = 16
        oxygen_support = False
        systolic_blood_pressure = 120
        heart_rate = 70
        level_of_consciousness = "alert"
        temperature = 37.0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

    @pytest.mark.parametrize("systolic_blood_pressure", [-20, -1, 401, 500], ids=lambda x: f"Presión sistólica inválida: {x} mmHg")
    def test_presion_sistolica_imposible(self, systolic_blood_pressure: int):
        """Lanzar excepción cuando la presión sistólica está fuera del rango 0-400."""
        respiratory_rate = 16
        oxygen_saturation = 98
        oxygen_support = False
        heart_rate = 70
        level_of_consciousness = "alert"
        temperature = 37.0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

    @pytest.mark.parametrize("heart_rate", [-10, -1, 301, 400], ids=lambda x: f"Frecuencia cardíaca inválida: {x} lpm")
    def test_frecuencia_cardiaca_imposible(self, heart_rate: int):
        """Lanzar excepción cuando la frecuencia cardíaca está fuera del rango 0-300."""
        respiratory_rate = 16
        oxygen_saturation = 98
        oxygen_support = False
        systolic_blood_pressure = 120
        level_of_consciousness = "alert"
        temperature = 37.0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

    @pytest.mark.parametrize("temperature", [19.9, 0.0, 50.1, 60.0], ids=lambda x: f"Temperatura inválida: {x}ºC")
    def test_temperatura_imposible(self, temperature: float):
        """Lanzar excepción cuando la temperatura está fuera del rango 20-50."""
        respiratory_rate = 16
        oxygen_saturation = 98
        oxygen_support = False
        systolic_blood_pressure = 120
        heart_rate = 70
        level_of_consciousness = "alert"

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)

    @pytest.mark.parametrize("level_of_consciousness", ["conscinete", "1", ""], ids=lambda x: f"Nivel de conciencia inválido: {x}")
    def test_conciencia_invalido(self, level_of_consciousness: str):
        """Lanzar excepción cuando el nivel de conciencia no es válido."""
        respiratory_rate = 16
        oxygen_saturation = 98
        oxygen_support = False
        systolic_blood_pressure = 120
        heart_rate = 70
        temperature = 37.0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.news2(respiratory_rate, oxygen_saturation, oxygen_support, 
                systolic_blood_pressure, heart_rate, level_of_consciousness, temperature)