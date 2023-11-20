import pygame as pg
from config import RCS


class CardView:
    back_img = pg.image.load(RCS['img']['back_img'])
    margin_x = 4
    margin_y = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def draw(display: pg.Surface, image_src, x, y):
        if image_src is not None:
            image = pg.image.load(image_src)
            display.blit(image, (x, y))
        else:
            display.blit(pg.Surface((128, 128), pg.SRCALPHA), (x, y))
