from copy import deepcopy
import numpy as np
from math import inf
from .base_agent import Agent, Move
from ..player import Player, other_player
from ..board import Board, CellState


class ABAgent (Agent):

    def __init__(self, player):
        super().__init__(player)

    def _ab(self, player, board, alpha, beta):
        if board.winner == player:
            # the maximising player is the one the *agent* is playing for
            if board.winner == self._player:
                return 1, []
            else:
                return -1, []
        elif len(board.empty_cells) == 0:
            return 0, []

        valid_moves = _valid_moves(player, board)
        best_move = None

        if player == self._player:
            max_val = -inf
            for move in valid_moves:
                mem_board = deepcopy(board)
                mem_board.set_cell(move.player, move.row, move.col)
                move_value, m = self._ab(other_player(player), mem_board, alpha, beta)
                # if the move value is greater than the current max value, replace the max value with the move val
                if move_value > max_val:
                    max_val = move_value
                    best_move = [move] + m
                alpha = max(alpha, move_value)
                if beta <= alpha:
                    break
            return max_val, best_move
        else:
            min_val = inf
            for move in valid_moves:
                mem_board = deepcopy(board)
                mem_board.set_cell(move.player, move.row, move.col)
                move_value, m = self._ab(other_player(player), mem_board, alpha, beta)
                if move_value < min_val:
                    min_val = move_value
                    best_move = [move] + m
                beta = min(beta, move_value)
                if beta <= alpha:
                    break
            return min_val, best_move

    # takes the move from the dfs call and makes the move
    def next_move(self, board):
        _, next_m = self._ab(self._player, board, alpha=-inf, beta=inf)
        return next_m[0]


def _valid_moves(player, board):
    valid_moves = []
    for i, j in board.empty_cells:
        valid_moves.append(Move(player, i, j))

    return valid_moves








