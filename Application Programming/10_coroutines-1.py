"""
1. Defining a Coroutine in Python
- Define a coroutine function 'linear_equation' which takes two arguments 'a' and 'b'.
- Any coroutine derived from 'linear_equation' should be capble of taking a number as input, and evaluating the expression 'a*(x**2)+b'.
- The coroutine after evaluating the expression should print the message 'Expression, 3*x^2 +4, with x being 6 equals 112'.

Hint: Use print() instead of 'return', to print out the output.
"""

# Define the coroutine function 'linear_equation' below.


def linear_equation(a, b):
    while True:
        x = yield
        print(f"Expression, {a}*x^2 + {b}, with x being {x} equals {a*(x**2)+b}")


t = linear_equation(3, 4)
next(t)
t.send(6)
