"""
Python - Calendar

Import the calendar module.
Define a function called 'usingcalendar' which takes the following parameter:
- 'datetuple' - a tuple of(year, month, date)

The function defintion code stub is given in the editor.
Generate the code based on the followig conditions:
Use the calendar module to build the code.

1.Check whether the given year from the tuple is a leap year.
  - if it is a leap year, assign the month's value as 2 throughout the whole function
  -Print the monthly calendar for the specified year and month.
2.Use itermonthdates module from calendar to iterate through the date of the specified month and year in the calendar.
  -Print the 7 dates that appear in the last week of that month starting from monday to sunday as a list.
  -For example, Lets say 29th of that month is on Monday then the last 7 dates will be 29,30,31,1,2,3,4
3.Print the day of the week, which appears on the most frequent in the specified month and year as a string.
 -The string can be "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
 -If there are more than one frequent day, then consider the one that comes first.
 -For example, if there are the same number of Mondays and Tuesdays, then consider Monday.
 -Make sure to check the edge case of Feb month having 28 or 29 days


Sample input:
datetuple = (2020,10,11)  

"""

import calendar
from collections import Counter


def usingcalendar(datetuple):

    year, month, _ = datetuple

    # 1. Print the monthly calendar for the specified year and month.
    if calendar.isleap(year):
        month = 2
    print(calendar.month(year, month))

    # 2. Use itermonthdates
    print(list(calendar.Calendar().itermonthdates(year, month))[-7:])

    # 3. Print the day of the week.
    maxday = Counter(
        d.strftime("%A")
        for d in calendar.Calendar().itermonthdates(year, month)
        if d.month == month
    ).most_common(1)

    print(maxday[0][0])


datetuple = (2020, 10, 11)
usingcalendar(datetuple)


# count = Counter(
#     d.strftime("%A")
#     for d in calendar.Calendar().itermonthdates(year, month)
#     if d.month == month
# )

# print(count)
