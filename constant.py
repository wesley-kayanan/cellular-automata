def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Color():
    @constant
    def WHITE():
        return (255,255,255)
    @constant
    def RED():
        return (250, 90, 120)
    @constant
    def YELLOW():
        return (120, 250, 90)
    @constant
    def GRAY():
        return (30, 30, 30)

class Dimension:

    def __init__(self, screen_size, grid_size):
        self.screen_size = screen_size
        self.grid_size = grid_size

    @property
    def SCREEN(self):
        return (self.screen_size, self.screen_size)

    @property
    def GRID(self):
        return (self.grid_size, self.grid_size)

    @property
    def CENTER(self):
        return ((self.screen_size - self.grid_size)/2, (self.screen_size - self.grid_size)/2)
    
    @property
    def GRID_RECT(self):
        center = (self.screen_size - self.grid_size)/2

        return (center, center, self.screen_size - center, self.screen_size - center)
    