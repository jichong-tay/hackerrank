"""
For Loop
This Exception Handling scenario deals with the StopIteration case that arises during the Internal execution of a For Loop.

Write the function definition for the function 'FORLoop', which takes no parameter, as follows:
1. Get an Integer input from the user, say 'n'.
2. Create a LIST of 'n' integers from the user say 'l1'.
3. Print the list 'l1'.
4. Create an Iterator for the list 'l1' and Assign it to the variable 'iter1'.
5. Using the next() function and the created iterator 'iter1', Print the elements of the list.
Return the iterator variable 'iter1'.


"""


def FORLoop():

    # 1. Get an Integer input from the user, say 'n'.
    n = int(input(""))
    # 2. Create a LIST of 'n' integers from the user say 'l1'.
    l1 = []
    for _ in range(n):
        element = int(input(""))
        l1.append(element)

    # 3. Print the list 'l1'.
    print(l1)

    # 4. Create an Iterator for the list 'l1' and Assign it to the variable 'iter1'.
    iter1 = iter(l1)

    # 5. Using the next() function and the created iterator 'iter1', Print the elements of the list.
    while True:
        try:
            print(next(iter1))
        except StopIteration:
            break

    # 6. Return the iterator variable 'iter1'.
    return iter1
