from pygame.event import Event
from pygame.key import ScancodeWrapper
from pygame import Surface
from abc import ABC, abstractmethod


class Behaviour(ABC):
    def __int__(self: "Behaviour") -> None:
        pass

    @abstractmethod
    def start(self: "Behaviour") -> None:
        pass

    @abstractmethod
    def process_events(self: "Behaviour", events: list[Event]) -> None:
        pass

    @abstractmethod
    def process_input(self: "Behaviour", keys: ScancodeWrapper) -> None:
        pass

    @abstractmethod
    def update(self: "Behaviour") -> None:
        pass

    @abstractmethod
    def render(self: "Behaviour", parent_surface: Surface) -> None:
        pass

