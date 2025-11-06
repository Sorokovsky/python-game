import pygame


class Window:
    _width: int
    _height: int
    _display: pygame.Surface

    def __init__(self: "Window", width: int = 1200, height: int = 800) -> None:
        pygame.init()
        self.set_width(width)
        self.set_height(height)
        self._setup_display()

    def set_width(self: "Window", width: int) -> None:
        self._width = width

    def set_height(self: "Window", height: int) -> None:
        self._height = height

    def _setup_display(self: "Window") -> None:
        self._display = pygame.display.set_mode((self._width, self._height))

    def draw(self: "Window") -> None:
        pygame.display.flip()
