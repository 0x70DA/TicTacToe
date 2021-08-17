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

    def make_move(self, move, letter):
        if self.board[move] == " ":
            self.board[move] = letter
            if self.check_winner(move, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, move, letter):
        """check the vertical and horizontal and the diagonals."""
        row_index = move // 3
        row = self.board[row_index*3:(row_index*3) + 3]
        if all([i == letter for i in row]):
            return True

        col_index = move % 3
        col = [self.board[col_index+i] for i in range(0, 7, 3)]
        if all([c == letter for c in col]):
            return True

        # The diagonal are at (0,4,8), (2,4,6)
        if move % 2 == 0:
            diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([d == letter for d in diagonal]):
                return True

            diagonal = [self.board[i] for i in [2, 4, 6]]
            if all(d == letter for d in diagonal):
                return True

        return False

    def has_empty_squares(self):
        return ' ' in self.board
