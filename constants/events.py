from pygame import USEREVENT

index = 0


def create_event() -> int:
    global index
    index += 1
    return USEREVENT + index


CREATE_ENEMY = create_event()
CREATE_BONUS = create_event()
GOOSE_ANIMATE = create_event()
START_GAME = create_event()
STOP_GAME = create_event()