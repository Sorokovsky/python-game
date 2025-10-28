import pygame

from color import Color
from vector import Vector


class GameObject:
    _size: Vector
    _position: Vector
    _color: Color
    _surface: pygame.Surface

    def __init__(self: "GameObject", size: Vector, position: Vector) -> None:
        self._size = size
        self._position = position
        self._surface = pygame.Surface((size.get_x(), size.get_y()))

    def set_color(self: "GameObject", color: Color) -> None:
        self._color = color
        self._surface.fill((color.get_r(), color.get_g(), color.get_b()))

    def get_surface(self: "GameObject") -> pygame.Surface:
        return self._surface

    def get_position(self: "GameObject") -> Vector:
        return self._position
