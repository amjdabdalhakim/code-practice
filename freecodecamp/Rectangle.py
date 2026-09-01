class Rectangle:
    def __init__(self, width, hight):
        self.w = width
        self.h = hight
    def __str__(self):
        return f"Rectangle(width: {self.w}, hight: {self.h})"
    def set_width(self, width):
        self.w = width
    def set_hight(self, hight):
        self.h = hight
    def get_perimeter(self):
        return 2 * (self.w + self.h)
    def get_area(self):
        return self.w * self.h
    def show(self):
        rect = ""
        for h in range(self.h):
            for w in range(self.w):
                rect += '*'
            rect += '\n' if h != self.h -1  else ''
        return rect

class Square(Rectangle):
    def __init__(self, side):
        self.w, self.h = side, side
    def __str__(self):
        return f"Square(side: {self.w})"
    def set_side(self, side):
        self.w, self.h = side, side
    def set_width(self, side):
        self.set_side(side)
    def set_hight(self, side):
        self.set_side(side)
rect = Rectangle(10, 5)
print(rect.show())   

sqr = Square(5)   
print(sqr.show())