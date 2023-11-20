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
    def create(c_type):
        """"Создаёт карту по названию типа"""
        return GameCard(c_type)

    @staticmethod
    def card_list(text: str):
        """ Из строки вида 'blue red yellow purple' возвращает список соответствующих карт"""
        return [GameCard.create(word) for word in text.split()]

    @staticmethod
    def all_cards():
        """Создает список карт"""
        return [GameCard(card_type) for _ in range(2) for card_type in GameCard.all_types]
