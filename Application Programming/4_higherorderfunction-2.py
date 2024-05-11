"""
2. Higher order functions and closures - 2
- Define a function factory, with a variable n initialized to zero, and two inner functions current and counter.
 - current must return the current value of n.
 - counter must increment the value of n by one.
 
 Hint: Check the closure functions f_current and f_counter, and return the currrent and counter functions from factory accordingly.
 
 Test Case 1
 Input
 2
 Expected Output
 2
 3
 
 Test Case 2
 Input
 Expected Output
89
90

"""

# Add the factory function implementation here


def factory(n):

    def current():
        return n

    def counter():
        nonlocal n
        n += 1
        return n

    return current, counter


f_current, f_counter = factory(int(input()))
