"""
1. Decorators - 1

1. Define a decorator function log which logs information about a function and the arguments passed to it.
2. Ensure the log message is written to STDOUT
3. Use the Test against custom input box to output the result for debugging.
4. Provide a text string (refer test case samples) to dispaly the output/error.

Test Case 1
Input:
hello world!
Expected Output:
Accessed the function -'greet' with arguments ('hello world!',) {}

Test Case 2
Input:
Python Rocks
Expected Output:
Accessed the function -'greet' with arguments ('Python Rocks',) {}

"""


# Add log function and inner function implementation here
def log(func):
    def wrapper(*args, **kwargs):
        val = f"Accessed the function -'{func.__name__}' with arguments {args} {kwargs}"
        return val

    return wrapper


@log
def greet(msg):
    "Greeting Message : " + msg


msg = "hello world!"

print(greet(msg))
