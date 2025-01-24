# Decription: Enemy player Class that inherits the Player Class
from Player import Player


class Enemy(Player):
    def __init__(self):
        super().__init__()

    def _generate_name(self):
        """Generates Enemy name"""
        self._playername = "Test"


if __name__ == '__main__':
    e = Enemy()
    print(e)
    e._generate_name()
    print(e.get_player_name())
