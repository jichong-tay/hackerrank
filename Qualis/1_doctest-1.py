"""
1. Problem 1 - Unit Testing using doctest in Python

A palindrome is number or other sequence of characters which is the same when read backward or forward.

Define the function 'isPalindrome' and write doctests which test the functionality of 'isPalindrome' as specified in the following:

Task to be peformed

-Complete the function definition of 'isPalindrome' which checks if a given positive integer is a palindrome or not, and returns True and False correspondingly.

-Write a doctest which checks if the function call 'isPalindrome(121)' returns True.

-Write a doctest which checks if teh function call 'isPalindrome(344)' returns False.

-Write a doctest which checks if the function call 'isPalindrome(-121)' raise a 'ValueError' with an error messages: "x must be a postive integer".

Write a doctest which checks if the function call 'isPalindrome("hello") raises a 'TypeError' with an error message: "x must be an integer".



"""


# Complete the following isPalindrome function:
def isPalindrome(x):
    # Write the doctests:
    """
    Checks if a given positive integer is a palindrome or not.
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
     Traceback (most recent call last):
     ...
     ValueError: x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    ...
    TypeError: x must be an integer
    """
    # Write the functionality:
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be a positive integer")
    return str(x) == str(x)[::-1]
