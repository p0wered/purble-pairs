import random
import pygame as pg
from card import GameCard


class GameBoard:
    cards = []

    def __init__(self, cards):
        cards = GameCard.all_cards()
        random.shuffle(self.cards)

    def __repr__(self):
        return str(self.cards)

    @staticmethod
    def render(display, custom_list):
        """Выводит на экран сетку карточек 2х4 в случайном порядке"""
        card_cloud, card_tree, card_blob, card_flower = pg.image.load('images/blue.png'), pg.image.load('images/red.png'), pg.image.load('images/yellow.png'), pg.image.load('images/purple.png')
        cycle, shift = 0, 0
        for card in custom_list:
            if cycle % 4 == 0:
                shift += 142
                cycle = 0
            cycle += 1
            card = str(card)
            if card == 'card_cloud':
                display.blit(card_cloud, (cycle * 140, shift))
            elif card == 'card_tree':
                display.blit(card_tree, (cycle * 140, shift))
            elif card == 'card_blob':
                display.blit(card_blob, (cycle * 140, shift))
            else:
                display.blit(card_flower, (cycle * 140, shift))

