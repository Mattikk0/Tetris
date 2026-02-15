import Figure_Actions
import Gameplay_Actions
from GameFolders.Gameplay_Actions import game_board


def movement(figure, pg, event):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            if not figure.x_left == 0:
                figure.x_left -= 1
                figure.x_right -= 1
        elif event.key == pg.K_RIGHT:
            if not figure.x_right == 14:
                figure.x_left += 1
                figure.x_right += 1
        elif event.key == pg.K_UP:
            Figure_Actions.rotate_figure(figure)
        elif event.key == pg.K_DOWN:
            if not figure.y_bot > 18:
                for i in range(figure.width):
                    if game_board[figure.y_bot][i] + 1 != 0 and game_board[figure.y_bot][i] + 1 != 1 and game_board[figure.y_bot][i] != 0 and game_board[figure.y_bot][i] != 1:
                        return
                # to zrobić

