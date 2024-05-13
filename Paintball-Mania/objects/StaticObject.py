from abc import abstractmethod
from . import Object


class StaticObject(Object):
    health: int
    endurance: int
    resistance: int

    @abstractmethod
    def __init__(self, position: list[int | float, int | float], health: int, endurance: int, resistance: int) -> None:
        super().__init__(position)
        self.health = health
        self.endurance = endurance
        self.resistance = resistance
