"""
ISPPJ1 2023
Study Case: Breakout

Author: José Agelvis
jalagut@gmail.com

This file contains the specialization of PowerUp to activate the Sticky Paddle
"""
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp
from src.PaddleAddons import StickyPaddle as StickyPaddleAddon


class StickyPaddle(PowerUp):
    def __init__(self, x: int, y: int, frame: int = 4, play_state=None) -> None:
        self.play_state = play_state
        super().__init__(x, y, frame)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle
        paddle.addons.append(
            StickyPaddleAddon(
                x=paddle.x, y=paddle.y, paddle=paddle, play_state=play_state
            )
        )
        self.in_play = False
