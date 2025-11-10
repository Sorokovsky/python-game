from typing import Tuple
from pygame import Surface, Rect
from pygame.event import Event, post
from pygame.key import ScancodeWrapper
from pygame.time import set_timer
from random import randint

from behavious.behaviour import Behaviour
from constants.events import CREATE_ENEMY, ENEMY_PLAYER_COLLIDED, STOP_GAME, PLAYER_MOVED
from constants.sizes import WIDTH, HEIGHT
from helpers.load_image import load_image


class Enemies(Behaviour):
    _size: Tuple[int, int] = (68, 24)
    _image_path: str = "images/enemy.png"
    _enemies: list[list[Surface | Rect | list[int]]] = []
    _timeout: int = 500
    _player: Surface | Rect | list[int] | None = None

    def start(self: "Enemies") -> None:
        set_timer(CREATE_ENEMY, self._timeout)

    def process_events(self: "Enemies", events: list[Event]) -> None:
        for event in events:
            if event.type == CREATE_ENEMY:
                created = self._create()
                self._enemies.append(created)
            if event.type == ENEMY_PLAYER_COLLIDED:
                post(Event(STOP_GAME))

            if event.type == PLAYER_MOVED:
                self._player = event.player

    def process_input(self: "Enemies", keys: ScancodeWrapper) -> None:
        pass

    def update(self: "Enemies") -> None:
        for enemy in self._enemies:
            enemy[1] = enemy[1].move(enemy[2])
            if self._player is not None and self._player.colliderect(enemy[1]):
                post(Event(ENEMY_PLAYER_COLLIDED))
            if enemy[1].right < 0:
                self._enemies.pop(self._enemies.index(enemy))

    def render(self: "Enemies", parent_surface: Surface) -> None:
        [parent_surface.blit(enemy[0], enemy[1]) for enemy in self._enemies]

    def _create(self: "Enemies") -> list[Surface | Rect | list[int]]:
        enemy_size = self._size
        enemy = load_image(self._image_path, enemy_size)
        enemy_rect = Rect(WIDTH, randint(0, HEIGHT), *enemy_size)
        enemy_move = [randint(-8, -4), 0]
        return [enemy, enemy_rect, enemy_move]
