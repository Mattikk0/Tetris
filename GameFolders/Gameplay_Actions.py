
import time
import Drawing_Actions
import Keyboard_Actions
game_board = [[0 for i in range(15)] for j in range(21)]

def clear_board():
    for x in range(15):
        for y in range(21):
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
                    if game_board[y][x] != 2:
                        game_board[y][x] = 1

def movement(figure, new_figure):
    import Main_Game
    if new_figure:
        figure.x_left = 5
        figure.x_right = figure.width + figure.x_left - 1
        figure.y_top = 0
        figure.y_bot = figure.y_top + figure.height - 1
        put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))
    else:
        figure.y_top += 1
        figure.y_bot += 1
        put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))
        print("-----------------------------------------------\n")
        for row in game_board:
            print(str(row) + "\n")


    if check_if_stopped(figure):
        x_left = figure.x_left
        y_top = figure.y_top
        for fy in range(len(figure.structure)):
            for fx in range(len(figure.structure[fy])):
                if figure.structure[fy][fx] == 1:
                    board_x = x_left + fx
                    board_y = y_top + fy
                    if 0 <= board_x < len(game_board[0]) and 0 <= board_y < len(game_board):
                        game_board[board_y][board_x] = 2
        Main_Game.stopped = True
    print("-----------------------------------------------\n")
    for row in game_board:
        print(str(row) + "\n")

def check_if_stopped(figure):
    for fig_x in range(figure.width):
        board_x = figure.x_left + fig_x
        if board_x < 0 or board_x >= len(game_board[0]):
            continue
        for fy in range(figure.height - 1, -1, -1):
            if fig_x < len(figure.structure[fy]) and figure.structure[fy][fig_x] == 1:
                below_y = figure.y_top + fy + 1
                if below_y >= len(game_board) or game_board[below_y][board_x] == 2:
                    return True
    return False