import pygame.event

from sorok_engine.window import Window


class Scene:
    _window: Window
    _is_run: bool = False

    def __init__(self: "Scene") -> None:
        self._window = Window()

    def run(self: "Scene") -> None:
        self._is_run = True
        self._window.draw()
        self._process_events()

    def _process_events(self: "Scene") -> None:
        while self._is_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_run = False
