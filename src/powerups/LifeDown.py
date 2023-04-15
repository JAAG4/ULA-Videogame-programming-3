"""
ISPPJ1 2023
Study Case: Breakout

Author: José Agelvis
jalagut@gmail.com

This file contains the specialization of PowerUp
"""
import random
from typing import TypeVar, NoReturn

from gale.factory import Factory

import settings
from src.powerups.PowerUp import PowerUp


class LifeDown(PowerUp):
    """
    Power-Down to remove one life from the player
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3)

    def take(self, play_state: TypeVar("PlayState")) -> NoReturn:
        # * Remove Life
        play_state.lives -= 1
        # * PLay Sound
        settings.SOUNDS["power_down"].stop()
        settings.SOUNDS["power_down"].play()
        # * De-Load
        self.in_play = False
