from . import Projectile
from abc import ABC, abstractmethod, ABCMeta


class Weapon(metaclass=ABCMeta):
    mag_capacity: int
    ammo: int
    projectile: Projectile
    rate_of_fire: float
    name: str

    @abstractmethod
    def __init__(self,
                 mag_capacity: int, ammo: int, projectile: Projectile,
                 rate_of_fire: float, name: str):

        self.mag_capacity = mag_capacity
        self.ammo = ammo
        self.projectile = projectile
        self.rate_of_fire = rate_of_fire
        self.name = name

