"""
Python - Itertools

Import the itertools module.
Define a function called 'performIterator', which takes 1 parameter.

The first parameter is tuplevalues, which is a tuple.
-tuplevaues will always contain 4 tuples.

-Declare an empty main list.
-Declare another list. Use the cycle module in itertools to cycle through the first tuple and append the values to the list.
  -Repeat the cycle 4 times.
  -Convert the list into a tuple and append it to the main list.
  
-Use the repeat module in itertools to repeat the first value from the second tuple.
  -Create a tuple with the values and append it to the main list.
  -Hint: Use the length of the tuple to determine the number of repetitions required.
  
-Use the accumulate module in itertools to get the product after each iteration from the third tuple.
 -Create the tuple with the values and append it to the main list.
 
-Use the chain module in itertools to chain all the values of the tuple.
  -Create a tuple with the values and append it to the main list.
  
-Use the filterfalse module in intertools to extract the odd numbers from the chained tutple
  -Create a tuple with the values and append it to the main list.
  
Convert the main list into a tuple and return it


"""

import itertools


def performIterator(tuplevalues):
    mainlist = []

    # cycle
    cycle = itertools.cycle(tuplevalues[0])
    cyclelist = []
    for i, letter in enumerate(cycle):
        cyclelist.append(letter)
        if i == 3:
            break
    mainlist.append(tuple(cyclelist))

    # repeat
    repeat = tuple(itertools.repeat(tuplevalues[1][0], len(tuplevalues[1])))
    mainlist.append(repeat)

    # accumulate
    accumulate = tuple(itertools.accumulate(tuplevalues[2]))
    mainlist.append(accumulate)

    # chain
    mainlist.append(
        tuple(
            itertools.chain(
                tuplevalues[0], tuplevalues[1], tuplevalues[2], tuplevalues[3]
            )
        )
    )

    # filterfalse
    mainlist.append(
        tuple(
            itertools.filterfalse(lambda x: x % 2 == 0, (itertools.chain(*tuplevalues)))
        )
    )

    return tuple(mainlist)
