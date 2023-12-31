import pygame as pg
from config import RCS


class CardView:

    @staticmethod
    def draw_selected(display: pg.Surface, image_src, x, y):
        if image_src is not None:
            image = pg.image.load(image_src)
            display.blit(image, (x, y))
        else:
            display.blit(pg.Surface((128, 128), pg.SRCALPHA), (x, y))

    @staticmethod
    def draw_back(display: pg.Surface, image_src, x, y):
        if image_src is not None:
            back = pg.image.load(RCS['img']['back_img'])
            display.blit(back, (x, y))
        else:
            div = pg.Surface((128, 128), pg.SRCALPHA)
            div.fill((255, 255, 255, 64))
            display.blit(div, (x, y))

    @staticmethod
    def draw_two(display: pg.Surface, source_1, source_2, index_1, index_2):
        CardView.draw_selected(display, source_1, RCS['positions'][index_1][0], RCS['positions'][index_1][1])
        CardView.draw_selected(display, source_2, RCS['positions'][index_2][0], RCS['positions'][index_2][1])
        pg.display.update()
