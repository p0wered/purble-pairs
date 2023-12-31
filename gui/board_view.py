import pygame as pg
from config import GEOM, RCS
from gui.card_view import CardView


class BoardView:

    def __init__(self):
        self.width = GEOM['card_width']
        self.height = GEOM['card_height']

    def render(self, display: pg.Surface, visible):
        """Выводит на экран сетку карточек 4х5 в случайном порядке"""
        st_x, st_y, cycle = 30, 30, 0
        for item in RCS['cards']:

            if cycle // 4 in [1, 2, 3, 4, 5]:
                st_x = 30
                st_y += self.height + 10
                cycle = 0
            cycle += 1
            item = str(item)

            if len(RCS['positions']) < 20:
                RCS['positions'].append((st_x, st_y))

            current = RCS['card_img'].get(str(item))

            if visible < 1.5:
                CardView.draw_selected(display, current, st_x, st_y)
            else:
                if RCS['cards'].index(item) in RCS['clicked']:
                    CardView.draw_selected(display, current, st_x, st_y)
                else:
                    CardView.draw_back(display, current, st_x, st_y)

            st_x += self.width + 10
