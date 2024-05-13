"""
1. Class and Static Methods-1

2. Define the following:
  - A class variable count which determines the number of circles created.
  - A method area that calculates the area of a circle.

3. The input should be comma-seperated-values, while the output should be the area for each value and the total number of circles created.

4. Check the main/tail section for output handling (read-only).

5. Use the Test against custom input box to output the result for debugging.

6. Provide float values separated by comma (refer test case samples) to display the output/error.
The outputs should be split into 2 lines:
  - The 1st output should return the area of the cirles for which inputs were provided.
  - The 2nd output should return the number of circles created for teh number of inputs provided.

  
Test Case 1:
Input:
1,2,3
Expected Output:
[3.14,12.56,28.26]
3

Test Case 2:
Input:
1.0,2.0,3.0
100
Expected Output:
[3.14,12.56,28.26]
3
"""


# Add Circle class implementation below
class Circle:
    no_of_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles += 1

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)
