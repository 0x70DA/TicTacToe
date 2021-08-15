import math
import random


class PLayer:
    """Base player class"""

    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        """Overriden in the child classes"""
        pass


class ComputerPlayer(Player):
    """A computer player class, that randomly chooses moves."""

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    """A Human player class."""

    def __init__(self, letter):
        super().__init(letter)

    def get_move(self, game):
        while True:
            square = input(f"{self.letter}'s turn. Enter move(0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                break
            except ValueError:
                print("Invalid square. Choose again.")
        return val
