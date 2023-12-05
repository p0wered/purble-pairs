import pygame as pg
import random as rd
from config import RCS
from gui.game_view import GameView
from board import GameBoard
from card import GameCard


class Application:

    def __init__(self):
        pg.init()
        pg.font.init()
        self.running = True
        self.current_mode = RCS['mode']
        self.game_view = GameView()
        self.board = GameBoard
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((RCS['display_width'], RCS['display_height']))

    def event_check_menu(self):
        pos = pg.mouse.get_pos()
        play_col = pg.Rect(RCS['play'][0], RCS['play'][1], RCS['play'][2], RCS['play'][3])
        rules_col = pg.Rect(RCS['rules'][0], RCS['rules'][1], RCS['rules'][2], RCS['rules'][3])
        quit_col = pg.Rect(RCS['quit'][0], RCS['quit'][1], RCS['quit'][2], RCS['quit'][3])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                self.board.delete_card(self.display)

                if play_col.collidepoint(pos):
                    RCS['mode'] = 2

                elif rules_col.collidepoint(pos):
                    RCS['mode'] = 1

                elif quit_col.collidepoint(pos):
                    self.running = False

        self.clock.tick(RCS['FPS'])

    def event_check_game(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                self.board.delete_card(self.display)

        self.clock.tick(RCS['FPS'])

    def event_check_rules(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                self.board.delete_card(self.display)

        self.clock.tick(RCS['FPS'])

    @staticmethod
    def music():
        pg.mixer.music.load(RCS['sound']['ost'])
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play()

    def run(self):
        pg.display.set_caption('Disco Pairs')
        RCS['cards'] = GameCard.all_cards()
        rd.shuffle(RCS['cards'])
        self.music()

        while self.running:
            
            if RCS['mode'] == 0:
                self.game_view.render_menu(self.display)
                self.event_check_menu()

            elif RCS['mode'] == 1:
                self.game_view.render_rules(self.display)
                self.event_check_rules()

            elif RCS['mode'] == 2:
                self.game_view.render_game(self.display)
                self.event_check_game()

            pg.display.update()

        pg.quit()
