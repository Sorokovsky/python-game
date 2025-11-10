from typing import Tuple
from random import randint

from pygame import Surface, Rect
from pygame.event import Event, post
from pygame.key import ScancodeWrapper
from pygame.time import set_timer

from behavious.behaviour import Behaviour
from constants.sizes import WIDTH, HEIGHT
from constants.events import PLAYER_MOVED, CREATE_BONUS, BONUS_PLAYER_COLLIDED
from helpers.load_image import load_image


class Bonuses(Behaviour):
    _size: Tuple[int, int] = (44, 74)
    _image_path: str = "images/bonus.png"
    _player: Rect | None = None
    _bonuses: list[list[Surface | Rect | list[int]]] = []
    _spawn_timeout: int = 250
    
    def start(self: "Bonuses") -> None:
        set_timer(CREATE_BONUS, self._spawn_timeout)

    def process_events(self: "Bonuses", events: list[Event]) -> None:
        for event in events:
            if event.type == PLAYER_MOVED:
                self._player = event.player
            if event.type == CREATE_BONUS:
                self._bonuses.append(self._create())

    def process_input(self: "Bonuses", keys: ScancodeWrapper) -> None:
        pass

    def update(self: "Bonuses") -> None:
        for bonus in self._bonuses:
            bonus[1] = bonus[1].move(bonus[2])
            if self._player is not None and self._player.colliderect(bonus[1]):
                post(Event(BONUS_PLAYER_COLLIDED))
                self._bonuses.pop(self._bonuses.index(bonus))
            if bonus[1].right < 0:
                self._bonuses.pop(self._bonuses.index(bonus))

    def render(self: "Bonuses", parent_surface: Surface) -> None:
        [parent_surface.blit(bonus[0], bonus[1]) for bonus in self._bonuses]
    
    def _create(self: "Bonuses") -> list[list[int | Rect] | Rect]:
        bonus_size = self._size
        bonus = load_image(self._image_path, bonus_size)
        bonus_rect = Rect(WIDTH, randint(0, HEIGHT), *bonus_size)
        bonus_move = [randint(-8, -4), 0]
        return [bonus, bonus_rect, bonus_move]
