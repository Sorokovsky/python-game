import pygame

from collors import *
from sizes import *
from create_enemy import create_enemy


def main() -> None:
    pygame.init()
    main_display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = pygame.Surface(PLAYER_SIZE)
    player.fill(WHITE)
    player_rect = player.get_rect()
    [enemy, enemy_rect, enemy_move] = create_enemy()

    is_playing = True
    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
        keys = pygame.key.get_pressed()
        player_speed = [0, 0]
        if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_speed = [0, 1]
        player_rect = player_rect.move(player_speed)
        enemy_rect = enemy_rect.move(enemy_move)
        main_display.fill(GREEN)
        main_display.blit(player, player_rect)
        main_display.blit(enemy, enemy_rect)
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()