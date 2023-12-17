import pygame as pg
from config import RCS, COL
from gui.board_view import BoardView


class GameView:

    def __init__(self):
        self.logo_img = pg.image.load(RCS['img']['logo'])
        self.bg_img = pg.image.load(RCS['img']['background'])
        self.icon = pg.image.load(RCS['img']['back_img'])
        self.height = RCS['display_height']
        self.font_title = pg.font.SysFont('Dobra-Bold.ttf', 106)
        self.font_bold = pg.font.SysFont('Dobra-Bold.ttf', 72)
        self.font_medium = pg.font.SysFont('Dobra-Medium.ttf', 46)
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

        if len(COL['play']) == 0 and len(COL['rules']) == 0 and len(COL['quit']) == 0:
            COL['play'] = [75, 320, text_play.get_width(), text_play.get_height()]
            COL['rules'] = [75, 400, text_rules.get_width(), text_rules.get_height()]
            COL['quit'] = [75, 480, text_quit.get_width(), text_quit.get_height()]

    def render_rules(self, display: pg.Surface):
        display.blit(self.bg_img, (0, 0))
        display.blit(self.font_bold.render('Правила игры Disco Pairs', True, (255, 255, 255)), (50, 50))
        display.blit(self.font_medium.render('Цель игры - найти все совпадающие по мотиву картинки и собрать их в пары', True, (255, 255, 255)), (50, 125))
        display.blit(self.font_medium.render('Каждый ход игрок выбирает две карты для открытия', True, (255, 255, 255)), (50, 200))
        display.blit(self.font_medium.render('Ходы игрока ограничены по времени и числу попыток', True, (255, 255, 255)), (50, 275))

        text_back = self.font_bold.render('< Назад', True, (255, 255, 255))
        display.blit(text_back, (50, self.height - 100))

        if len(COL['back']) == 0:
            COL['back'] = [50, self.height - 100, text_back.get_width(), text_back.get_height()]

    def render_game(self, display: pg.Surface):
        display.blit(self.bg_img, (0, 0))
        self.board_view.render(display)
        display.blit(self.font_bold.render(f'Количество ходов: {str(RCS["moves"])} / 15', True, (255, 255, 255)), (660, 80))
        display.blit(self.font_bold.render(f'Найдено пар: {str(RCS["found"])} / 15', True, (255, 255, 255)), (660, 180))

    def render_replay(self, display: pg.Surface):
        text_play = self.font_title.render('Игра завершена', True, (255, 255, 255))
        display.blit(text_play, (75, 320))

