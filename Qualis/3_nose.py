"""
1. Python Qualis - Nose Testing Framework

Python Qualis - Nose Testing Framework

In this scenario, you will be writing test cases using nose testing framework.

Steps to do:
-Open the test module mytest/test_circle.py and follow instructions below.
-Import the Cirle class from the circle module using the expression from proj.circle import Circle.
-Import assert_raises from nose.tools using the expression from nose.tools import assert_raises.
-Define a nose test class 'TestingCircleCreation':
  -Define a nose test method 'test_creating_circle with_numeric_radius', which creates a circle with radius 2.5, and check if its radius value is 2.5 using eq_() method.
  -Define a nose test method 'test_creating_circle with_negative_radius', which checks if the ValueError exception is raised with the error message "radius must be between 0 and 1000 inclusive" using eq_() method, while creating a circle of radius -2.5.
  (Hint: Use assert_raises() and with).
  -Define a nose test method 'test_creating_circle_with_greater_radius', which checks if the ValueError execption is raised with the error message "radius must be between 0 and 1000 inclusive" using eq_() method, while creating a circle of radius 1001.
  (Hint: Use assert_raises() and with).
  -Define a nose test method 'testing_creating_circle_with_no_nnumeric_radius', which checks if the TypeError exception is raised with the error message "radius must be a number" using eq_() method, while creating a circle of radius 'hello'.
  (Hint: Use assert_raises() and with).
-Define a nose test class 'TestCircleArea':
  -Define a nose test method 'test_circlearea_with_random_numeric_radius', which creates a circle 'c1' with radius 2.5, and check if its computed area is 19.63 using eq_() method.
  -Define a nose test method 'test_circlearea_with_min_radius', which creates a circle 'c2' with radius 0, and check if its computed area is 0 using eq_() method.
  -Define a nose test method 'test_circlearea_with_max_radius', which creates a circle 'c3' with radius 1000, and check if its computed area is 3141592.65 using eq_() method.
-Define a nose test class 'TestCircleCircumference':
  -Define a nose test method 'test_circlecircum_with_random_numeric_radius', which creates a circle 'c1' with radius 2.5, and check if its computed circumference is 15.71 using eq_() method.
  -Define a nose test method 'test_circlecircum_with_min_radius', which creates a circle 'c2' with radius 0, and check if its computed circumference is 0 using eq_() method.
  -Define a nose test method 'test_circlecircum_with_max_radius', which creates a circle 'c3' with radius 1000, and check if its computed circumference is 6283.19 using eq_() method.

Note
-Nose packages are available in the environment.
-If additional package is neeed, use the following command to install any package in the environment.

pip3 install --user <package-name>

Carry out the following taskes in order.
Task 1: Open Online IDE
-Once the test has been opened, click Online IDE option to perform the challenge in an online environment.
Taske 2: Setup the Environment
-Once the online IDE has been opened, click 'Run-->Install' to install the required dependencies.
Task 3: Perform Handson using python script.
-Open python script file(mytest/test_circle.py) and follow the instructions given in that file.
-Once you done with test case. Click 'Run --> Run' to run all the tests in test module test_circle.py.
Important Note
read every instruction properly given in the test_circle.py file.
Task 4: Testing the Solutions
-After completing the solution, test it by clicking the 'Run Tests' button to perform the preliminary validations.
-The number of test cases that have passed and failed will be displayed.
Note: The results of the preliminary validation does not impact the final scoring. In-depth scoring will be done at a later stage.


"""
