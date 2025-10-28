class Time:
    _seconds: float = 0.0
    _prev: float = 0.0
    _fps: int

    def __init__(self: "Time", fps: int) -> None:
        self._fps = fps

    def update(self: "Time") -> None:
        self._prev = self._seconds
        self._seconds += (1 / self._fps)

    def get_seconds(self: "Time") -> float:
        return self._seconds

    def get_fps(self: "Time") -> int:
        return self._fps
