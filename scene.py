import pygame.event
from window import Window
from vector import Vector
from game_object import GameObject
from pygame.constants import QUIT


class Scene:
    _window: Window
    _objects: list[GameObject]
    _is_running: bool

    def __init__(self: "Scene", size: Vector) -> None:
        self._window = Window(size)
        self._objects = []
        self._is_running = False

    def start(self: "Scene") -> None:
        pass

    def add_object(self: "Scene", object: GameObject) -> None:
        self._objects.append(object)
        self._window.draw(object)

    def run(self: "Scene") -> None:
        self._is_running = True
        while self._is_running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._is_running = False
