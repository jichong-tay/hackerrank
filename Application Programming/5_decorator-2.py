"""
2. Decorators - 2

1. Decorate the average funciton with the log decorator as shown in the following code.
2. Execute and verify if the log decorator is able to write the log to STDOUT.
      @log
      def average(n1,n2,n3):
          return (n1+n2+n3)/3
3. Use the Test against custom input box to output the result for debugging.
4. Provide integer/float values (refer test case samples) to display the output/error.

Test Case 1
Input:
3,8,16
Expected Output:
Accessed the function -'average' with arguments (3.0, 8.0, 16.0) {}
9.0

Tesst Case 2
Input:
2.5,5.5,7.5
Expected Output
Accessed the function -'average' with arguments (2.5, 5.5, 7.5) {}
5.166666666666667


"""


def log(func):
    def inner(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(
            func.__name__, args, kwdargs
        )
        return str_template + "\n" + str(func(*args, **kwdargs))

    return inner


# Add greet function definition here
@log
def average(n1, n2, n3):
    return (n1 + n2 + n3) / 3
