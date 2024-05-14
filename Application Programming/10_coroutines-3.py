"""
3. Give a Try: Linking two coroutines
- Define 'linear_equation' and 'coroutine_decorator' functions as requested in previous test case.
- Define a coroutine function 'numberParser', which is capable of converting the passed input into an integer and also sends the integers to two linear equation coroutines - `equation1` and `equation2`

-'equation1' represents linear equation coroutine with a = 3 and b =4
-'equation2' represents linear equation coroutine with a = 2 and b =-2



"""


# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwargs):
        c = coroutine_func(*args, **kwargs)
        next(c)
        return c

    return wrapper


# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print(f"Expression, {a}*x^2 + {b}, with x being {x} equals {a*(x**2)+b}")


# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)


def main(x):
    n = numberParser()
    n.send(x)


main(6)
