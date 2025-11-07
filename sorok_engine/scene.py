from pygame import event as events
from pygame.constants import QUIT
from typing import Tuple, List
from pygame import Surface
from sorok_engine.game_object import GameObject

from sorok_engine.window import Window


class Scene:
    _window: Window
    _is_run: bool
    _game_objects: List[GameObject]

    def __init__(self: "Scene") -> None:
        self._window = Window()
        self._is_run = False
        self._game_objects = []

    def run(self: "Scene") -> None:
        self._is_run = True
        self._window.draw()
        self._process_events()

    def create_object(self: "Scene", position: Tuple[int, int], size: Tuple[int, int]) -> GameObject:
        game_object = GameObject(Surface(size), position, size, self)
        self._game_objects.append(game_object)
        return game_object

    def _start_objects(self: "Scene") -> None:
        [game_object.start() for game_object in self._game_objects]

    def _process_events(self: "Scene") -> None:
        while self._is_run:
            for event in events.get():
                if event.type == QUIT:
                    self._is_run = False
