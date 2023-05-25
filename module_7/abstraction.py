""" Example 1: Creating an abstract class using the abc module: """

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage
rectangle = Rectangle(4, 6)
print(rectangle.area())      # Output: 24
print(rectangle.perimeter()) # Output: 20


""" Using the abc module's abstractmethod decorator: """

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

