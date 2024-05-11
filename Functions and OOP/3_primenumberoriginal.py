"""
Prime Number Generator

Define a function called `primegenerator`, which takes two parameters.
The parameter 'num' is an integer and is the range up to which the prime number must be generated,
and the parameter 'val' contains either 0 or 1.
The function definition code stub is given in the editor.
Use the concept of generator to yield prime numbers based on the following conditions:

1. The prime numbers for the 'num' value of 21 are
... 2, 3, 5, 7, 11, 13, 17, 19

2. If the value of 'val' is 0, then you should yield the following values
... 3, 7, 13, 19

3. If the value of 'val' is 1, then you should yield the following valuee
... 2, 5, 11, 17

Contraints
- The 'num' value is inclusive

"""

import unittest


def primegenerator(num, val):
    "primegenerator yield prime number based on val"
    primes = [2] if num >= 2 else []
    for i in range(3, num + 1):
        if is_prime(i):
            primes.append(i)
    if val == 0:
        yield from (primes[i] for i in range(len(primes)) if i % 2 == 1)
    elif val == 1:
        yield from (primes[i] for i in range(len(primes)) if i % 2 == 0)


def is_prime(n):
    "is_prime check for prime number and return bool"
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class TestPrimeGenerator(unittest.TestCase):
    "Test for primegenerator function"

    def test_prime_generator(self):
        "Test for primegenerator function"
        num = 21
        val = 1
        expected_output = [2, 5, 11, 17]

        # Capture the output of the generator
        output_gen = primegenerator(num, val)
        output_list = list(output_gen)

        # Check if the generated list matches the expected output
        self.assertEqual(output_list, expected_output)


if __name__ == "__main__":
    unittest.main()
