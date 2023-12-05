import pygame as pg
from config import RCS
from gui.board_view import BoardView


class GameView:

    def __init__(self):
        self.logo_img = pg.image.load(RCS['img']['logo'])
        self.bg_img = pg.image.load(RCS['img']['background'])
        self.icon = pg.image.load(RCS['img']['back_img'])
        self.font_title = pg.font.SysFont('Dobra-Bold.ttf', 106)
        self.font_bold = pg.font.SysFont('Dobra-Bold.ttf', 72)
        self.font_medium = pg.font.SysFont('Dobra-Medium.ttf', 48)
        self.font_light = pg.font.SysFont('Dobra-Light.ttf', 36)
        self.board_view = BoardView()

    def render_menu(self, display: pg.Surface):
        display.blit(self.bg_img, (0, 0))
        display.blit(self.logo_img, (45, 180))

        text_play = self.font_title.render('Играть', True, (255, 255, 255))
        display.blit(text_play, (75, 320))

        text_rules = self.font_title.render('Правила', True, (255, 255, 255))
        display.blit(text_rules, (75, 400))

        text_quit = self.font_title.render('Выход', True, (255, 255, 255))
        display.blit(text_quit, (75, 480))

        if len(RCS['play']) == 0 and len(RCS['rules']) == 0 and len(RCS['quit']) == 0:
            RCS['play'] = [75, 320, text_play.get_width(), text_play.get_height()]
            RCS['rules'] = [75, 400, text_rules.get_width(), text_rules.get_height()]
            RCS['quit'] = [75, 480, text_quit.get_width(), text_quit.get_height()]

    def render_rules(self, display: pg.Surface):
        display.blit(self.bg_img, (0, 0))
        display.blit(self.font_title.render('Правила игры Disco Pairs', True, (255, 255, 255)), (75, 320))

    def render_game(self, display: pg.Surface):
        display.blit(self.bg_img, (0, 0))
        self.board_view.render(display)
