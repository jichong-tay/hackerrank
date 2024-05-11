"""
4. Python Files - 4
1. Remove the new line and unwanted characters at the end of each line in the list zenlines.
Hint: Use the strip method of strings and list comprehenisons.
2. Return the output
3. Use the Test against custom input box to output the result for debugging.
4. Use print(res) to display the output.

Expected Output
['', 'The Zen of Python, by Tim Peters', '', 'Beautiful is better than ugly.', 'Explicit is better than implicit.', 'Simple is better than complex.', 'Complex is better than complicated.', 'Flat is better than nested.', 'Sparse is better than dense.', 'Readability counts.', "Special cases aren't special enough to break the rules.", 'Although practicality beats purity.', 'Errors should never pass silently.', 'Unless explicitly silenced.', 'In the face of ambiguity, refuse the temptation to guess.', 'There should be one-- and preferably only one --obvious way to do it.', "Although that way may not be obvious at first unless you're Dutch.", 'Now is better than never.', 'Although never is often better than *right* now.', "If the implementation is hard to explain, it's a bad idea.", 'If the implementation is easy to explain, it may be a good idea.', "Namespaces are one honking great idea -- let's do more of those!", '']

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
    zenlines = fp.readlines()
    output = [lines.strip() for lines in zenlines]
    print(output)
    return output


main()
