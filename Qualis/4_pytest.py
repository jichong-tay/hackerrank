"""
1. Python Qualis - Pytest Testing Framework

Python Qualis - Pytest Testing Framework

In this scenario, you will be writing test cases using pytest testing framework.

Steps to do:
-Open the test module mytest/test_inventory.py and follow instructions below.
-Import MobileInventory class and InsufficientException from the inventory module using the expression from proj.inventory import MobileInventory, InsufficientException.
-Import pytest using the expression import pytest.
-Use assert statement for assert, and to check. Ex: assert 1 == 1.

-Define a pytest test class **'TestingInventoryCreation'**
  -Define a pytest test method **'test_creating_empty_inventory'**, which creates an empty inventory and checks if its 'balance_inventory' is an empty dict using assert.
  -Define a pytest test method **'test_creating_specified_inventory'**, which checks if inventory instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}.
  -Define a pytest test method  **'test_creating_inventory_with_list'**, which checks if the  method raises a TypeError with the message "Input inventory must be a dictionary" when a list "['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']" is passed as input using assert.
  -Define a pytest test method **'test_creating_inventory_with_numeric_keys'**, which checks if the  method raises a ValueError with the message "Mobile model name must be a string" using assert, when the dict {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'} is passed as input.
  -Define a pytest test method **'test_creating_inventory_with_nonnumeric_values'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} is passed as input.
  -Define a pytest test method **'test_creating_inventory_with_negative_value'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} is passed as input.

-Define another pytest test class **'TestInventoryAddStock'**, which tests the behavior of the **'add_stock'** method, with the following tests
  -Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25} and assign it to class attribute **'inventory'**.
  -Define a pytest test method **'test_add_new_stock_as_dict'**, which adds the new stock {'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10} to the existing inventory, and update the **balance_inventory** attribute. Also, check if the updated **balance_inventory** equals {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10} using assert.
  -Define a pytest test method **'test_add_new_stock_as_list'**, which adds the new stock ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'] to the existing inventory, and which checks if the method raises a TypeError with the message "Input stock must be a dictionary" using assert.
  -Define a pytest test method **'test_add_new_stock_with_numeric_keys'**, which adds the new stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} to the existing inventory, and which checks if the method raises a ValueError with the message "Mobile model name must be a string" using assert.
  -Define a pytest test method **'test_add_new_stock_with_nonnumeric_values'**, which adds the new stock {'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
  -Define a pytest test method **'test_add_new_stock_with_float_values'**, which adds the new stock {'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.

-Define another pytest test class **'TestInventorySellStock'**, which tests the behavior of the **'sell_stock'** method, with the following tests
  -Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with the input {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1}, and assign it to the class attribute **'inventory'**.
  -Define a pytest test method **'test_sell_stock_as_dict'**, which sells the requested stock {'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1} from the existing inventory, and update the **balance_inventory** attribute. Also check if the updated **balance_inventory** equals {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0} using assert.
  -Define a pytest test method **'test_sell_stock_as_list'**, which tries selling the requested stock ['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'] from the existing inventory, and which checks if the method raises a TypeError with the message "Requested stock must be a dictionary" using assert.
  -Define a pytest test method **'test_sell_stock_with_numeric_keys'**, which tries selling the requested stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} from the existing inventory, and which checks if the method raises ValueError with the message "Mobile model name must be a string" using assert.
  -Define a pytest test method **'test_sell_stock_with_nonnumeric_values'**, which tries selling the requested stock {'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
  -Define a pytest test method **'test_sell_stock_with_float_values'**, which tries selling the requested stock {'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
  -Define a pytest test method **'test_sell_stock_of_Nonexisting_model'**, which tries selling the requested stock {'iPhone Model B':2, 'Xiaomi Model B':5} from the existing inventory, and which checks if the method raises an InsufficientException with the message "No Stock. New Model Request" using assert.
  -Define a pytest test method **'test_sell_stock_of_insufficient_stock'**, which tries selling the requested stock {'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15} from the existing inventory, and which checks if the method raises an InsufficientException with the message "Insufficient Stock" using asser

Note
 pytest packages are available in the environment.
-If additional package is neeed, use the following command to install any package in the environment.

pip3 install --user <package-name>

Carry out the following taskes in order.
Task 1: Open Online IDE
-Once the test has been opened, click Online IDE option to perform the challenge in an online environment.
Taske 2: Setup the Environment
-Once the online IDE has been opened, click 'Run-->Install' to install the required dependencies.
Task 3: Perform Handson using python script.
-Open python script file(mytest/test_inventory.py) and follow the instructions given in that file.
-Once you done with test case. Click 'Run --> Run' to run all the tests in test module test_inventory.py.
Important Note
read every instruction properly given in the test_inventory.py file.
Task 4: Testing the Solutions
-After completing the solution, test it by clicking the 'Run Tests' button to perform the preliminary validations.
-The number of test cases that have passed and failed will be displayed.
Note: The results of the preliminary validation does not impact the final scoring. In-depth scoring will be done at a later stage.
Task 5: Submit the Solution
-Once all the test cases are passed, you can click 'Submit' to submit your solution in Hackerrank.

"""
