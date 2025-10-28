from player import Player
from engine.scene import Scene
from engine.vector import Vector
from engine.color import Color


def main() -> None:
    player = Player(Vector(12, 12), Vector(12, 12))
    player.set_color(Color(255, 255, 255))
    scene = Scene(Vector(1200, 800))
    scene.add_object(player)
    scene.run()


if __name__ == "__main__":
    main()
