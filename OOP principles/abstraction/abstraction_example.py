# Example explained:
# The Shape abstract class defines a common interface that all shapes must implement (area() and perimeter()), 
# without specifying how these calculations should be done. 
# Different shape classes (like Circle and Rectangle) provide their specific implementations. 
# A function working with shapes can rely on these methods existing, without knowing how each shape calculates its properties.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return "This is a geometric shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def description(self):
        return f"This is a circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def description(self):
        return f"This is a rectangle with length {self.length} and width {self.width}"


# Can use code with different shapes
def print_shape_info(shape):
    print(shape.description()) 
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Create shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_shape_info(circle)
print_shape_info(rectangle)