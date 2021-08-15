import math
import time
from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self):
        # create empty board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    @staticmethod
    def print_board_nums():
        """Print a numbered board at the beginning of the game."""
        for row in [[str(i) for i in range(j*3, (j*3)+3)] for j in range(3)]:
            print('|' + ' | '.join(row) + '|')

    def print_board(self):
        """Print the current board"""
        for row in [self.board[i*3:(i*3)+3] for i in range(3)]:
            print('|' + ' | '.join(row) + '|')

    def avialable_moves(self):
        """Return a list of available moves."""
        return [index for index, value in enumerate(self.board) if value == " "]
