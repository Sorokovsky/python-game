from vector import Vector
from window import Window


class Game:
    _window: Window

    def __init__(self: "Game") -> None:
        self._window = Window(Vector(1200, 800))

    def set_size(self: "Game", size: Vector) -> None:
        self._window.set_size(size)
