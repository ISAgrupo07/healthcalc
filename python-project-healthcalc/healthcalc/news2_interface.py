from abc import ABC, abstractmethod



class News2(ABC):

    @abstractmethod
    def news2(self, frecResp: float, oxSat: float, oxSup: bool, preArtSis: float, frecCard: float, consciente: str, temp: float) -> float:
        pass