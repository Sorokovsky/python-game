from pygame import Surface
from typing import Tuple
from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame.font import SysFont, Font

from behavious.behaviour import Behaviour
from constants.events import BONUS_PLAYER_COLLIDED
from constants.sizes import WIDTH


class Score(Behaviour):
    _font: Font
    _score: int = 0
    _title: str = "Рахунок: "
    _color: Tuple[int, int, int] = (0, 0, 0)
    
    def start(self: "Score") -> None:
        self._font = SysFont("Verdana", 20)

    def process_events(self: "Score", events: list[Event]) -> None:
        for event in events:
            if event.type == BONUS_PLAYER_COLLIDED:
                self._score += 1

    def process_input(self: "Score", keys: ScancodeWrapper) -> None:
        pass

    def update(self: "Score") -> None:
        pass

    def render(self: "Score", parent_surface: Surface) -> None:
        parent_surface.blit(self._font.render(self._title + str(self._score), True, self._color), (WIDTH - 200, 20))
