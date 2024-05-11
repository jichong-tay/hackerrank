"""
2. Python Files - 2

1. Read the multi-line string zenPython as data from a file and create a file object fp.
Hint: Use io.StringIO.
2. Return the f instance created.
3. Use the Test aginst custom input to output the result for debugging.
4. Use print(res) to display the output.

"""

import io


def main():
    zenPython = """
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """

    # Create fp implementation, check for fp instance and return status

    # Create a file object fp

    fp = io.StringIO(zenPython)
    if isinstance(fp, io.StringIO):
        return fp
