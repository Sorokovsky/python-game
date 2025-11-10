from typing import Tuple
from pygame import Surface, error
from pygame.image import load
from pygame.transform import scale


def load_image(path: str, size: Tuple[int, int]) -> Surface:
    loaded = load(path)
    try:
        return scale(loaded.convert_alpha(), size)
    except error:
        return scale(loaded, size)
