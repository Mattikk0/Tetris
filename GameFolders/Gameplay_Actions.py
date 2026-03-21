import sys
import pygame as pg
full_rows = []
number_of_full_rows = 0
lines_deleted = 0
game_board = [[0 for i in range(15)] for j in range(21)]
def clear_board():
    for x in range(15):
        for y in range(len(game_board)):
            if game_board[y][x] == 1:
                game_board[y][x] = 0

def put_structure_on_board(figure, position):
    #struktura position: (x_left, x_right, y_top, y_bot)
    clear_board()
    x_left, x_right, y_top, y_bot = position
    max_x = x_right + 1
    max_y = y_bot + 1

    max_x = min(max_x, len(game_board[0]))
    x_left = max(x_left, 0)
    max_y = min(max_y, len(game_board))
    y_top = max(y_top, 0)

    for x in range(x_left, max_x):
        for y in range(y_top, max_y):
            fig_x = x - x_left
            fig_y = y - y_top
            if 0 <= fig_y < len(figure.structure) and 0 <= fig_x < len(figure.structure[0]):
                if figure.structure[fig_y][fig_x] == 1:
                    if not game_board[y][x] > 1:
                        game_board[y][x] = 1

def movement(figure, new_figure):
    import __main__ as Main_Game
    if new_figure:
        figure.x_left = 6
        figure.x_right = figure.width + figure.x_left - 1
        figure.y_top = 0
        figure.y_bot = figure.y_top + figure.height - 1
        put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))
    else:
        can_move_down = True
        for fig_x in range(figure.width):
            for fy in range(figure.height - 1, -1, -1):
                if fig_x < len(figure.structure[fy]) and figure.structure[fy][fig_x] == 1:
                    board_x = figure.x_left + fig_x
                    below_y = figure.y_top + fy + 1
                    if below_y >= len(game_board) or (game_board[below_y][board_x] != 0 and game_board[below_y][board_x] != 1):
                        can_move_down = False
                    break
        if can_move_down:
            figure.y_top += 1
            figure.y_bot += 1
            put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))
        else:
            x_left = figure.x_left
            y_top = figure.y_top
            for fy in range(len(figure.structure)):
                for fx in range(len(figure.structure[fy])):
                    if figure.structure[fy][fx] == 1:
                        board_x = x_left + fx
                        board_y = y_top + fy
                        if 0 <= board_x < len(game_board[0]) and 0 <= board_y < len(game_board):
                            game_board[board_y][board_x] = figure.number + 2
            Main_Game.stopped = True
            full_rows.clear()
            remove_full_lines()
            lower_lines()
            return

def check_full_lines(line_number):
    for x in range(len(game_board[0])):
        if game_board[line_number][x] == 0:
            return -1
    full_rows.append(line_number)
    return line_number

def remove_full_lines():
    global number_of_full_rows
    for y in range(len(game_board)):
        temp = check_full_lines(y)
        if temp != -1:
            for x in range(len(game_board[temp])):
                game_board[temp][x] = 0
    number_of_full_rows = len(full_rows)
    return number_of_full_rows
def check_highest_row():
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if game_board[y][x] > 1:
                return y
    return -1

def lower_lines():
    highest_row = check_highest_row()
    for row in full_rows:
        if row > highest_row:
            for y in range(row, -1, -1):
                for x in range(len(game_board[0])):
                    if not y-1 < 0:
                        game_board[y][x] = game_board[y-1][x]

def game_over():
    if check_highest_row() == 0:
        global lines_deleted
        lines_deleted = 0
        return True
    return False

def after_game_over():
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()
    if keys[pg.K_SPACE]:
        pg.event.post(pg.event.Event(pg.USEREVENT, {"action": "RESTART"}))

def reset_board():
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            game_board[y][x] = 0

def count_the_score(delay):
    global number_of_full_rows
    global lines_deleted
    temp = 0 #mnożnik wyniku
    match number_of_full_rows:
        case 0:
            return 0
        case 1:
            temp = 100
        case 2:
            temp = 200
        case 3:
            temp = 500
        case 4:
            temp = 1000
    lines_deleted += number_of_full_rows
    number_of_full_rows = 0
    return (100/delay)*temp

def decreasing_delay(delay):
    global lines_deleted
    if lines_deleted >= 10:
        lines_deleted = 0
        return 0.8 * delay
    return delay

def on_high_score_screen():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            return "EXIT"
    return None



