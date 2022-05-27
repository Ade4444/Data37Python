
class Rectangle():

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return (self.width + self.length) * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.length = length


s = Square(5)
print(s.get_area())
print(s.get_perimeter())

print(isinstance(s, Square))
print(isinstance(s, Rectangle))
print(isinstance(Square, Rectangle))

