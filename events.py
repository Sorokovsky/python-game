import pygame

index = 0

def create_event() -> int:
    global index
    index += 1
    return pygame.USEREVENT + index

CREATE_ENEMY = create_event()
CREATE_BONUS = create_event()