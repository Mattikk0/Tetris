import pygame as pg
import Gameplay_Actions
from GameFolders.Gameplay_Actions import game_board

black = (0,0,0)
dark_grey = (48,48,48)
very_dark_grey = (16,16,16)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
pink = (255,105,180)
yellow = (255,255,0)
orange = (255,165,0)
brown = (139,69,19)
colors = [blue, pink, orange, brown, red, green, yellow]
#pg.init()
screen_width = 1350
screen_height = 1200
two_thirds_width = (2 * screen_width) // 3
two_thirds_height = (2 * screen_height) // 3
one_third_height = screen_height // 3
one_third_width = screen_width // 3
#screen = pg.display.set_mode((screen_width, screen_height))
#pg.display.set_caption('Tetris')
zone1 = pg.Rect(0, 0, two_thirds_width, screen_height)
zone2 = pg.Rect(two_thirds_width, 0, one_third_width, one_third_height)
zone3 = pg.Rect(two_thirds_width, one_third_height, one_third_width, two_thirds_height)
screen = None

def init_pygame():
    global screen
    pg.init()
    info = pg.display.Info()
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Tetris")
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
    for i in range(1, Gameplay_Actions.game_board.__len__()):
        for j in range(Gameplay_Actions.game_board[i].__len__()):
            cell_value = Gameplay_Actions.game_board[i][j]
            if cell_value != 0 and cell_value != 1:
                color = colors[cell_value - 2]
                pg.draw.rect(screen, color, (zone1.left + j * (zone1.width // 15),
                                            zone1.top + (i - 1) * (zone1.height // 20),
                                            zone1.width // 15,
                                            zone1.height // 20))

def draw_figure(figure):
    cell_width = zone1.width // 15
    cell_height = (zone1.height // 20)
    for y in range(figure.height):
        for x in range(figure.width):
            if figure.x_left + x < len(game_board[0]) and figure.structure[y][x] == 1 and not game_board[figure.y_top + y][figure.x_left + x] > 1:
                x_pos = zone1.left + (figure.x_left + x) * cell_width
                y_pos = zone1.top + (figure.y_top + y - 1) * cell_height
                if 0 <= x_pos < zone1.right and 0 <= y_pos < zone1.bottom:
                    pg.draw.rect(screen, figure.color, (x_pos, y_pos, cell_width, cell_height))


def draw_next_figure(figure):
    cell_width = zone2.width // 7
    cell_height = zone2.height // 7
    for y in range(figure.height):
        for x in range(figure.width):
            if figure.structure[y][x] == 1:
                x_pos = zone2.left + (x + 2) * cell_width
                y_pos = zone2.top + (y + 2) * cell_height
                pg.draw.rect(screen, figure.color, (x_pos, y_pos, cell_width, cell_height))

def game_over_screen(c):
    screen.fill(black)
    font_big = pg.font.Font(None, 100)
    font_med = pg.font.Font(None, 80)
    font_small = pg.font.Font(None, 50)
    text = font_big.render("GAME OVER!", True, white)
    score = font_med.render(f"Score: {c}", True, white)
    exit_game = font_small.render("(Press escape to exit)", True, white)
    restart_game = font_small.render("(Press space to restart)", True, white)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    text_scr = score.get_rect(center=(screen_width // 2, (screen_height // 2) + 50))
    text_exit = exit_game.get_rect(center=(screen_width // 2, (screen_height // 2) + 150))
    text_restart = restart_game.get_rect(center=(screen_width // 2, (screen_height // 2) + 250))
    screen.blit(text, text_rect)
    screen.blit(score, text_scr)
    screen.blit(exit_game, text_exit)
    screen.blit(restart_game, text_restart)
    pg.display.flip()

def draw_score(score):
    font = pg.font.Font(None, 70)
    text = font.render(f"Score: {int(score)}", True, white)
    text_rect = text.get_rect(center=((zone3.right + zone3.left) // 2, (zone3.top + zone3.bottom) // 2))
    screen.blit(text, text_rect)
    pg.display.flip()

