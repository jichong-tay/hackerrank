"""
3. Decorators - 3

1. Define a decorator function bold_tag which adds bold HTML tags<b> ... </b> to the vlue of anotehr function.
2.Use the Test against custom input box to output the result for debugging.
3. Provide a string (refer test case samples) to display the output/error.

Test Case 1
Input:
Decorator exercise
Expected Output:
<b>Decorator exercise</b>

Test Case 2
Input:
12367899
Expected Output:
<b>12367899</b>
"""

import sys
import os


# Define and implement bold_tag
def bold_tag(func):
    def inner(*args, **kwdargs):
        return "<b>" + str(func(*args, **kwdargs)) + "</b>"

    return inner


@bold_tag
def say(msg):
    return msg
