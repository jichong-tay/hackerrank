"""
Python - Collection

Import the collections module.
Definde a function called 'collectionfunc' which takes the following 6 parameters:
 - The first parameer, 'text', is a string of sentence.
 - The second parameter, 'dictionary1' is a dictioary.
 - The third parameter, 'key1' is a list of keys.
 - The fourth parameter, 'val1' is a list of values.
 - The fifth paramter, 'deduct', is a dictionary.
 - The sixth parameter, 'list1' is a list of keys.

The function definition code stub is given in the editor.
Generate print statements based on the followin conditions:

1. Create a dictionary with the count of words in text1.
  -The words must be the key, and the count must be the value.
  -Print the dictionary sorted by key.
  
2. Create a Counter object using dictionary1.
  -Substract the values of the counter object from the respective values specified in the deduct dictionary.
  -Convert the counter object into a dictionary and print the same.

3. Create an ordered dictionary with key1 values as key and val1 values as value.
  -Delete the key in the ordered dictionary using the second value from key1.
  -Reinsert the second values from key1 as key and val1 as value into the ordered dictionary.
  -Convert the ordered dictionary into a normal dictionary and print the same.
  
4. Create a default dictionary that has 'even' and 'odd' keys.
  -The keys must have the list as their respective values.
  -Extract the even and odd numbers from list1.
  -Print the default dictionary as a normal dictionary.

text1 = "how many times does each word show up in this sentence word times each each word"
dictionary1 = {1: 3, 2: 4, 12: 2, 14: 6}
key1 = ['a','b','c']
val1 = [1,2,3]
deduct = {1: 0, 14:2}
list1 = [1,3,5,7,9,10]

Expected Output
{'does': 1, 'each': 3, 'how': 1, 'in': 1, 'many': 1, 'sentence': 1, 'show': 1, 'this': 1, 'times': 2, 'up': 1, 'word': 3}
{'1': 3, '2': 4, '12': 2, '14': 4}
{'a': 1, 'c': 3, 'b': 2}
{'odd': [1, 3, 5, 7, 9], 'even': [10]}



"""

import collections


def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):

    # 1. Create a dictionary with the count of words in text1.
    text1list = text1.split()
    text1dict = {}
    for i in text1list:
        text1dict[i] = text1list.count(i)
    text1dict1 = dict(sorted(text1dict.items()))
    print(text1dict1)

    # 2. Create a Counter object using dictionary1.
    counter1 = collections.Counter(dictionary1)
    counter1.subtract(deduct)
    print(dict(counter1))

    # 3. Create an ordered dictionary with key1 values as key and val1 values as value.
    #   -Delete the key in the ordered dictionary using the second value from key1.
    #   -Reinsert the second values from key1 as key and val1 as value into the ordered dictionary.
    #   -Convert the ordered dictionary into a normal dictionary and print the same.
    ordereddict1 = collections.OrderedDict(zip(key1, val1))
    del ordereddict1[key1[1]]
    ordereddict1[key1[1]] = val1[1]
    print(dict(ordereddict1))

    # 4. Create a default dictionary that has 'even' and 'odd' keys.
    # -The keys must have the list as their respective values.
    # -Extract the even and odd numbers from list1.
    # -Print the default dictionary as a normal dictionary.
    defaultdict1 = collections.defaultdict(list)
    for num in list1:
        if num % 2 == 0:
            defaultdict1["even"].append(num)
        else:
            defaultdict1["odd"].append(num)
    print(dict(defaultdict1))


# Sample Input
text1 = (
    "how many times does each word show up in this sentence word times each each word"
)
dictionary1 = {1: 3, 2: 4, 12: 2, 14: 6}
key1 = ["a", "b", "c"]
val1 = [1, 2, 3]
deduct = {1: 0, 14: 2}
list1 = [1, 3, 5, 7, 9, 10]

collectionfunc(text1, dictionary1, key1, val1, deduct, list1)
