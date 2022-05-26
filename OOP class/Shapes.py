class Rectangle():

    def __init__(self, width, length):

        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return (self.width + self.length) * 2

class Square(Rectangle):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.width = width
        self.length = length


rect_ = Rectangle(6, 4)
squa_ = Square(4, 4)

print(rect_.get_area())
print(rect_.get_perimeter())
print(squa_.get_area())
print(squa_.get_perimeter())

