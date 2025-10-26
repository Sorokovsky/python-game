class Vector:
    _width: int
    _height: int

    def __init__(self: "Vector", width: int, height: int) -> None:
        self._width = width
        self._height = height

    def get_width(self: "Vector") -> int:
        return self._width

    def get_height(self: "Vector") -> int:
        return self._height
