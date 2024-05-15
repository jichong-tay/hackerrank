"""
2. Problem 1 - Unit Testing using unittest in Python

Complete the definition of class 'Circle' with the following specifications:
-Define a class method '__init__' which initializes a circle with attribute 'radius', having the following restrictions:
    - 'radius' must be a numeric value. If not, raise TypeError with error message "radius must be a number".
    - 'radius' must be between 0 and 1000 (inclusive on both sides). If not, raise ValueError with errror message "radius must be between 0 and 1000 inclusive".
-Define a class method 'area' which computes the area of a circle, and returns the value rounded off to 2 decimals.
 Hint: Use 'pi' value from 'math' module.
-Define the class method 'circumference' which computes the circumference of a circle, and returns the value rounded off to 2 decimals.
  Hint: Use 'pi' value from 'math' module.

Complete the definition  of class 'TestingCircleCreation; which test the behaviour of the '__init__' method as specified:
 -Define test method of class 'test_creating_circle_with_numeric_radius' which creates a circle with radius 2.5, and check if its radius matches the value 2.5.
 -Define test method 'test_creating_circle_with_negative_radius' which checks if a ValueError exception is raised with the error message "radius must be between 0 and 1000 inclusive" while creating a circle of radius -2.5.
 -Define test method 'test_creating_circle_with_greaterthan_radius' which checks if a ValueError exception is raised with the error message "radius must be between 0 and 1000 inclusive" while creating a circle of radius 1000.1.
 -Defind test method 'test_creating_circle_with_nonnumeric_radius' which checks if a TypeError exception is raised with the error message "radius must be a number" while creating a circle of radius 'hello'.


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


class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if
        # the value of c1.radius is equal to 2.5 or not.
        c1 = Circle(2.5)
        self.assertEqual(c1.radius, 2.5)

    def test_creating_circle_with_negative_radius(self):
        # Define a circle 'c' with radius -2.5, and check
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError) as e:
            c = Circle(-2.5)
            self.assertEqual(
                str(e.exception), "radius must be between 0 and 1000 inclusive"
            )

    def test_creating_circle_with_greaterthan_radius(self):
        # Define a circle 'c' with radius 1000.1, and check
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError) as e:
            c = Circle(1000.1)
            self.assertEqual(
                str(e.exception), "radius must be between 0 and 1000 inclusive"
            )

    def test_creating_circle_with_nonnumeric_radius(self):
        # Define a circle 'c' with radius 'hello' and check
        # if it raises a TypeError with the message
        # "radius must be a number".
        with self.assertRaises(TypeError) as e:
            c = Circle("hello")
            self.assertEqual(str(e.exception), "radius must be a number")


if __name__ == "__main__":

    unittest.main()
