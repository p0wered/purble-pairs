import random


class GameCard:
    all_types = ['blue', 'purple', 'red', 'yellow']

    def __init__(self, card_type):
        self.card_type = card_type

    def __repr__(self):
        return f'card_{self.card_type}'

    def __eq__(self, other):
        return self.card_type == other.card_type

    @staticmethod
    def create():
        instant = random.choice(GameCard.all_types)
        card_type = instant
        return GameCard(card_type)

    @staticmethod
    def all_cards():
        return [GameCard(card_type) for _ in range(2) for card_type in GameCard.all_types]
