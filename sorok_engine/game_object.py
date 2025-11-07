from __future__ import annotations
from pygame import Surface
from typing import Tuple, TYPE_CHECKING


if TYPE_CHECKING:
    from sorok_engine.scene import Scene

class GameObject:
    _surface: Surface
    _position: Tuple[int, int]
    _size: Tuple[int, int]
    _scene: Scene

    def __init__(self: "GameObject", surface: Surface, position: Tuple[int, int], size: Tuple[int, int], scene: Scene) -> None:
        self._surface = surface
        self._position = position
        self._size = size
        self._scene = scene

    def get_surface(self: "GameObject") -> Surface:
        return self._surface

    def get_position(self: "GameObject") -> Tuple[int, int]:
        return self._position

    def get_size(self: "GameObject") -> Tuple[int, int]:
        return self._size

    def start(self: "GameObject") -> None:
        pass

    def update(self: "GameObject") -> None:
        pass

    def stop(self: "GameObject") -> None:
        pass