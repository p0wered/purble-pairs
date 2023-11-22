import pygame as pg
from config import GEOM, RCS
from gui.card_view import CardView


class BoardView:

    def __init__(self):
        pass

    @staticmethod
    def render(display: pg.Surface):
        """Выводит на экран сетку карточек 2х4 в случайном порядке"""
        w, h = GEOM['card_width'], GEOM['card_height']
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
            current = RCS['card_img'].get(str(item))
            if RCS['cards'].index(item) in RCS['clicked']:
                CardView.draw_selected(display, current, st_x, st_y)
            else:
                CardView.draw_back(display, current, st_x, st_y)
            st_x += w + 10

