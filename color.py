class Color:
    _r: int
    _g: int
    _b: int

    def __init__(self: "Color", r: int, g: int, b: int) -> None:
        self._r = r
        self._g = g
        self._b = b

    def get_r(self: "Color") -> int:
        return self._r

    def get_g(self: "Color") -> int:
        return self._g

    def get_b(self: "Color") -> int:
        return self._b
