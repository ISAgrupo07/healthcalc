from abc import ABC, abstractmethod
from healthcalc.person import Person



class IdealBodyWeight(ABC):

    @abstractmethod
    def ibw(self, person: Person) -> float:
        pass