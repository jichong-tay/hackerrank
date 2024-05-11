"""
Addition and Substraction of Complex Numbers

1. Define the class 'comp' that represents the Real and Imaginary parts of a complex number.
For example, for the complex number "2+3i", 2 is the real part, and 3 is the imaginary part.

Hint:
Define the initializer method, __init__, that takes 2 values and assigns them to the above 2 attributes, respectively.

2. Define a method 'add' inside the class 'comp', which determines the sum of two complex numbers and Print the sum as
"Sum of the two Complex numbers : 35+47i"

3. Define a method 'sub' inside the class 'comp', which determines the difference of two complex numbers and Print the difference as "Subtraction of the two Complex numbers : -33-43i"
Note: Substract the second complex number from the first complex number.

Sample Output
Sum of the two Complex numbers :4+6i
Subtraction of the two Complex numbers :-2-2i
"""

import unittest
from unittest.mock import patch
from io import StringIO


class comp:
    def __init__(self, real, imgainary):
        self.real = real
        self.imgainary = imgainary

    def add(self, compInstance):
        sum_real = self.real + compInstance.real
        sum_imaginary = self.imgainary + compInstance.imgainary
        print(f"Sum of the two Complex numbers :{sum_real}{sum_imaginary:+}i")

    def sub(self, compInstance):
        sum_real = self.real - compInstance.real
        sum_imaginary = self.imgainary - compInstance.imgainary
        print(f"Subtraction of the two Complex numbers :{sum_real}{sum_imaginary:+}i")


class TestcompClass(unittest.TestCase):
    "Test for movieClass function"

    def test_comp_class(self):
        comp1 = comp(4, 5)
        comp2 = comp(4, 5)

        expected_output_add = "Sum of the two Complex numbers :8+10i"
        expected_output_sub = "Subtraction of the two Complex numbers :0+0i"

        # Redirect standard output to a StringIO object
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            comp1.add(comp2)
            comp_add = mock_stdout.getvalue()

        self.assertEqual(expected_output_add, comp_add.strip())

        # Redirect standard output to a StringIO object
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            comp2.sub(comp2)
            comp_sub = mock_stdout.getvalue()
        self.assertEqual(expected_output_sub, comp_sub.strip())


if __name__ == "__main__":
    unittest.main()
