import random

from GameFolders import Drawing_Actions

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
figures = [[[1,1,1,1]], #I - 0
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
colors = [blue, pink, orange, brown, red, green, yellow]

class Figure:
    def __init__(self, number):
        self.number = number
        self.structure = figures[number]
        self.color = colors[number]
        self.x_left = 0
        self.x_right = 0
        self.y_top = 0
        self.left_bot = 0
        self.height = len(self.structure)
        self.width = max(len(row) for row in self.structure)

def rotate_figure(figure):
    import Gameplay_Actions
    rotated_structure = []
    old_height = figure.height
    old_width = figure.width
    if figure.number == 0:
        for x in range(figure.width):
            new_row = []
            for y in range(figure.height):
                new_row.append(figure.structure[y][x])
            rotated_structure.append(new_row)
    else:
        for x in range(figure.width):
            new_row = []
            for y in range(figure.height-1, -1, -1):
                new_row.append(figure.structure[y][x])
            rotated_structure.append(new_row)
    temp = figure.height
    figure.height = figure.width
    figure.width = temp
    figure.structure = rotated_structure
    figure.x_left += (old_width // 2) - (figure.width // 2)
    figure.y_top += (old_height // 2) - (figure.height // 2)
    figure.x_right = figure.x_left + figure.width - 1
    figure.y_bot = figure.y_top + figure.height - 1
    if figure.y_bot > 19:
        figure.y_bot = 19
        figure.y_top = figure.y_bot - figure.height + 1
    Gameplay_Actions.put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))

def undo_rotate_figure(figure, structure):
    figure.structure = structure
    figure.x_left = max(figure.x_left, 0)
    figure.x_right = figure.x_left + figure.width - 1
    figure.y_top = max(figure.y_top, 0)
    figure.y_bot = figure.y_top + figure.height - 1
    figure.height = len(figure.structure)
    figure.width = max(len(row) for row in figure.structure)

def choose_figure():
    index = random.randint(0, len(figures)-1)
    return index