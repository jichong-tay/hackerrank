"""
1. Match Pattern and Replace

1. Write a function subst which replaces a pattern matching portion with another value.
2. Using subst, replace all the word ROAD with RD in the following:

    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            

Expected Output

"""

import io
import re


def subst(pattern, replace_str, string):
    # susbstitute pattern and return it
    return re.sub(pattern, replace_str, string)


def main():
    addr = [
        "100 NORTH MAIN ROAD",
        "100 BROAD ROAD APT.",
        "SAROJINI DEVI ROAD",
        "BROAD AVENUE ROAD",
    ]

    # Create pattern Implementation here
    pattern = r"\bROAD\b"

    # Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address = [subst(pattern, "RD.", address) for address in addr]
    print(new_address)

    return new_address


main()
