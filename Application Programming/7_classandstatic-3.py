"""
3. Class and Static Methods-3

1. Define a static method getPi inside Circle which returns the value 3.14.
  Hint: Use staticmethod decorator.

2. Redefine the area method such that it uses the getPi static method in it.

3. Try accessing the static method by using an object and the class.

4. Check the main/til section for output handling (read-only).

5. Use the Test against custom input box to output the result for debugging.

6. Provide float values seperated by comma (refer test case samples) to display the output/error.
  The output should return a key-value pair of the circle numbe and its corresponding area.
  
Test Case 1:
Input:
1,2,3
Expected Output:
['1:3.14','2:12.56','3:28.26']

Test Case 2:
Input:
2.0,3.0,4,5
Expected Output:
['1 : 12.56', '2 : 28.26', '3 : 50.24', '4 : 78.5']
"""


# Add circle class implementation here
class Circle:
    no_of_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.no_of_circles += 1

    @classmethod
    def getCircleCount(self):
        return Circle.no_of_circles

    @staticmethod
    def getPi():
        return 3.14

    def area(self):
        return round(self.getPi() * self.radius * self.radius, 2)
