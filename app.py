import pygame as pg
import random as rd
from config import RCS, COL
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
        play_col = pg.Rect(COL['play'][0], COL['play'][1], COL['play'][2], COL['play'][3])
        rules_col = pg.Rect(COL['rules'][0], COL['rules'][1], COL['rules'][2], COL['rules'][3])
        quit_col = pg.Rect(COL['quit'][0], COL['quit'][1], COL['quit'][2], COL['quit'][3])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:

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
        pos = pg.mouse.get_pos()
        back_col = pg.Rect(COL['back'][0], COL['back'][1], COL['back'][2], COL['back'][3])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                self.board.delete_card(self.display)

                if back_col.collidepoint(pos):
                    RCS['mode'] = 0

        self.clock.tick(RCS['FPS'])

    @staticmethod
    def music():
        pg.mixer.music.load(RCS['sound']['ost'])
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play()

    def run(self):
        rebuild = True
        pg.display.set_caption('Disco Pairs')
        self.music()

        while self.running:
            
            if RCS['mode'] == 0:
                rebuild = True
                self.game_view.render_menu(self.display)
                self.event_check_menu()

            elif RCS['mode'] == 1:
                self.game_view.render_rules(self.display)
                self.event_check_rules()

            elif RCS['mode'] == 2:
                if rebuild:
                    RCS['cards'] = GameCard.all_cards()
                    rd.shuffle(RCS['cards'])
                    rebuild = False
                self.game_view.render_game(self.display)
                self.board.stats()
                self.event_check_game()

            elif RCS['mode'] == 3:
                self.game_view.render_replay(self.display)

            pg.display.update()

        pg.quit()
