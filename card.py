import random
from config import RCS


class GameCard:
    all_types = ['ct1', 'ct2', 'ee1', 'ee2', 'pc1', 'pc2', 'pn1', 'pn2', 'vl1', 'vl2', 'vn1', 'vn2', 'if1', 'if2', 'eo1', 'eo2']

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

    @staticmethod
    def compare(index_1, index_2):
        if RCS['cards'][index_1] != 'none' and RCS['cards'][index_2] != 'none':
            letter_1 = RCS['cards'][index_1][5:7]
            letter_2 = RCS['cards'][index_2][5:7]
            if letter_1 == letter_2 and index_1 != index_2:
                return True
            else:
                return False
