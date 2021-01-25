from copy import deepcopy
import numpy as np
from .base_agent import Agent, Move
from ..player import Player, other_player
from ..board import Board, CellState


class DFSAgent(Agent):

    def __init__(self, player):
        super().__init__(player)

    def _dfs(self, player, board):
        if board.winner is not None:
            # if board.winner == self._player:
            # you should assign scores for the _current_ player
            if board.winner == player:
                # you can just return None if you have no move to return, e.g.:
                # return 1, None
                return 1, None
            else:
                return -1, None
        elif len(board.empty_cells) == 0:
            return 0, None

        # you want the moves for the player you're simulating
        valid_moves = _valid_moves(player, board)
        move_values = {}

        best_score = -2
        best_move = None
        # while still going through the possible moves
        for move in valid_moves:
            # make a variable to store the current board state
            mem_board = deepcopy(board)
            # make the supposed next move
            mem_board.set_cell(move.player, move.row, move.col)
            # stores the value of that move once dfs has wiggled its way all the way to the end
            # alternate players, forgetting about the best move
            move_value, _ = self._dfs(other_player(player), mem_board)
            # switches it (necessary because using the same loop for both min and max)
            move_value = -move_value
            # adds the move to the dictionary along with its value
            # note that this is a dictionary and will only store the latest move for each utility
            move_values.update({move_value: move})
        # goes through all the values and chooses the one with the biggest utility
        for move_value in move_values:
            # if the value of the move that was just tested is greater than the best score
            # preset or the last best score, reset the variable
            if move_value > best_score:
                best_score = move_value
                # you want to retrieve move from the dictionary you put it in
                best_move = move_values[move_value]
        # returns the move that is judged to be the best for gameplay
        return best_score, best_move

    # takes the move from the dfs call and makes the move
    def next_move(self, board):
        # only need the move, dont need to store the value
        _, next_m = self._dfs(self._player, board)
        return next_m


def _valid_moves(player, board):
    valid_moves = []
    for i, j in board.empty_cells:
        valid_moves.append(Move(player, i, j))

    return valid_moves
