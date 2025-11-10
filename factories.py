import pygame
import random
from pygame import Surface, Rect

from constants.sizes import *
from constants.collors import *


def create_enemy() -> list[Surface | Rect | list[int]]:
    enemy_size = ENEMY_SIZE
    enemy = pygame.Surface(enemy_size)
    enemy.fill(BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]


def create_player() -> list[Surface | Rect | list[int]]:
    player_size = PLAYER_SIZE
    player = pygame.Surface(player_size, pygame.SRCALPHA)
    image = pygame.transform.scale(pygame.image.load("images/player.png").convert_alpha(), player_size)
    player.blit(image, (0, 0))
    player_rect = player.get_rect()
    player_move = [-1, 0]
    return [player, player_rect, player_move]


def create_bonus() -> list[Surface | Rect | list[int]]:
    bonus_size = BONUS_SIZE
    bonus = pygame.Surface(bonus_size)
    bonus.fill(RED)
    bonus_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *bonus_size)
    bonus_move = [random.randint(-8, -4), 0]
    return [bonus, bonus_rect, bonus_move]
