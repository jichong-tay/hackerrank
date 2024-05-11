"""
Polymorphism

1. Defind a class "rectangle" with two methods "display" and "area".
-Define the method "display" such that it will Print the message "This is a Rectangle" upon calling.
-Define the method "area" which takes 2 parameters "Lengh" and "Breath" and find the area of the rectangle and Print as "Area of Rectangle is 144".

2. Define a class "square" with two methods "display" and "area".
-Define the method "display" such that it will Print the message "This is a Square" upon calling.
-Define the method "area" which takes a single parameter "Side" and find the area of the square and Print as "Area of square is 169".

"""

import unittest
from unittest.mock import patch
from io import StringIO


import math
import os
import random
import re
import sys


class rectangle:
    def display(self):
        print("This is a Rectangle")

    def area(self, length, breadth):
        area_value = length * breadth
        print(f"Area of Rectangle is  {area_value}")


class square:
    def display(self):
        print("This is a Square")

    def area(self, side):
        area_value = side**2
        print(f"Area of square is  {area_value}")
