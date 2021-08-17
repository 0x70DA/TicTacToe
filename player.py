import random


class ComputerPlayer:
    """A computer player class, that randomly chooses moves."""

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer:
    """A Human player class."""

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        while True:
            move = input(f"{self.letter}'s turn. Enter move(0-8): ")
            try:
                move = int(move)
                if move not in game.available_moves():
                    raise ValueError
                break
            except ValueError:
                print("Invalid square. Choose again.")
        return move
