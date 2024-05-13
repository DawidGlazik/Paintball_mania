from game_logic.Player import Player
from objects.Object import Object


class Board:
    fields: list[list[int | str | bool | None]]
    players: list[Player]
    objects: list[Object]

    def __init__(self, board_size):
        self.fields = [[None for _ in range(board_size)] for _ in range(board_size)]

