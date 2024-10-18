import math

# Base class: Shape
class Shape:
    def area(self):
        """Method to calculate area, must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override this method")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Override the area method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with radius."""
        self.radius = radius
    
    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
