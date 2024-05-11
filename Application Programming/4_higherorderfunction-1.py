"""
1. Higher order functions and closures - 1
- Define a function named dectector with one parameter element, which returns an inner function isIn.
- isIn accepts parameter sequence, and returns True or False after checking the presence of element in sqeuence.
- Create two closure functions detect30 and detect45 using detector.
 - Pass 30 to detect30, and 45 to detect45 for implementation.

Test Case 1:
Input
2,30,45,6
Expected Output
True
True

Test Case 2:
Input
8,30,4,6
Expected Output
True
False

Test Case 3:
Input
8,3,4,6,9,4,5,0,1,445,300
Expected Output
False
False

"""

# Complete the function below.


# Write detecter implementation
def detector(element):
    # Write isIn implementation
    def isIn(sequence):
        return element in sequence

    return isIn


# Write closure function implementation for detect30 and detect45

detect30 = detector(30)
detect45 = detector(45)
