"""
1. Write a text to a file using "with"

Define a function "writeTo" with two parameters, "filename" and "text".
"text" takes any input string, and "filename" refers to the name of the file which the input text is written.

Hint: Use "with" statement to open the file in which the input text is written.


"""


def writeTo(filename, input_text):
    with open(filename, "w") as file:
        file.write(input_text)
