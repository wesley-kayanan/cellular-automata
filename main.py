import pygame as pg
import numpy as np

from constant import *
from template import *
from rules import *

# Initialization
pg.init()

COLOR = Color()
DIMENSION = Dimension(600, 400)

timer = Timer(500)
grid_rect = pg.Rect(DIMENSION.GRID_RECT)
state_colors = np.array([COLOR.RED, COLOR.WHITE])
current_state = np.random.randint(2, size=(30, 30))

# Start
ps = PygameScreen('Cellular Automata', COLOR.GRAY, DIMENSION.SCREEN)
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if timer.check_update():
        grid = get_next_state(current_state)
        surface = pg.surfarray.make_surface(state_colors[grid])
        surface = pg.transform.scale(surface, DIMENSION.GRID)

        ps.screen.blit(surface, DIMENSION.CENTER)
        pg.display.update(grid_rect)