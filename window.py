import pygame

from vector import Vector


class Window:
    _width: int
    _height: int

    def __init__(self: "Window", size: Vector) -> None:
        self.set_size(size)

    def set_size(self, size: Vector) -> None:
        self._width = size.get_width()
        self._height = size.get_height()

    def update_frame(self: "Window") -> None:
        pygame.display.set_mode((self._width, self._height))
        pygame.display.flip()
