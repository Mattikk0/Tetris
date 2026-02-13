import pygame as pg
black = (0,0,0)
dark_grey = (48,48,48)
very_dark_grey = (16,16,16)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
pink = (255,105,180)
yellow = (255,255,0)
orange = (255,165,0)
brown = (139,69,19)
pg.init()
info = pg.display.Info()
screen_width = 1350
screen_height = 1200
two_thirds_width = (2 * screen_width) // 3
two_thirds_height = (2 * screen_height) // 3
one_third_height = screen_height // 3
one_third_width = screen_width // 3
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Tetris')
zone1 = pg.Rect(0, 0, two_thirds_width, screen_height)
zone2 = pg.Rect(two_thirds_width, 0, one_third_width, one_third_height)
zone3 = pg.Rect(two_thirds_width, one_third_height, one_third_width, two_thirds_height)
############################################## Rysowanie ekranu gry
def draw_screen():
    pg.draw.rect(screen, black, zone1)
    pg.draw.rect(screen, black, zone2)
    pg.draw.rect(screen, black, zone3)
    line_width = 5
    pg.draw.line(screen, dark_grey,
                 (zone1.right, 0), (zone1.right, screen_height), line_width)
    pg.draw.line(screen, dark_grey,
                 (zone1.left, 0), (zone1.left, screen_height), line_width)
    pg.draw.line(screen, dark_grey,
                 (zone2.right, 0), (zone2.right, screen_height), line_width)
    pg.draw.line(screen, dark_grey,
                 (0, zone1.bottom), (screen_width, zone1.bottom), line_width)
    pg.draw.line(screen, dark_grey,
                 (0, zone1.top), (screen_width, zone1.top), line_width)
    pg.draw.line(screen, dark_grey,
                 (zone1.right, zone2.bottom), (screen_width, zone2.bottom), line_width)
    for i in range(1, 20):
        pg.draw.line(screen, very_dark_grey,
                     (zone1.left + (line_width / 2) + 1, i * (screen_height // 20)),
                     (zone1.right - (line_width / 2), i * (screen_height // 20)), 2)

    for i in range(1, 15):
        pg.draw.line(screen, very_dark_grey,
                     (i * (screen_height // 20), zone1.top + (line_width / 2)),
                     (i * (screen_height // 20), zone1.bottom - (line_width / 2)), 2)
