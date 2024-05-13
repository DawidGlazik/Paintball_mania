from abc import abstractmethod
from . import Object


class Consumable(Object):
    @abstractmethod
    def __init__(self, position: list[int | float, int | float]) -> None:
        super().__init__(position)

    @abstractmethod
    def effect(self) -> None:
        pass
