from copy import deepcopy
import numpy as np
from .base_agent import Agent, Move
from ..player import Player
from ..board import Board, CellState


class SOAgent (Agent):

    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        valid_moves = self._valid_moves(board)
        for move in valid_moves:
            if move.col == 0 or 2:
                return move
            else:
                self.next_move(board)


def _valid_moves(self, board):
    valid_moves = []
    for i, j in board.empty_cells:
        valid_moves.append(Move(self._player, i, j))
    return valid_moves
