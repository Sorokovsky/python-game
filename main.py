from game_object import GameObject
from scene import Scene
from vector import Vector
from color import Color


def main() -> None:
    player = GameObject(Vector(12, 12), Vector(12, 12))
    player.set_color(Color(255, 255, 255))
    scene = Scene(Vector(1200, 800))
    scene.add_object(player)

    scene.run()


if __name__ == "__main__":
    main()
