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
    def render(display, sprites, positions):
        """Выводит на экран сетку карточек 2х4 в случайном порядке"""
        card_cloud, card_tree, card_blob, card_flower = pg.image.load('images/blue.png'), pg.image.load('images/red.png'), pg.image.load('images/yellow.png'), pg.image.load('images/purple.png')
        card_width, card_height = 128, 128
        st_x, st_y, cycle = 261, 244, 0
        for item in sprites:
            if cycle // 4 in [1, 2, 3]:
                st_x = 261
                st_y += card_height + 10
                cycle = 0
            cycle += 1
            item = str(item)
            if len(positions) < 8:
                positions.append((st_x, st_y))
            st_x += card_width + 10
            if item == 'card_cloud':
                display.blit(card_cloud, (st_x, st_y))
            elif item == 'card_tree':
                display.blit(card_tree, (st_x, st_y))
            elif item == 'card_blob':
                display.blit(card_blob, (st_x, st_y))
            else:
                display.blit(card_flower, (st_x, st_y))
