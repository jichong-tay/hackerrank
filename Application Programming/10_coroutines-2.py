"""
2. give a Try: Define a Decorator for Coroutine
- Define a Decorator 'coroutine_decorator', which can decorate any coroutine function.
- The decorator must create the coroutine, call 'next' on it and return the coroutine that is ready for accepting any input.
For eg.

@coroutine_decorator
def linear_equation(a, b):
...

e1 = linear_equation(3, 4) #e1 should able to accept input without calling 'next' on it.
e1.send(6)

"""


# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwargs):
        c = coroutine_func(*args, **kwargs)
        next(c)
        return c

    return wrapper


# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print(f"Expression, {a}*x^2 + {b}, with x being {x} equals {a*(x**2)+b}")


t = linear_equation(3, 4)
t.send(6)
