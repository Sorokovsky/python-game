from pygame import Surface, Rect
from typing import Tuple
from pygame.event import Event, post
from pygame.key import ScancodeWrapper
from pygame.time import set_timer
from pygame.constants import K_DOWN, K_LEFT, K_UP, K_RIGHT
from os import listdir
from os.path import join

from behavious.behaviour import Behaviour
from constants.events import GOOSE_ANIMATE, ENEMY_PLAYER_COLLIDED, STOP_GAME, PLAYER_MOVED
from constants.sizes import WIDTH, HEIGHT
from helpers.load_image import load_image


class Player(Behaviour):
    _size: Tuple[int, int] = (60, 25)
    _surface: Surface
    _default_speed: Tuple[int, int] = [0, 0]
    _speed: Tuple[int, int] = [0, 0]
    _speed_down: Tuple[int, int] = [0, 4]
    _speed_up: Tuple[int, int] = [0, -4]
    _speed_right: Tuple[int, int] = [4, 0]
    _speed_left: Tuple[int, int] = [-4, 0]
    _rect: Rect
    _goose_folder: str = "images/goose"
    _default_image_url: str = "images/player.png"
    _images: list[str]
    _animation_interval: int = 250
    _index: int = 0

    def start(self: "Player") -> None:
        self._images = listdir(self._goose_folder)
        set_timer(GOOSE_ANIMATE, self._animation_interval)
        self._surface = load_image(self._default_image_url, self._size)
        self._rect = self._surface.get_rect()
        post(Event(PLAYER_MOVED, {
            "player": self._rect
        }))

    def process_events(self: "Player", events: list[Event]) -> None:
        for event in events:
            if event.type == GOOSE_ANIMATE:
                self._index += 1
                if self._index >= len(self._images):
                    self._index = 0
            if event.type == ENEMY_PLAYER_COLLIDED:
                post(Event(STOP_GAME))

    def process_input(self: "Player", keys: ScancodeWrapper) -> None:
        if keys[K_DOWN] and self._rect.bottom < HEIGHT:
            self._speed = self._speed_down

        if keys[K_UP] and self._rect.top > 0:
            self._speed = self._speed_up

        if keys[K_LEFT] and self._rect.left > 0:
            self._speed = self._speed_left

        if keys[K_RIGHT] and self._rect.right < WIDTH:
            self._speed = self._speed_right

    def update(self: "Player") -> None:
        self._rect = self._rect.move(self._speed)
        self._speed = self._default_speed
        post(Event(PLAYER_MOVED, {
            "player": self._rect
        }))

    def render(self: "Player", parent_surface: Surface) -> None:
        self._surface = load_image(join(self._goose_folder, self._images[self._index]), self._size)
        parent_surface.blit(self._surface, self._rect)
