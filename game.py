import pygame

from vector import Vector
from window import Window


class Game:
    _window: Window
    _is_running: bool

    def __init__(self: "Game") -> None:
        self._window = Window(Vector(1200, 800))
        self._is_running = False

    def set_size(self: "Game", size: Vector) -> None:
        self._window.set_size(size)
        self._is_running = True

    def start(self: "Game") -> None:
        self._is_running = True
        self.loop()

    def loop(self: "Game") -> None:
        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
