import pygame.time

from factories import *
from events import CREATE_ENEMY, CREATE_BONUS
from collors import *


def main() -> None:
    background = pygame.transform.scale(pygame.image.load('images/background.png'), (WIDTH, HEIGHT))
    background_x1 = 0
    background_x2 = background.get_width()
    background_move = 3
    pygame.init()
    main_display = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("Verdana", 20)
    clock = pygame.time.Clock()
    [player, player_rect, player_move] = create_player()
    [bonus, bonus_rect, bonus_move] = create_bonus()
    score = 0

    is_playing = True
    pygame.time.set_timer(CREATE_ENEMY, 500)
    pygame.time.set_timer(CREATE_BONUS, 200)
    enemies = []
    bonuses = []
    while is_playing:
        background_x1 -= background_move
        background_move -= background_move
        main_display.blit(background, (background_x1, 0))
        main_display.blit(background, (background_x2, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == CREATE_ENEMY:
                enemies.append(create_enemy())

            if event.type == CREATE_BONUS:
                bonuses.append(create_bonus())
        keys = pygame.key.get_pressed()
        player_speed = [0, 0]

        if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
            player_speed = [0, 1]

        if keys[pygame.K_UP] and player_rect.top > 0:
            player_speed = [0, -1]

        for enemy in enemies:
            enemy[1] = enemy[1].move(enemy[2])
            main_display.blit(enemy[0], enemy[1])
            if player_rect.colliderect(enemy[1]):
                is_playing = False
            if enemy[1].left < 0:
                enemies.pop(enemies.index(enemy))

        for bonus in bonuses:
            bonus[1] = bonus[1].move(bonus[2])
            main_display.blit(bonus[0], bonus[1])
            if player_rect.colliderect(bonus[1]):
                score += 1
                bonuses.pop(bonuses.index(bonus))

        player_rect = player_rect.move(player_speed)
        main_display.blit(player, player_rect)
        main_display.blit(font.render("Рахунок: " + str(score), True, BLACK), (WIDTH - 200, 20))
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()