"""
Exception Handling #1
Write the function defintion for function "Handle_Exc1", that takes no parameter and will handle the 'ValueError' exception.

Write a script that reads two integers, say a and b, from STDIN, and:
1. Raise ValueError exception if a is greater than '150' or if b is less than '100' and Print a Message.
The message to user must be "Input integers value out of range."

ELSE IF
2. Raise ValueError execption if their sum is greater than '400' and Print a Message.
The message to the user must be "Their sum is out of range".

3. If none of the above Exception happens, then Print the Message "All in range."

"""


def Handle_Exc1():
    input_a = int(input(""))
    input_b = int(input(""))

    try:
        if input_a > 150 or input_b < 100:
            raise ValueError("Input integers value out of range.")
        elif input_a + input_b > 400:
            raise ValueError("Their sum is out of range")
    except ValueError as e:
        print(e)
    else:
        print("All in range")
