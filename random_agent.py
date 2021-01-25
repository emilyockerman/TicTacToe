import random

from .base_agent import Agent


class RandomAgent(Agent):
    def __init__(self, player):
        # in cases of single inheritance, allows you to not have to change the name of the class
        # (makes it easier; acts as a placeholder)
        super().__init__(player)

    def next_move(self, board):
        # write an algorithm that would call a random valid move
        valid_moves = self._valid_moves(board)
        move = random.choice(valid_moves)
        return move
