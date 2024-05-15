"""
2. Problem 2 - Unit Testing using doctest in Python

Complete the definition of class "Cicle" with the following spectifications:
 - Define doctest for '__init__' which creates a circle 'c1' with raidus 2.5, and checks if th accessing attribute 'radius', returns the value 2.5.
 - Define class method 'area' which computes the area of a circle, and returns the value rounded off to 2 decimals.
 Hint: Use 'pi' value from the 'math' module.
 - Define doctest for 'area' which creates a circle 'c1' with raidus 2.5, and checks if the area of the circle is 19.63.
 - Define class method 'circumference' which computes the circumference of a circle, and returns the value rounded off to 2 decimals.
 Hint: Use 'pi' value from the 'math' module.
 - Defind doctests for 'circumference' which creates a circle 'c1' with raidus 2.5, and checks if the circumference of the circle is 15.71.


"""

import math


# Define the class 'Circle' and its methods with proper doctests:
class Circle:

    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        __init__ method.
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius

    def area(self):
        # Define doctests for area method:
        """
        area method
        >>> c1 = Circle(2.5)
        >>> c1.area()
        19.63
        """
        # Define area functionality:
        return round(math.pi * self.radius**2, 2)

    def circumference(self):
        # Define doctests for circumference method:
        """
        circumference method
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define circumference functionality:
        return round(2 * math.pi * self.radius, 2)
