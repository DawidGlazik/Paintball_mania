from abc import abstractmethod, ABCMeta


class Object(metaclass=ABCMeta):
    position: list[int | float, int | float]

    @abstractmethod
    def __init__(self, position: list[int | float, int | float]) -> None:
        self.position = position
