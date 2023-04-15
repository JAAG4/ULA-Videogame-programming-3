"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Paddle.
"""
import pygame

import settings


class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 64
        self.height = 16

        # By default, the blue paddle
        self.skin = 0

        # By default, the 64-pixels-width paddle.
        self.size = 1

        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"]

        # The paddle only move horizontally
        self.vx = 0

        self.addons = []

    def resize(self, size: int) -> None:
        self.size = size
        self.width = (self.size + 1) * 32

    def dec_size(self):
        self.resize(max(0, self.size - 1))

    def inc_size(self):
        self.resize(min(3, self.size + 1))

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float, *args, **kwargs) -> None:
        next_x = self.x + self.vx * dt
        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)
        self.addons = [addon for addon in self.addons if addon.in_play]
        for obj in self.addons:
            obj.update(dt=dt, play_state=kwargs.get("play_state"))

    def render(self, surface: pygame.Surface, *args, **kwargs) -> None:
        surface.blit(self.texture, (self.x, self.y), self.frames[self.skin][self.size])
        surface.blit(
            self.texture,
            (self.x, self.y),
            self.frames[self.skin][self.size],
            special_flags=kwargs.get("blend_mode", 0),
        )
        self.addons = [addon for addon in self.addons if addon.in_play]
        for obj in self.addons:
            obj.render(surface, *args, **kwargs)
