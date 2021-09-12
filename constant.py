def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Color(object):
    @constant
    def WHITE():
        return (255,255,255)

COLOR = Color()