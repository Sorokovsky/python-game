from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame import Surface


class Behaviour:
    def __int__(self: "Behaviour") -> None:
        pass

    def start(self: "Behaviour") -> None:
        pass

    def process_events(self: "Behaviour", events: list[Event]) -> None:
        pass

    def update(self: "Behaviour") -> None:
        pass

    def render(self: "Behaviour", parent_surface: Surface) -> None:
        pass

    def process_input(self: "Behaviour", keys: ScancodeWrapper) -> None:
        pass

