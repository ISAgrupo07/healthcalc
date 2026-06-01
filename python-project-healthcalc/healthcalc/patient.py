from healthcalc.person import Person
from healthcalc.gender import Gender

class Patient(Person):
    
    def __init__(self, weight: float, height: float, gender: Gender, age: int):
        self._weight = weight
        self._height = height
        self._gender = gender
        self._age = age

    def weight(self) -> float:
        return self._weight

    def height(self) -> float:
        return self._height

    def gender(self) -> Gender:
        return self._gender

    def age(self) -> int:
        return self._age