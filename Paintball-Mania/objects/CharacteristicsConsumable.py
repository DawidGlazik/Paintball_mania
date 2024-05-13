from abc import abstractmethod
from . import Consumable


class CharacteristicsConsumable(Consumable):
    def __init__(self, position: list[int | float, int | float], ) -> None:
        super().__init__(position)

    @abstractmethod
    def effect(self) -> None:
        pass
