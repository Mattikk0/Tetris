import sys
import pygame as pg
import Drawing_Actions
import Figure_Actions
import Gameplay_Actions
import Keyboard_Actions
from GameFolders import Menu_Actions
from GameFolders.Gameplay_Actions import after_game_over

stopped = False


def main():
    global stopped
    score = 0
    Menu_Actions.launch_menu()
    delay = Menu_Actions.set_delay
    Drawing_Actions.init_pygame()
    Gameplay_Actions.reset_board()
    running = True

    clock = pg.time.Clock()

    Drawing_Actions.draw_screen()
    pg.display.flip()

    last_drop_time = pg.time.get_ticks()

    figure = Figure_Actions.Figure(Figure_Actions.choose_figure())
    next_figure = Figure_Actions.Figure(Figure_Actions.choose_figure())

    Gameplay_Actions.movement(figure, True)

    Drawing_Actions.draw_screen()
    Drawing_Actions.draw_figure(figure)
    Drawing_Actions.draw_next_figure(next_figure)
    pg.display.flip()

    while running:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit(0)

            Keyboard_Actions.movement(figure, pg, event)

        now = pg.time.get_ticks()

        if now - last_drop_time > delay:
            Gameplay_Actions.movement(figure, False)
            last_drop_time = now

            if stopped and not Gameplay_Actions.game_over():
                figure = next_figure
                next_figure = Figure_Actions.Figure(Figure_Actions.choose_figure())
                Gameplay_Actions.movement(figure, True)
                stopped = False

        if not Gameplay_Actions.game_over():
            Drawing_Actions.draw_screen()
            Drawing_Actions.draw_figure(figure)
            Drawing_Actions.draw_next_figure(next_figure)
            pg.display.flip()
        else:
            Drawing_Actions.game_over_screen(score)
            pg.display.flip()
            after_game_over()


if __name__ == "__main__":
    main()