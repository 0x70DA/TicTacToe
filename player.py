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

    def get_move(self):
        pass


class HumanPlayer(Player):
    """A Human player class."""

    def __init__(self, letter):
        super().__init(letter)

    def get_move(self):
        pass
