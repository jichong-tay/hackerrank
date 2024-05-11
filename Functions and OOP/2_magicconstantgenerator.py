"""
Magic Constant Generator

Magic Constant 'M'

A magic square is an arrangement of numbers in a square, where the sum of the numbers in each row, each column, and each diagonal will be equal to the same number.

For example, if the number of rows and columns in a magic square is "n", then it will have n*n numbers.

You can create a magic square of any number 'n' except when n= 2.
The constant which is the sum of every row, column, and diagonal is called the magic constant, M.
Every magic square will have this constant M, which is based on the value of n.
The smallest 'nontrivial' case, which is a 3x3 magic square, has a magic constant of 15.

If n=3, then M=15.
If n=4, then M=34, and so on.

The magic constants, are from n=3,4,5,6,7,8:
... 15, 34, 65, 111, 175, 260

Write the function definition for the generator named 'generator_Magic', which takes a single parameter 'n1', an integer.
1. Define the above Generator sucht that it should yield the Magic constant(s) for the values starting from 3 to 'n1'.

Note
Printing the output will be taken care of during testing, so you need not print the Magic constants yielded by generator 'generatr_Magic' and it's Type.


"""

import unittest


def generator_Magic(n1):
    for n in range(3, n1 + 1):
        M = n * (n * n + 1) // 2
        yield M


class TestMagicGenerator(unittest.TestCase):
    def test_generator_Magic(self):
        n = 8
        expected_output = [15, 34, 65, 111, 175, 260]

        # Capture the output of the generator
        output_gen = generator_Magic(n)
        output_list = list(output_gen)

        # Check if the generated list matches the expected output
        self.assertEqual(output_list, expected_output)

        # Check the type of the generator
        self.assertEqual(type(output_gen), type(generator_Magic(n)))


if __name__ == "__main__":
    unittest.main()
