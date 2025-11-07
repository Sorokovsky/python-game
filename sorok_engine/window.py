from pygame import Surface, init
from pygame.display import set_mode, flip


class Window:
    _width: int
    _height: int
    _display: Surface

    def __init__(self: "Window", width: int = 1200, height: int = 800) -> None:
        init()
        self.set_width(width)
        self.set_height(height)
        self._setup_display()

    def set_width(self: "Window", width: int) -> None:
        self._width = width

    def set_height(self: "Window", height: int) -> None:
        self._height = height

    def _setup_display(self: "Window") -> None:
        self._display = set_mode((self._width, self._height))

    def draw(self: "Window") -> None:
        flip()
