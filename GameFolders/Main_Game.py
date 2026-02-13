import sys
import pygame as pg
import Drawing_Actions
import Figure_Actions
import Gameplay_Actions
import Keyboard_Actions

running = True
pg.init()
clock = pg.time.Clock()
stopped = False
Drawing_Actions.draw_screen()
pg.display.flip()

last_drop_time = pg.time.get_ticks()
delay = 1000

figure = Figure_Actions.Figure(Figure_Actions.choose_figure())
Gameplay_Actions.movement(figure, True)
Drawing_Actions.draw_screen()
pg.display.flip()
############################################# Pętla gry
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
        if stopped:
            figure = Figure_Actions.Figure(Figure_Actions.choose_figure())
            Gameplay_Actions.movement(figure, True)
            stopped = False
    Drawing_Actions.draw_screen()
    pg.display.flip()

