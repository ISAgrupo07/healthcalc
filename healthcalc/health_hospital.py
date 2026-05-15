from abc import ABC, abstractmethod

class HealthHospital(ABC):
    
    @abstractmethod
    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        pass

    @abstractmethod
    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        pass