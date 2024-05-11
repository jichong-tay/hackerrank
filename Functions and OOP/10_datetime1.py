"""
Python - DateTime

Import datetime module.
Define a function called 'dateandtime', which takes 2 parammeters.
- The first paramter is val, which takes an integer(1-6).
- The second paramter is tup, a tuple whose values change based on the value of the val parameter.

Input Constraints
- When the value of val is 1 and 4, the tuple will contain 3 values in the order of (year, month, day) in the form of an integer.
- When the value of val is 2, the tuple will contain a single value that is the timestamp.
- When the value of val is 3, the tuple will contain 3 values in the order of (hour, minutes, seconds) in the form of an integer.
- When the value of val is 5, the tuple will contain 6 values in the order of (year, month, day, hours, minutes, seconds) in the form of an integer.

The function definition code stub is given in the editor.
Generate printe statements based on the following conditions:

1. Declare and empty list.
2. When the value of val is 1:
- Convert the tuple to date and append it to the list.
3. When the value of val is 2:
- Convert the tuple into a date and append it to the list.
4. When the value of val is 3:
- Convert the tuple into a time and append it to the list.
- Extract the Hour 00-12 format of the time and append it to the list.
5.When the value of val is 4:
- Convert the tuple into a date.
- From the date, extract the Weekday (full version) and append it to the list.
- From the date, extract the Month name (full version) and append it to the list.
- From the date, extract the Day number of the year (001-366) and append it to the list.
6. When the value of val is 5:
- Convert the tuple to a datetime and append it to the list.
7. Return the list.  

"""

import datetime


def dateandtime(val, tup):
    # Write your code here
    list1 = []

    if val == 1:
        date1 = datetime.date(*tup)
        list1.append(date1)

        date2 = date1.strftime("%d/%m/%Y")
        list1.append(date2)

    elif val == 2:
        date1 = datetime.date.fromtimestamp(tup[0])
        list1.append(date1)

    elif val == 3:
        time1 = datetime.time(*tup)
        list1.append(time1)
        time2 = time1.strftime("%I")
        list1.append(time2)

    elif val == 5:
        output = datetime.datetime(*tup)
        list1.append(output)

    elif val == 4:

        date1 = datetime.date(*tup)

        weekday_full = date1.strftime("%A")
        list1.append(weekday_full)

        month_full = date1.strftime("%B")
        list1.append(month_full)

        day_of_year = date1.strftime("%j")
        list1.append(day_of_year)

    return list1
