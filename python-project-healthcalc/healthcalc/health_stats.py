from abc import ABC, abstractmethod

class HealthStats(ABC):
    @abstractmethod
    def alturaMedia(self) -> float: pass

    @abstractmethod
    def pesoMedio(self) -> float: pass

    @abstractmethod
    def imcMedio(self) -> float: pass

    @abstractmethod
    def numSexoH(self) -> int: pass

    @abstractmethod
    def numSexoM(self) -> int: pass

    @abstractmethod
    def numTotalPacientes(self) -> int: pass