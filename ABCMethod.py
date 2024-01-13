


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Creating objects and setting values
circle_obj = Circle(radius=3)
square_obj = Square(side=4)

# Accessing areas
circle_area = circle_obj.area()
square_area = square_obj.area()

# Printing results
print("Circle Area: {}".format(circle_area))
print("Square Area: {}".format(square_area))



