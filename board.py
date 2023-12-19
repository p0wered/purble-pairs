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

                    while True:
                        elapsed = timer() - start
                        CardView.draw_two(display, src1, src2, i1, i2)
                        if elapsed > 0.6:
                            break

                    if GameCard.compare(i1, i2):
                        RCS['cards'][i1], RCS['cards'][i2] = 'none', 'none'

                    RCS['clicked'].clear()

    @staticmethod
    def stats(moves):
        """Статистика игровой сессии"""
        import json
        end_list = []
        found = 0

        with open('userdata.json') as f:
            data = json.load(f)
            record = data['record']

        for k in range(20):
            end_list.append('none')

        if moves >= 25:
            RCS['status'] = 'lose'
            RCS['mode'] = 3

        for item in RCS['cards']:

            if RCS['cards'] == end_list:
                result = RCS['moves']
                if result < record:
                    data['record'] = result
                    with open('userdata.json', 'w') as f:
                        json.dump(data, f)
                RCS['status'] = 'win'
                RCS['mode'] = 3

            if item == 'none':
                found += 1
                if found >= 2:
                    RCS['found'] = int(found / 2)
