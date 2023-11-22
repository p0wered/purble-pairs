import random


class GameCard:
    all_types = ['b1', 'b2', 'p1', 'p2', 'r1', 'r2', 'y1', 'y2']

    def __init__(self, card_type):
        self.card_type = card_type

    def __repr__(self):
        return f'card_{self.card_type}'

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
        return [str(GameCard(card_type)) for _ in range(1) for card_type in GameCard.all_types]
