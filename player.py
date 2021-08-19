import random
import math


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


class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # pick a random square as the first move.
            move = random.choice(game.available_moves())
        else:
            # use the minimax algorithm.
            move = self.minimax(game, self.letter)['position']
        return move

    def minimax(self, state, player):
        max_player = self.letter  # the smart computer player
        other_player = 'O' if player == 'X' else 'X'

        # check if the previous move is a winning move?
        if state.winner == other_player:
            return {
                'position': None,
                'score': 1 * (len(state.available_moves()) + 1) if other_player == max_player else -1 * (len(state.available_moves()) + 1)
            }
        elif len(state.available_moves()) == 0:
            return {'position': None, 'score': 0}

        if player == max_player:
            # any score should be more to maximize the score
            best_move = {'position': None, 'score': -math.inf}
        else:
            # any score should be less to minimize the score
            best_move = {'position': None, 'score': math.inf}

        # try out every possible move.
        for possible_move in state.available_moves():
            # make the move
            state.make_move(possible_move, player)
            # simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            # undo the move
            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move  # the next optimal move

            if player == max_player:
                if sim_score['score'] > best_move['score']:
                    best_move = sim_score
            else:
                if sim_score['score'] < best_move['score']:
                    best_move = sim_score
        return best_move
