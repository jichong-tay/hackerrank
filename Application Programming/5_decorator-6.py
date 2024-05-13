"""
6. Decorators - 6

1. Chain two decorators with the greet function as shown in the following code.
2. Run the code and verify if the HTML tags have been added on both sides of the string.

  @bold_tag
  @italic_tag
  def greet():
      return input()

3. Use the Test against custom input box to output the result for debugging.
4. Provide a string (refer test case samples) to display the output/error.

Input:
Python is a programming language
Expected Output:
<i><b>Python is a programming language</b></i>


"""


def bold_tag(func):

    def inner(*args, **kwdargs):
        return "<b>" + func(*args, **kwdargs) + "</b>"

    return inner


def italic_tag(func):

    def inner(*args, **kwdargs):
        return "<i>" + func(*args, **kwdargs) + "</i>"

    return inner


# Add greet() implementation here
@italic_tag
@bold_tag
def greet():
    return input()


print(greet("Hello World! Welcome to Python Programming Language."))
