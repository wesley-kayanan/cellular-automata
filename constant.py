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

class Size():
    @constant
    def DEFAULT():
        return (500, 500)