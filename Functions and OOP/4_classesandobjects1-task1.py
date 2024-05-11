"""
Cinema Ticket

1. Define a class 'Movie' that represents
  -Name of the Movie
  -Number of Tickets
  -Total cost
of a movie ticket printing machine.

Hint
Define the initializer method, __init__, that takes three values and assigns them to the above 3  attributes, respectively.

2. Improve the class definition of 'Movie' such that any Movie object is displayed in the following format:

Sample:

Movie: Kabir Sigh
Number of Tickets: 5
Total Cost: 666

Hint: Define the method __str__ inside the class 'Movie'

"""

import unittest


class Movie:
    def __init__(self, name, tickets, cost):
        self.name = name
        self.tickets = tickets
        self.cost = cost

    def __str__(self):
        return f"Movie : {self.name}\nNumber of Tickets : {self.tickets}\nTotal Cost : {self.cost}"


class TestMovieClass(unittest.TestCase):
    "Test for movieClass function"

    def test_movie_class(self):
        moviename = "Star Wars"
        numoftickets = 2
        cost = 210
        expected_output = "Movie : Star Wars\nNumber of Tickets : 2\nTotal Cost : 210"

        movie = Movie(moviename, numoftickets, cost)
        self.assertEqual(movie.name, moviename)
        self.assertEqual(movie.tickets, numoftickets)
        self.assertEqual(movie.cost, cost)
        self.assertEqual(str(movie), expected_output)


if __name__ == "__main__":
    unittest.main()
