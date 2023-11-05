import random
import pygame as pg
from card import GameCard

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
card_cloud = pg.image.load('images/blue.png')
card_tree = pg.image.load('images/red.png')
card_blob = pg.image.load('images/yellow.png')
card_flower = pg.image.load('images/purple.png')

# переменные
display = pg.display.set_mode((screen_width, screen_height))
running = True
clock = pg.time.Clock()
cards = GameCard.all_cards()
random.shuffle(cards)
shift = 0


# экран
def display_redraw():
    global shift
    display.blit(bg_img, (0, 0))
    for card in cards:
        shift *= 80
        card = str(card)
        if card == 'card_cloud':
            display.blit(card_cloud, (shift, 0))
        if card == 'card_tree':
            display.blit(card_cloud, (shift, 0))
        if card == 'card_blob':
            display.blit(card_cloud, (shift, 0))
        if card == 'card_flower':
            display.blit(card_cloud, (shift, 0))
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
            pos = pg.mouse.get_pos()
            if test_cl.collidepoint(pos):
                print(cards)
    clock.tick(FPS)
    return running


while running:
    display_redraw()
    running = event_processing()

pg.quit()
