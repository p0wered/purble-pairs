import random
from typing import Optional
from card import GameCard


class GameBoard:
    cards = []

    def __init__(self, cards):
        cards = GameCard.all_cards()
        random.shuffle(self.cards)

    def __str__(self):
        return str(self.cards)


board = GameBoard
print(board.cards)
