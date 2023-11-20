import random
import pygame as pg
from card import GameCard
from board import GameBoard
from gui.board_view import BoardView
from config import RCS

pg.init()

# параметры
pg.mixer.music.load(RCS['sound']['ost'])
pg.mixer.music.play()
pg.mixer.music.set_volume(0.3)
pg.display.set_caption('Disco Pairs')
pg.font.SysFont('arial', 36)

# картинки
bg_img = pg.image.load('src/bg.png')

# переменные
ico = pg.image.load('cards/back.png')
pg.display.set_icon(ico)
display = pg.display.set_mode(RCS['display'])
running = True
clock = pg.time.Clock()
RCS['cards'] = GameCard.all_cards()
random.shuffle(RCS['cards'])
main_board = GameBoard


# экран
def display_redraw():
    display.blit(bg_img, (0, 0))
    BoardView.render(display)
    pg.display.update()


# нажатие клавиш
def event_processing():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
            main_board.delete_card()
    clock.tick(RCS['FPS'])
    return running


while running:
    display_redraw()
    running = event_processing()

pg.quit()
