import pygame

from vector import Vector
from game_object import GameObject


class Window:
    _width: int
    _height: int
    _display: pygame.Surface

    def __init__(self: "Window", size: Vector) -> None:
        self.set_size(size)

    def set_size(self, size: Vector) -> None:
        self._width = size.get_x()
        self._height = size.get_y()
        self._display = pygame.display.set_mode((self._width, self._height))

    def draw(self: "Window", game_object: GameObject) -> None:
        x = game_object.get_position().get_x()
        y = game_object.get_position().get_y()
        self._display.blit(game_object.get_surface(), (x, y))

