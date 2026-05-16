from healthcalc.health_hospital import HealthHospital
from healthcalc.health_stats import HealthStats
from healthcalc.health_hospital_adapter import HealthHospitalAdapter

class HealthHospitalProxy(HealthHospital, HealthStats):
    def __init__(self):
        self._hospitalService = HealthHospitalAdapter()
        self._historial = []

    def checkAccess(self) -> bool:
        return True

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        if not self.checkAccess():
            raise PermissionError("Access denied")
        resultado = self._hospitalService.indiceMasaCorporal(altura, peso)
        self._historial.append({
            'altura': altura,
            'peso': peso,
            'imc': resultado[0],
            'sexo': None
        })
        return resultado

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        if not self.checkAccess():
            raise PermissionError("Access denied")
        resultado = self._hospitalService.pesoCorporalIdeal(genero, altura)
        self._historial.append({
            'altura': altura,
            'peso': resultado,
            'imc': None,
            'sexo': genero
        })
        return resultado

    def numTotalPacientes(self) -> int:
        return len(self._historial)

    def alturaMedia(self) -> float:
        if not self._historial:
            return 0.0
        return sum(p['altura'] for p in self._historial) / len(self._historial)

    def pesoMedio(self) -> float:
        if not self._historial:
            return 0.0
        return sum(p['peso'] for p in self._historial) / len(self._historial)

    def imcMedio(self) -> float:
        imcs = [p['imc'] for p in self._historial if p['imc'] is not None]
        if not imcs:
            return 0.0
        return sum(imcs) / len(imcs)

    def numSexoH(self) -> int:
        return len([p for p in self._historial if p['sexo'] in ['man', 'hombre', 'H']])

    def numSexoM(self) -> int:
        return len([p for p in self._historial if p['sexo'] in ['woman', 'mujer', 'M']])