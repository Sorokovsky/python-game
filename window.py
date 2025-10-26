import pygame

from vector import Vector


class Window:
    _width: int
    _height: int
    _display: pygame.Surface

    def __init__(self: "Window", size: Vector) -> None:
        self.set_size(size)

    def set_size(self, size: Vector) -> None:
        self._width = size.get_width()
        self._height = size.get_height()
        self._display = pygame.display.set_mode((self._width, self._height))

    def get_display(self: "Window") -> pygame.Surface:
        return self._display

    def update_frame(self: "Window") -> None:
        pygame.display.flip()
