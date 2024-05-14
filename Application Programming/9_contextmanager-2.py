"""
2. Archiving a file using "with"

 - Defind a function "archive" with two parameters, "zfile" and "filename."
 - ".zfile" refers to the "*.zip" file which the file "filename" is archived.
 
 - Define a function "writeTo" with two parameters, "filename" and "text". 
   "text" takes any input string, and "filename" refers to the name of the file which the input text is written.
Hint: Use "zipfile" module and "with".
"""

import zipfile


# Define 'writeTo' function below, such that
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename, "w") as file:
        file.write(input_text)


# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile, "w") as z:
        z.write(filename)
