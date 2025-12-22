from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

    def __add__(self, obj2):
        first = self.name[:int(len(self.name)/2)]
        second = obj2.name[:int(len(self.name)/2)]
        return first+second

class Square(Shape):
    def __init__(self, length = 0):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Square have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a+self.b+self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def fact(self):
        return "Длина любой стороны треугольника меньше суммы двух других"

a = Square()
b = Circle(10)

shapes=[a,b]
for i in shapes:
    print(i.fact())
    print(i.area())

print(a+b)
