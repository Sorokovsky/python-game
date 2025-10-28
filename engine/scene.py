import pygame.event
from engine.window import Window
from engine.vector import Vector
from engine.game_object import GameObject
from pygame.constants import QUIT
import time


class Scene:
    _window: Window
    _objects: list[GameObject]
    _is_running: bool

    _fps: int

    def __init__(self: "Scene", size: Vector, fps: int = 120) -> None:
        self._window = Window(size)
        self._objects = []
        self._is_running = False
        self._fps = fps

    def start(self: "Scene") -> None:
        pass

    def add_object(self: "Scene", object: GameObject) -> None:
        self._objects.append(object)
        self._window.draw(object)

    def run(self: "Scene") -> None:
        self._is_running = True
        self._loop()

    def _on_close(self: "Scene") -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self._is_running = False

    def _update_objects(self: "Scene") -> None:
        self._window.clear()
        for object in self._objects:
            object.update()
            self._window.draw(object)
        pygame.display.flip()

    def _loop(self: "Scene") -> None:
        while self._is_running:
            self._update_objects()
            self._on_close()
