"""
Define a function called `stringmethod` that takes in 5 parameters: `para`, `special1`, `special2`, `list1`, `strfind`.

The first parameter is a para, which takes a string sentence.
The second parameter is a special1, which takes a string of special characters.
The third parameter is a special2, which takes a single string of special characters.
The fourth parameter is a list1, which takes a list of strings.
The fifth parameter is a strfind, which takes a string.

The function should do the following:
  1. remove all the special characters from para specified in special1 and save them in variable word1
  2. get the first 70 characters from word1, reverse the string, save it in variable rword2, print rword2
  3. remove all the wide spaces from rword2, join the characters using the special character specified in special2, print the joint string
  4. if every string from list1 is present in para, then format the print statement as follow: "Every string in {list1} are present in the paragraph" else "Every string in {list1} are not present in the paragraph"
  5. Split every word from word1, and print the first 20 words as a list
  6. calculate the less frequently used words whose count <3. and print the last 20 less frequently used words as a list
  7. print the last index in word1 where substring strfind is present
"""


def stringmethod(para, special1, special2, list1, strfind):

    # 1. remove special characters from para specified in special1 and save them in variable word1
    word1 = "".join(char for char in para if char not in special1)

    # 2. get the first 70 characters from word1, reverse the string, save it in variable rword2, print rword2
    rword2 = word1[:70][::-1]
    print(rword2)

    # 3. remove all the wide spaces from rword2, join the characters using the special character specified in special2, print the joint string
    rword2nospace = "".join(char for char in rword2 if char != " ")
    joinstring = special2.join(rword2nospace)
    print(joinstring)

    # 4. if every string from list1 is present in para, then format the print statement as follow: "Every string in {list1} are present in the paragraph" else "Every string in {list1} are not present in the paragraph"
    all_present = all(string in para for string in list1)
    if all_present:
        print(f"Every string in {list1} were present")
    else:
        print(f"Every string in {list1} were not present")
    # 5. Split every word from word1, and print the first 20 words as a list
    words = word1.split()
    print(words[:20])

    # 6. calculate the less frequently used words whose count <3. and print the last 20 less frequently used words as a list
    words = word1.split()
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    # Filter out words with a frequency less than 3
    less_frequent_words = [word for word, count in word_counts.items() if count < 3]
    print(less_frequent_words[-20:])

    # 7. Print the last index in word1 where substring strfind is present
    last_index = word1.rfind(strfind)
    print(last_index)


import unittest
from unittest.mock import patch
from io import StringIO


class TestStringMethod(unittest.TestCase):

    def test_stringmethod(self):
        # self.maxDiff = None
        para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapien, eget aliquam turpis urna at quam. Sed a&eros vel@ ante vestibulum vulputate. Suspendisse vitae vulputate velit. Suspendisse! ligula nisl, semper ut sodales et, ultricies porttitor felis. Nunc ac mattis erat, aliquet pretium risus. Nullam quis congue lacus, et mollis nulla. Nunc laoreet in nisi sit amet facili*sis. Cras rutrum justo ut eros mollis volutpat. Sed quis mi nunc. Nunc sed bibendum nibh, quis bibendum tortor."
        special1 = ",_!@*%#$."
        special2 = ","
        list1 = ["adipiscing", "Aliquam", "Suspendisse"]
        strfind = "vulputate"

        expected1 = "ido mes mauqilA tile gnicsipida rutetcesnoc tema tis rolod muspi meroL\ni,d,o,m,e,s,m,a,u,q,i,l,A,t,i,l,e,g,n,i,c,s,i,p,i,d,a,r,u,t,e,t,c,e,s,n,o,c,t,e,m,a,t,i,s,r,o,l,o,d,m,u,s,p,i,m,e,r,o,L\nEvery string in ['adipiscing', 'Aliquam', 'Suspendisse'] were present\n['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Aliquam', 'sem', 'odio', 'varius', 'nec', 'aliquam', 'nec', 'tempor', 'commodo', 'ante', 'Pellentesque', 'sit']\n['ultricies', 'ac', 'mattis', 'erat', 'aliquet', 'pretium', 'risus', 'Nullam', 'congue', 'lacus', 'mollis', 'nulla', 'laoreet', 'Cras', 'rutrum', 'justo', 'volutpat', 'bibendum', 'nibh', 'tortor']\n851\n"

        # Redirect standard output to a StringIO object
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            stringmethod(para, special1, special2, list1, strfind)
            actual1 = mock_stdout.getvalue()

        self.assertEqual(actual1, expected1)


if __name__ == "__main__":
    unittest.main()
