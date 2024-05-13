"""
4. Decorators - 4

1. Define a decorator function italic_tag which adds italic HTML tags<i> ... </i> to the vlue of anotehr function.
2.Use the Test against custom input box to output the result for debugging.
3. Provide a string (refer test case samples) to display the output/error.

Test Case 1
Input:
Hi Decorator
Expected Output:
<i>Hi Decorator</i>

"""

import sys
import os


def bold_tag(func):

    def inner(*args, **kwdargs):
        return "<b>" + func(*args, **kwdargs) + "</b>"

    return inner


# Implement italic_tag below
def italic_tag(func):

    def inner(*args, **kwdargs):
        return "<i>" + func(*args, **kwdargs) + "</i>"

    return inner


@italic_tag
def say(msg):
    return msg
