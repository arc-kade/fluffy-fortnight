# #abstract base class
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())

#absract method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

# Concrete method
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return "Moving"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
print(dog.make_sound())
cat = Cat()
print(cat.make_sound())

# Abstract properties
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)

# Self instantiation

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

animal = Animal()