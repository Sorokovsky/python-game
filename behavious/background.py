from pygame.event import Event
from pygame.key import ScancodeWrapper

from behavious.behaviour import Behaviour
from pygame import Surface
from pygame.transform import scale
from pygame.image import load
from constants.sizes import WIDTH, HEIGHT

class Background(Behaviour):
    _image_path: str = "images/background.png"
    _speed: int = 3
    _surface: Surface
    _first_position: int = 0
    _second_position: int

    def start(self: "Background") -> None:
        self._surface = scale(load(self._image_path), (WIDTH, HEIGHT))
        self._second_position = self._surface.get_width()

    def process_events(self: "Behaviour", events: list[Event]) -> None:
        pass

    def process_input(self: "Background", keys: ScancodeWrapper) -> None:
        pass

    def update(self: "Background") -> None:
        self._first_position -= self._speed
        self._second_position -= self._speed
        if self._first_position < -self._surface.get_width():
            self._first_position = self._surface.get_width()
        if self._second_position < -self._surface.get_width():
            self._second_position = self._surface.get_width()

    def render(self: "Background", parent_surface: Surface) -> None:
        parent_surface.blit(self._surface, (self._first_position, 0))
        parent_surface.blit(self._surface, (self._second_position, 0))
