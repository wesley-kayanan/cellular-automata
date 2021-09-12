import pygame as pg
from constant import *
from template import *

# Initializations

COLOR = Color()
SIZE = Size()
ps = PygameScreen('Cellular Automata', COLOR.WHITE, SIZE.DEFAULT)

pg.display.flip()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False