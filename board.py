import pygame as pg
from gui.board_view import BoardView
from config import GEOM, RCS


class GameBoard:
    @staticmethod
    def delete_card():
        """Удаляет две выбранные одинаковые карточки"""
        pos = pg.mouse.get_pos()
        for i, position in enumerate(RCS['positions']):
            col_card = pg.Rect(position, (GEOM['card_width'], GEOM['card_height']))
            if col_card.collidepoint(pos):
                RCS['clicked'].append(i)
                print(f'Выбрана карточка {RCS["cards"][i]}')
                if len(RCS['clicked']) == 2:
                    i1 = RCS['clicked'][0]
                    i2 = RCS['clicked'][1]
                    if RCS['cards'][i1] == RCS['cards'][i2] and i1 != i2:
                        RCS['cards'][i1], RCS['cards'][i2] = 'none', 'none'
                    else:
                        print('Неверно')
                    RCS['clicked'].clear()

    # @staticmethod
    # def game_finished():
    #     count = 0
    #     for item in RCS['cards']:
    #         if item == 'none':
    #             count += 1
    #             if count == len(RCS['cards']):
    #
