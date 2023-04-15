"""
ISPPJ1 2023
Study Case: Breakout

Author: José Agelvis
jalagut@gmail.com

This file contains the specialization of PowerUp
"""
import random
from typing import TypeVar, NoReturn


import settings
from src.Ball import Ball

from src.powerups.PowerUp import PowerUp
from src.PaddleAddons import RocketLauncher


class Rockets(PowerUp):
    """
    Power-up to gain RocketLaunchers temporarily
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 7)
        self.quantity = 4
        self.period = 2

    def take(self, play_state: TypeVar("PlayState")) -> NoReturn:
        paddle = play_state.paddle
        paddle.addons.append(
            RocketLauncher(x=paddle.x, y=paddle.y, paddle=paddle, side="left")
        )
        paddle.addons.append(
            RocketLauncher(
                x=paddle.x,
                y=paddle.y,
                paddle=paddle,
                side="right",
            )
        )
