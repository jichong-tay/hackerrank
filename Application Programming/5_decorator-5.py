"""
5. Decorators - 5

1. Define a function greet which accepts a string and returns italic HTML tags.
2.Use the Test against custom input box to output the result for debugging.
3. Provide a string (refer test case samples) to display the output/error.

Test Case 1
Input:
Hello World! Welcome to Python Programming Language.

Expected Output:
<i>Hello World! Welcome to Python Programming Language.</i>

"""


def bold_tag(func):

    def inner(*args, **kwdargs):
        return "<b>" + func(*args, **kwdargs) + "</b>"

    return inner


def italic_tag(func):

    def inner(*args, **kwdargs):
        return "<i>" + func(*args, **kwdargs) + "</i>"

    return inner


# Add greet() function definition
@italic_tag
def greet():
    return input()


print(greet("Hello World! Welcome to Python Programming Language."))
