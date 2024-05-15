"""
3. Problem 3 - Unit Testing using unittest in Python

Complete the definition of class 'Circle' with the following specifications:
-Define a class method '__init__' which initializes a circle with attribute 'radius', having the following restrictions:
    - 'radius' must be a numeric value. If not, raise TypeError with error message "radius must be a number".
    - 'radius' must be between 0 and 1000 (inclusive on both sides). If not, raise ValueError with errror message "radius must be between 0 and 1000 inclusive".
-Define a class method 'area' which computes the area of a circle, and returns the value rounded off to 2 decimals.
 Hint: Use 'pi' value from 'math' module.
-Define the class method 'circumference' which computes the circumference of a circle, and returns the value rounded off to 2 decimals.
  Hint: Use 'pi' value from 'math' module.

Complete the defintion of class 'TestCircleCircumference' which tests the behavior of the 'circumference' method, as specified:
  -Define test method 'test_circlecircum_with_random_number_radius' which creates a circle 'c1' with radius 2.5, and checks if its computed circumference matches the value 15.71.
  -Define test method 'test_circlecircum_with_min_radius' which creates a circle 'c2' with radius 0, and checks if its computed circumference matches the value 0.
  -Define test method 'test_circlecircum_with_max_radius' which creates a circle 'c3' with radius 1000, and checks if its computed circumference matches the value 6283.19.

"""

import math
import unittest


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
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius < 0 or radius > 1000:
            raise ValueError("radius must be between 0 and 1000 inclusive")

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


class TestCircleCircumference(unittest.TestCase):

    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if
        # its circumference is 15.71.
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(), 15.71)

    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if
        # its circumference is 0.
        c2 = Circle(0)
        self.assertEqual(c2.circumference(), 0)

    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000, and check if
        # its circumference is 6283.19.
        c3 = Circle(1000)
        self.assertEqual(c3.circumference(), 6283.19)


if __name__ == "__main__":

    unittest.main()
