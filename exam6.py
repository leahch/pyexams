

class Figure:
    def square(self):
        return 0

class Cube(Figure):
    def __init__(self, x):
        self.x = x

    def square(self):
        return self.x**3

class AbstractFigure(Figure):
    pass
 
c1 = Cube(2)
print(c1.square())
a1 = AbstractFigure()
print(a1.square())





    


