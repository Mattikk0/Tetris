import Figure_Actions
import Gameplay_Actions

def movement(figure, pg, event):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            figure.x_left -= 1
            figure.x_right -= 1
        elif event.key == pg.K_RIGHT:
            figure.x_left += 1
            figure.x_right += 1
        elif event.key == pg.K_UP:
            Figure_Actions.rotate_figure(figure)
        elif event.key == pg.K_DOWN:
            Gameplay_Actions.movement(figure, False)

