import math, time
from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self):
        # create empty board
        self.board = [' ' for _ in range(9)] 
        self.current_winner = None

    def print_board_nums(self):
        # 0,1,2
        # 3,4,5
        # 6,7,8
        for row in [[str(i) for i in range(j*3, (j*3)+3)] for j in range(3)]:
            print('|' + ' | '.join(row) + '|')



    def print_board(self):
        """Print the current board"""
        for row in [self.board[i*3:(i*3)+3] for i in range(3)]:
            print('|' + ' | '.join(row) + '|')

    