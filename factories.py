import pygame
from pygame import Surface, Rect

from sizes import *
from collors import *

def create_enemy() -> list[Surface | Rect | list[int]]:
    enemy_size = ENEMY_SIZE
    enemy = pygame.Surface(enemy_size)
    enemy.fill(BLUE)
    enemy_rect = pygame.Rect(WIDTH, 100, *enemy_size)
    enemy_move = [-1, 0]
    return [enemy, enemy_rect, enemy_move]

def create_player() -> list[Surface | Rect | list[int]]:
    player_size = PLAYER_SIZE
    player = pygame.Surface(player_size)
    player.fill(WHITE)
    player_rect = player.get_rect()
    player_move = [-1, 0]
    return [player, player_rect, player_move]
