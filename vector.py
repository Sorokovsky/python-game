class Vector:
    _x: int
    _y: int

    def __init__(self: "Vector", x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_x(self: "Vector") -> int:
        return self._x

    def get_y(self: "Vector") -> int:
        return self._y
