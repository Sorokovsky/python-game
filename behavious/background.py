from behavious.behaviour import Behaviour
from pygame import Surface
from pygame.transform import scale
from pygame.image import load
from constants.sizes import WIDTH, HEIGHT

class Background(Behaviour):
    _image_path: str = "images/background.png"
    _surface: Surface
    _first_position: int
    _second_position: int

    def start(self: "Background") -> None:
        self._surface = scale(load(self._image_path), (WIDTH, HEIGHT))
