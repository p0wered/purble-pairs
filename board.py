from time import monotonic as timer
import pygame as pg
from config import GEOM, RCS
from gui.card_view import CardView
from card import GameCard


class GameBoard:

    @staticmethod
    def delete_card(display: pg.Surface):
        """Удаляет две выбранные одинаковые карточки"""
        pos = pg.mouse.get_pos()
        for i, position in enumerate(RCS['positions']):
            col_card = pg.Rect(position, (GEOM['card_width'], GEOM['card_height']))

            if col_card.collidepoint(pos) and i not in RCS['clicked'] and RCS['cards'][i] != 'none':
                RCS['clicked'].append(i)

                if len(RCS['clicked']) == 2:
                    i1 = RCS['clicked'][0]
                    i2 = RCS['clicked'][1]
                    img1 = RCS['cards'][i1]
                    img2 = RCS['cards'][i2]
                    src1 = RCS['card_img'][img1]
                    src2 = RCS['card_img'][img2]
                    start = timer()
                    RCS['moves'] += 1

                    if RCS['moves'] >= 15:
                        RCS['mode'], RCS['moves'], RCS['found'] = 0, 0, 0

                    while True:
                        elapsed = timer() - start
                        CardView.draw_two(display, src1, src2, i1, i2)
                        if elapsed > 1:
                            break

                    if GameCard.compare(i1, i2):
                        RCS['cards'][i1], RCS['cards'][i2] = 'none', 'none'

                    RCS['clicked'].clear()

    @staticmethod
    def stats():
        end_list = []
        found = 0

        for k in range(20):
            end_list.append('none')

        for item in RCS['cards']:
            if RCS['cards'] == end_list:
                RCS['mode'], RCS['moves'], RCS['found'] = 0, 0, 0
            if item == 'none':
                found += 1
                if found >= 2:
                    RCS['found'] = int(found / 2)
