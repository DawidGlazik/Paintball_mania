from . import Consumable
class PointConsumable(Consumable):
    def __init__(self, position: list[int | float, int | float]) -> None:
        super().__init__(position)

    def effect(self) -> None:
        pass
