from behavious.background import Background
from behavious.player import Player
from behavious.enemies import Enemies
from behavious.bonuses import Bonuses
from behavious.score import Score
from game import Game


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
