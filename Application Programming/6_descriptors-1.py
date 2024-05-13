"""
1. Descriptors

1. Define the class Temperature where the initializer method accepts temperature in Fahrenheit units.
2. Define a Descriptor class Celsius with two methods:
    a. __get__ - Returns temperature in Celsius units.
    b. __set__ - Allows to change temperature to a new value in celsius units.
3. Create an attribute celsius for the Temperature class and try the following code:

t1 = Temperature(32)
t1.celsius = 0

Hint: The implementation is provided in the validations. Test against the ustom input to validate the output.

4. Use the Test against custom input box to output the result for debugging.

5. Provide 2 numbers in 2 lines(refer test case samples) and click Run Code to display the output/error.
  -1st input - Fahrenheit value.
  -2nd input - Celsius value.
  Note: In both cases, Fahrenheit and Celsius is calculated.
  
Test Case 1:
Input:
32
0
Expected Output:
(32,0.0)
(32.0,0.0)

Test Case 2:
Input:
212
100
Expected Output:
(212, 100.0)
(212.0, 100.0)

"""


# Add Celsius class implementation below.
class Celsius:
    def __get__(self, instance, owner):
        return (instance.fahrenheit - 32) * 5.0 / 9.0

    def __set__(self, instance, value):
        instance.fahrenheit = value * 9.0 / 5.0 + 32


# Add temperature class implementation below.
class Temperature:
    celsius = Celsius()  # Attach the Celsius descriptor to the Temperature class

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit


t1 = Temperature(32)
print(t1.fahrenheit, t1.celsius)
t1.celsius = 0
print(t1.fahrenheit, t1.celsius)


##alternative
# # Add Celsius class implementation below.


# # Add temperature class implementation below.
# class Temperature:

#     def __init__(self, fahrenheit):
#         self.fahrenheit = fahrenheit

#     @property
#     def celsius(self):
#         return getattr(self, "_celsius", 0.0)

#     @celsius.setter
#     def celsius(self, value):
#         if hasattr(self, "_celsius"):
#             self.value = value
#         if hasattr(self, "_fahrenheit"):
#             value = (value - 32.0) * 5.0 / 9.0
#             self._celsius = value


# t1 = Temperature(32)
# print(t1.fahrenheit, t1.celsius)
# t1.celsius = 0
# print(t1.fahrenheit, t1.celsius)
