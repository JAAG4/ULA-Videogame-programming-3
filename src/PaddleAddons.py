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


class RocketLauncher(PaddleAddon):
    def __init__(
        self,
        x: int,
        y: int,
        paddle,
        side: Literal["left", "right"] = "left",
        quantity: int = 10,
        period: int = 2,
    ) -> None:
        super().__init__(x, y, paddle)
        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["powerups"]
        self.frame = 0
        self.rocket_factory = Factory(Rocket)
        self.offset_x = 0
        self.offset_y = 0
        self.side = side
        self.max_quantity = quantity
        self.period = period
        self.timer = 0

    def addon_action(self, *args, **kwargs):
        """
        SHOOT ROCKETS

        Expected Args:
            play_state : Current PlayState of the Game
        """
        play_state = None
        if args:
            play_state = args[0]
        elif kwargs.get("play_state"):
            play_state = kwargs.get("play_state")
        else:
            raise ValueError("COULD NOT GET PLAY STATE")
        paddle = play_state.paddle
        for _ in range(self.max_quantity):
            # * Spawn Left Rocket
            # $ Spawn
            r_left = self.rocket_factory.create(paddle.x - 16, paddle.y - 8)
            settings.SOUNDS["rocket_launch"].stop()
            settings.SOUNDS["rocket_launch"].play()
            # $ Move
            r_left.vy = -200
            r_left.vx = -1

            # * Spawn Right Rocket
            # $ Spawn
            r_right = self.rocket_factory.create(paddle.x + paddle.width, paddle.y - 8)
            # $ Move
            r_right.vy = -200
            r_right.vx = -1
            # * De-Spawn Powerup
            # * Add Rockets to Ball List
            play_state.balls.append(r_left)
            play_state.balls.append(r_right)
            # raise NotImplementedError()
        self.in_play = False

    def update(self, *args, **kwargs) -> NoReturn:
        self.timer += kwargs.get("dt", 0)
        if self.side == "left":
            self.offset_x = -16
        else:
            self.offset_x = self.paddle.width
        super().update()


class StickyPaddle(PaddleAddon):
    def __init__(
        self,
        x: int,
        y: int,
        paddle,
        offset_x: int = 0,
        offset_y: int = -2,
        play_state=None,
    ) -> None:
        super().__init__(x, y, paddle, offset_x, offset_y)
        self.stuck_balls = []
        self.play_state = play_state
        self.width = paddle.width + 1
        self.height = paddle.height + 2
        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"][0][paddle.size]

    def update(self, *args, **kwargs) -> NoReturn:
        self.width = self.paddle.width
        self.height = self.paddle.height
        for ball in self.play_state.balls:
            if ball.collides(self) and not isinstance(ball, Rocket):
                self.stuck_balls.append([ball, (self.x - ball.x)])
        for ball in self.stuck_balls:
            ball[0].vx = 0
            ball[0].vy = 0
            ball[0].x = self.x - ball[1]
        super().update(*args, **kwargs)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, surface):
        pass

    def addon_action(self, *args, **kwargs):
        for ball in self.stuck_balls:
            ball[0].vx = randint(-80, 80)
            ball[0].vy = randint(-170, -100)
        self.stuck_balls = []
        self.in_play = False
