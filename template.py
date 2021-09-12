import pygame as pg

class PygameScreen:

    def __init__(self, title, color, size):
        self.title = title
        self.color = color
        self.size = size
        self.screen = pg.display.set_mode(size)
        self.sync_screen()
    
    def sync_screen(self):
        self.screen = pg.display.set_mode(self.size)
        self.screen.fill(self.color)
        pg.display.set_caption(self.title)

    def change_size(self, size):
        self.size = size
        self.screen = pg.display.set_mode(size)
    
    def change_color(self, color):
        self.color = color
        self.screen.fill(color)
    
    def change_title(self, title):
        self.title = title
        pg.display.set_caption(title)