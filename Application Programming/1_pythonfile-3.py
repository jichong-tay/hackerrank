"""
3. Python Files - 3

1. Read data from the file object fp as a list of strings and store it in the variable zenlines.
 Hint: Use the readlines() method.
2. Output the first 5 values of zenlines.
3. Use the Test against custom input box to output the result for debugging.
4. Use print(res) to display the output.

Expected Output
['\n', '    The Zen of Python, by Tim Peters\n', '    \n', '    Beautiful is better than ugly.\n', '    Explicit is better than implicit.\n']


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

    fp = io.StringIO(zenPython)

    # Add Implementation step here
    zenlines = fp.readlines()[:5]
    return zenlines


main()
