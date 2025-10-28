from engine.game_object import GameObject
from engine.vector import Vector


class Player(GameObject):
    _v0: int = 0
    _g: float = 9.8
    _t: float = 0

    def __init__(self: "Player", size: Vector, position: Vector):
        super(Player, self).__init__(size, position)

    def update(self: "Player", fps: int) -> None:
        x = self.get_position().get_x()
        y = int((self._v0 * self._t) + (self._g * self._t * self._t) / 2)
        self._position = Vector(x, y)
        self._t += (1 / fps)
