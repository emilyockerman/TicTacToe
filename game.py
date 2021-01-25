from copy import deepcopy

from .board import Board, CellState
from .player import Player, PLAYER_NAMES


class Game(object):
    def __init__(self, player_x, player_o, size=3, num_to_win=None,
                 starting_board=None):
        self._player_x = player_x
        self._player_o = player_o

        self._current_player = (Player.X, self._player_x)
        self._next_player = (Player.O, self._player_o)

        if starting_board is None:
            self._board = Board(size=size, num_to_win=num_to_win)

        self._num_rounds = 0

    def play(self):
        # while no one has won yet, do...
        while (self._board.winner is None
               and self._num_rounds < self._board.size ** 2):
            self._show_board()
            self._make_next_move()
            self._current_player, self._next_player = \
                self._next_player, self._current_player
            self._num_rounds = self._num_rounds + 1
        # shows the board to the screen
        self._show_board()
        # happens all too often in this rudimentary game!
        if self._board.winner is None:
            print("It's a draw!")
        else:
            print("Congratulations, {} won!".format(
                PLAYER_NAMES[self._board.winner]))

    def _show_board(self):
        print(self._board)
        print("")

    # the next move is made by the player whose turn it is
    def _make_next_move(self):
        move = self._current_player[1].next_move(deepcopy(self._board))

        assert move.player == self._current_player[0]
        assert self._board.cell(move.row, move.col) == CellState.EMPTY

        self._board.set_cell(move.player, move.row, move.col)
