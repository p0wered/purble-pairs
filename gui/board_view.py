import pygame as pg
from config import GEOM, RCS


class BoardView:

    def __init__(self):
        pass

    @staticmethod
    def render(display: pg.Surface):
        """Выводит на экран сетку карточек 2х4 в случайном порядке"""
        w, h = GEOM['card_width'], GEOM['card_height']
        card_images = {
            'card_blue': pg.image.load('cards/blue.png'),
            'card_red': pg.image.load('cards/red.png'),
            'card_yellow': pg.image.load('cards/yellow.png'),
            'card_purple': pg.image.load('cards/purple.png')
        }
        st_x, st_y, cycle = 261, 244, 0
        for item in RCS['cards']:
            if cycle // 4 in [1, 2, 3]:
                st_x = 261
                st_y += h + 10
                cycle = 0
            cycle += 1
            item = str(item)
            if len(RCS['positions']) < 8:
                RCS['positions'].append((st_x, st_y))
            image = card_images.get(str(item))
            if image is not None:
                display.blit(image, (st_x, st_y))
            else:
                display.blit(pg.Surface((w, h), pg.SRCALPHA), (st_x, st_y))
            st_x += w + 10

    # @staticmethod
    # def card_selected(index):
    #     index = RCS['clicked'][0]
    #     pg.transform.flip(RCS['cards'][index], True, False)
