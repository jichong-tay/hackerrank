"""
Inheritance - Parent and Children Shares

This hands-on is about dividing a family's total assets within the family memebers based on a percentge.
1. Parents will always inherit 50% of the fmaily's total asset worth.
2. The son will inherit a percentage of the family's total's asset worth indicated by the input value 'Percentage_for_son'.
3. The daughter will inherit a percentage of the family's total's asset worth indicated by the input value 'Percentage_for_daughter'.

The definition for the parnet class 'parent' will be already given in the coding section.

1. Define a class 'son' derived from the clas 'parent'.
-inherit the init function from the parnet class and add a variable 'Percentage_for_son', which indicates the percentage of the inheritance he will get form the family's total asset worth.
-Defind a method 'son_display', which will Print the share of the son rounded off to 2 decimal places, for example, "Share of Son is 2.0 Million."

2. Define a class 'daughter' derived from the clas 'parent'.
-inherit the init function from the parnet class and add a variable 'Percentage_for_daugher', which indicates the percentage of the inheritance he will get form the family's total asset worth.
-Defind a method 'daugher_display', which will Print the share of the daughter rounded off to 2 decimal places, for example, "Share of Daughter is 8.0 Million."

Hint: use the round() function.

Note
The output should always be expressed in the unit "Million", as mentioned above.

Sample Output
Share of Son is 2.4 Million.
Total Asset Worth is 10 Million.
Share of Parents is 5.0 Million.
Share of Daughter is 2.6 Million.
Total Asset Worth is 10 Million.
Share of Parents is 5.0 Million.
True
True
False
False


"""

import unittest
from unittest.mock import patch
from io import StringIO


import math
import os
import random
import re
import sys


class parent:
    def __init__(self, total_asset):
        self.total_asset = total_asset

    def display(self):
        "Display the total asset worth and the share of the parents."
        print("Total Asset Worth is " + str(self.total_asset) + " Million.")
        print(
            "Share of Parents is " + str(round(self.total_asset / 2, 2)) + " Million."
        )


class son(parent):
    "Son class inheriting from parent class."

    def __init__(self, total_asset, Percentage_for_son):
        parent.__init__(self, total_asset)
        self.total_asset = total_asset
        self.Percentage_for_son = Percentage_for_son

    def son_display(self):
        "Display the share of the son."
        share = round(self.total_asset * (self.Percentage_for_son / 100), 2)
        print(f"Share of Son is {share} Million.")


class daughter(parent):
    "Daughter class inheriting from parent class."

    def __init__(self, total_asset, Percentage_for_daughter):
        parent.__init__(self, total_asset)
        self.total_asset = total_asset
        self.Percentage_for_daughter = Percentage_for_daughter

    def daughter_display(self):
        share = round(self.total_asset * (self.Percentage_for_daughter / 100), 2)
        print(f"Share of Daughter is {share} Million.")


class TestClass(unittest.TestCase):
    "Test for parent and children shares"

    def testclass(self):
        t = 10
        sp = 24
        dp = 26

        parent1 = parent(t)
        son1 = son(t, sp)
        daughter1 = daughter(t, dp)

        expected_output_son1 = "Share of Son is 2.4 Million."
        expected_output_son2 = (
            "Total Asset Worth is 10 Million.\nShare of Parents is 5.0 Million."
        )

        expected_output_daughter1 = "Share of Daughter is 2.6 Million."
        expected_output_daughter2 = (
            "Total Asset Worth is 10 Million.\nShare of Parents is 5.0 Million."
        )

        # Redirect standard output to a StringIO object
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            son1.son_display()
            output1 = mock_stdout.getvalue()

        self.assertEqual(output1.strip(), expected_output_son1)

        # Redirect standard output to a StringIO objectssssss
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            son1.display()
            output2 = mock_stdout.getvalue()

        self.assertEqual(output2.strip(), expected_output_son2)

        # Redirect standard output to a StringIO object
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            daughter1.daughter_display()
            output1 = mock_stdout.getvalue()

        self.assertEqual(output1.strip(), expected_output_daughter1)

        # Redirect standard output to a StringIO objectssssss
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            daughter1.display()
            output2 = mock_stdout.getvalue()

        self.assertEqual(output2.strip(), expected_output_daughter2)


if __name__ == "__main__":
    unittest.main()
