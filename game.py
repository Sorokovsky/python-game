from pygame import Surface, init
from pygame.constants import QUIT
from pygame.display import set_mode, flip
from pygame.event import post, get, Event
from pygame.key import get_pressed
from pygame.time import Clock

from behavious.behaviour import Behaviour
from constants.events import START_GAME, STOP_GAME
from constants.sizes import WIDTH, HEIGHT


class Game:
    _behaviors: list[Behaviour]
    _display: Surface
    _is_running = False,
    _clock: Clock

    def __init__(self: "Game") -> None:
        init()
        self._behaviors = []
        self._clock = Clock()

    def add_behaviour(self: "Game", behaviour: Behaviour) -> None:
        behaviour.start()
        self._behaviors.append(behaviour)

    def start(self: "Game", fps: float = 120) -> None:
        self._clock.tick(fps)
        self._display = set_mode((WIDTH, HEIGHT))
        self._is_running = True
        post(Event(START_GAME))
        self._loop()

    def _loop(self: "Game") -> None:
        while self._is_running:
            self._process__events()
            self._process_inputs()
            self._update()
            self._render()

    def _process__events(self: "Game") -> None:
        events = get()
        [behaviour.process_events(events) for behaviour in self._behaviors]
        for event in events:
            if event.type == START_GAME:
                self._is_running = True
            if event.type == STOP_GAME or event.type == QUIT:
                self._is_running = False

    def _process_inputs(self: "Game") -> None:
        keys = get_pressed()
        [behaviour.process_input(keys) for behaviour in self._behaviors]

    def _update(self: "Game") -> None:
        [behaviour.update() for behaviour in self._behaviors]

    def _render(self: "Game") -> None:
        [behaviour.render(self._display) for behaviour in self._behaviors]
        flip()
