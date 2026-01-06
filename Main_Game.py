import sys
import random
import pygame as pg
## Szerokość 10 wysokość 20
running = True
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
screen_width = 1350#info.current_w
screen_height = 1200#info.current_h
two_thirds_width = (2 * screen_width) // 3
two_thirds_height = (2 * screen_height) // 3
one_third_height = screen_height // 3
one_third_width = screen_width // 3
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Tetris')
zone1 = pg.Rect(0, 0, two_thirds_width, screen_height)
zone2 = pg.Rect(two_thirds_width, 0, one_third_width, one_third_height)
zone3 = pg.Rect(two_thirds_width, one_third_height, one_third_width, two_thirds_height)
game_board = [[0 for i in range(15)] for j in range(20)]
figures = [[1,1,1,1], #I - 0
           [[0,1,0], #T - 1
            [1,1,1]],
           [[1,0,0], #J - 2
            [1,1,1]],
           [[0,0,1],#L - 3
            [1,1,1]],
           [[1,1,0], #Z - 4
            [0,1,1]],
           [[0,1,1], #S - 5
            [1,1,0]],
           [[1,1], #O - 6
            [1,1]]]
colors = [blue, red, green, orange, pink, yellow, brown]
############################################## Liczenie jedynek w strukturze figury (pomaga w liczeniu jej szerokości)
def count_ones(row1, row2):
    count = 0
    for cell in row1:
        if cell == 1:
            count += 1
    for cell in row2:
        if cell == 1:
            count += 1
    for i in range(0, len(row1)):
        if row1[i] == 1 & row2[i] == 1:
            count-=1
    return count
############################################## Klasa Figury
class Figure:
    def __init__(self, number):
        self.number = number
        self.structure = figures[number]
        self.color = colors[number]
        if number == 0:
            self.height = 1
            self.width = 4
        else:
            self.height = len(self.structure)
            self.width = count_ones(self.structure[0], self.structure[1])

############################################## Obracanie figury
def rotate_figure(figure):
    if figure.number == 0:
        temp = figure.height
        figure.height = figure.width
        figure.width = temp
        return
    rotated_structure = []
    for x in range(figure.width):
        new_row = []
        for y in range(figure.height-1, -1, -1):
            new_row.append(figure.structure[y][x])
        rotated_structure.append(new_row)
    figure.structure = rotated_structure
    figure.height = len(figure.structure)
    figure.width = len(figure.structure[0])


############################################## Wybór figury
def choose_figure():
    index = random.randint(0, len(figures)-1)
    return index
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


############################################# Pętla gry
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit(0)

    draw_screen()
    pg.display.flip()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        print("Left key pressed")
    if keys[pg.K_RIGHT]:
        print("Right key pressed")

    if keys[pg.K_UP]:
        print("Up key pressed")

    if keys[pg.K_DOWN]:
        print("Down key pressed")

