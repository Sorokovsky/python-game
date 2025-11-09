import pygame.time

from factories import *
from events import CREATE_ENEMY


def main() -> None:
    pygame.init()
    main_display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    [player, player_rect, player_move] = create_player()

    is_playing = True
    pygame.time.set_timer(CREATE_ENEMY, 500)
    enemies = []
    while is_playing:
        main_display.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == CREATE_ENEMY:
                enemies.append(create_enemy())
        keys = pygame.key.get_pressed()
        player_speed = [0, 0]

        if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_speed = [0, 1]

        if keys[pygame.K_UP] and player_rect.top > 0:
            player_speed = [0, -1]

        for enemy in enemies:
            enemy[1] = enemy[1].move(enemy[2])
            main_display.blit(enemy[0], enemy[1])
            if enemy[1].left < 0:
                enemies.pop(enemies.index(enemy))

        player_rect = player_rect.move(player_speed)
        main_display.blit(player, player_rect)
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()