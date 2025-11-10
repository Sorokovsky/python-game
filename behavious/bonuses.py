from typing import Tuple
from random import randint

from pygame import Surface, Rect
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame.time import set_timer

from behavious.behaviour import Behaviour
from constants.sizes import WIDTH, HEIGHT
from constants.events import PLAYER_MOVED, CREATE_BONUS


class Bonuses(Behaviour):
    _size: Tuple[int, int] = (40, 40)
    _color: Tuple[int, int, int] = (255, 0, 0)
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
        pass

    def render(self: "Bonuses", parent_surface: Surface) -> None:
        pass
    
    def _create(self: "Bonuses") -> list[list[int | Rect] | Rect]:
        bonus_size = self._size
        bonus = Surface(bonus_size)
        bonus.fill(self._color)
        bonus_rect = Rect(WIDTH, randint(0, HEIGHT), *bonus_size)
        bonus_move = [randint(-8, -4), 0]
        return [bonus, bonus_rect, bonus_move]
