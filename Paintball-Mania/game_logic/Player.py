from . import Weapon


class Player:
    id: int
    position: list[int, int] | list[float, float]
    health: int
    stamina: int
    armor: int
    weapon: Weapon
    projectiles: list[list[int, int], int] | list[list[float, float], int]
    score: float
    player_status: bool
    lives: int
    time_to_respawn: float | int
