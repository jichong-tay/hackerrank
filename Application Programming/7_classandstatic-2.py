"""
2. Class and Static Methods-2

1. Define a class method getCircleCount inside Circle which returns the number of circle objects created.
2. Try accessing the class method using an object and the class.
3. To test the number of circles created and the area of each circle, provdie the radius of each circle in the input.
4. Output the total count of circles.
5. Check the main/tail section for output handling (read-only).
6. Use the Test against custom input box to output the result for debugging.
7. Provide float values seperated by comma (refer test case samples) to display the output/error.
    The outputs should be split into 2 lines:
      - The 1st output should return a key-value pair of the circle number and it's corresponding area.
      - The 2nd output should return the number of circles created or the number of inputs provided.

  
Test Case 1:
Input:
1,2,3
Expected Output:
['1:3.14','2:12.56','3:28.26']
3

Test Case 2:
Input:
2.0,3.0,4,5
Expected Output:
['1 : 12.56', '2 : 28.26', '3 : 50.24', '4 : 78.5']
4
"""


# Add Circle class implementation here
class Circle:
    no_of_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles += 1

    @classmethod
    def getCircleCount(self):
        return Circle.no_of_circles

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)
