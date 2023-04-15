"""
ISPPJ1 2023
Study Case: Breakout

Author: José Agelvis
jalagut@gmail.com

This file contains the class Rocket Launcher, Which is an Addon to the Pallet
"""
import pygame
import settings
from typing import NoReturn
from gale.factory import Factory
from src.Rocket import Rocket
from typing import Any, Literal
from functools import partial
from random import randint


class PaddleAddon:
    def __init__(
        self, x: int, y: int, paddle, offset_x: int = 0, offset_y: int = 0
    ) -> None:
        self.paddle = paddle
        self.x = x
        self.y = y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.width = 16
        self.height = 16
        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["powerups"]
        self.frame = 0
        self.do_render = True
        self.in_play = True

    def update(self, *args, **kwargs) -> NoReturn:
        self.x = self.paddle.x + self.offset_x
        self.y = self.paddle.y + self.offset_y

    def render(self, surface: pygame.Surface, *args, **kwargs) -> NoReturn:
        if self.do_render:
            surface.blit(
                self.texture,
                (self.x, self.y),
                self.frames[self.frame],
                special_flags=kwargs.get("blend_mode", 0),
            )

    def addon_action(self, *args, **kwargs):
        pass

