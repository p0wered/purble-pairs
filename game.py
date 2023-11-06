import random
import pygame as pg
from card import GameCard
from board import GameBoard

pg.init()

# параметры
FPS = 60
screen_width, screen_height = 1366, 768
pg.mixer.music.load('src/ambient.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(0.3)
pg.display.set_caption('Purble Pairs')

# картинки
bg_img = pg.image.load('src/bg.jpg')

# переменные
display = pg.display.set_mode((screen_width, screen_height))
running = True
clock = pg.time.Clock()
cards = GameCard.all_cards()
random.shuffle(cards)
col_cloud_1 = pg.Rect(0, 0, 0, 0)


# экран
def display_redraw():
    display.blit(bg_img, (0, 0))
    main_board = GameBoard
    main_board.render(display, cards)
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
            print('mouse clicked')
    clock.tick(FPS)
    return running


while running:
    display_redraw()
    running = event_processing()

pg.quit()