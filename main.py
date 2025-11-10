from behavious.background import Background
from behavious.player import Player
from behavious.enemies import Enemies
from behavious.bonuses import Bonuses
from behavious.score import Score
from game import Game


# def old_main() -> None:
#     font = pygame.font.SysFont("Verdana", 20)
#     score = 0
#     while is_playing:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_playing = False
#             if event.type == CREATE_ENEMY:
#                 enemies.append(create_enemy())
#             if event.type == CREATE_BONUS:
#                 bonuses.append(create_bonus())
#             if event.type == GOOSE_ANIMATE:
#                 image = pygame.image.load(os.path.join(GOOSE_PATH, PLAYER_IMAGES[image_index])).convert_alpha()
#                 player = pygame.transform.scale(image, PLAYER_SIZE)
#                 image_index += 1
#                 if image_index >= len(PLAYER_IMAGES):
#                     image_index = 0
#         keys = pygame.key.get_pressed()
#         player_speed = [0, 0]
#
#         if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
#             player_speed = player_move_down
#
#         if keys[pygame.K_UP] and player_rect.top > 0:
#             player_speed = player_move_up
#
#         if keys[pygame.K_LEFT] and player_rect.left > 0:
#             player_speed = player_move_left
#
#         if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
#             player_speed = player_move_right
#
#         for enemy in enemies:
#             enemy[1] = enemy[1].move(enemy[2])
#             main_display.blit(enemy[0], enemy[1])
#             if player_rect.colliderect(enemy[1]):
#                 is_playing = False
#             if enemy[1].left < 0:
#                 enemies.pop(enemies.index(enemy))
#
#         for bonus in bonuses:
#             bonus[1] = bonus[1].move(bonus[2])
#             main_display.blit(bonus[0], bonus[1])
#             if player_rect.colliderect(bonus[1]):
#                 score += 1
#                 bonuses.pop(bonuses.index(bonus))
#
#         player_rect = player_rect.move(player_speed)
#         main_display.blit(player, player_rect)
#         main_display.blit(font.render("Рахунок: " + str(score), True, BLACK), (WIDTH - 200, 20))
#         pygame.display.flip()
#         clock.tick(120)
#
#     pygame.quit()


def main() -> None:
    game = Game()
    game.add_behaviour(Background())
    game.add_behaviour(Player())
    game.add_behaviour(Enemies())
    game.add_behaviour(Bonuses())
    game.add_behaviour(Score())
    game.start()


if __name__ == "__main__":
    main()
