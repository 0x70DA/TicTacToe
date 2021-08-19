import time
from game import TicTacToe
from player import HumanPlayer, ComputerPlayer, AIPlayer


def play(game, player_x, player_y, print_game=True):
    if print_game:
        TicTacToe.print_board_nums()

    letter = 'X'
    while game.has_empty_squares():
        if letter == 'X':
            move = player_x.get_move(game)
        else:
            move = player_y.get_move(game)

        # check if the move is available
        if game.make_move(move, letter):
            if print_game:
                print(f"{letter} makes a move to square {move}")
                game.print_board()
                print()

            if game.winner != None:
                if print_game:
                    print(f"{letter} wins!!!")
                return letter  # end the loop and exit the game

            letter = "O" if letter == "X" else "X"
            time.sleep(1)  # delay one second between each turn
    # the loop finished and it's a tie.
    if print_game:
        print("It's a tie!!!")


if __name__ == "__main__":
    game = TicTacToe()
    player1 = HumanPlayer('X')
    player2 = AIPlayer('O')
    play(game, player1, player2, True)
