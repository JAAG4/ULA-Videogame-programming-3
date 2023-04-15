"""
ISPPJ1 2023
Study Case: Breakout

Author: José Agelvis
jalagut@gmail.com

This file contains a specialization of  the class Ball. To use as Rockets for the ROcket Powerup
"""
from src.Ball import Ball
import settings


class Rocket(Ball):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.texture = settings.TEXTURES["spritesheet"]
        self.frame = 1
        self.width = 16
        self.height = 16
        self.vx = 0
        self.vy = -10

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y), settings.FRAMES["powerups"][self.frame]
        )

    def push(self, *args):
        pass

    def solve_world_boundaries(self) -> None:
        r = self.get_collision_rect()
        if r.top < 0:
            self.in_play = False
