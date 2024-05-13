"""
1. Define an abstract class "Animal" with an abstract method "say".
Hint: Use "abc" module

2. Defind a child class "Dog", drived from "Animal".
Also, define a method "say" which prints the message "I speak Booooo".

"""

from abc import ABC, abstractmethod


# Define the abstract class 'Animal' below
# with abstract method 'say'
class Animal(ABC):

    @abstractmethod
    def say(self):
        pass


# Define class Dog derived from Animal
# Also define 'say' method inside 'Dog' class
class Dog(Animal):

    def say(self):
        return "I speak Booooo"


d1 = Dog()
print("Dog,'d1', says :", d1.say())
