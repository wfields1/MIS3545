"""
Question 1:
"""


def crazy_about_9(a, b):
    """
    a, b: two integers
    Returns True if either one is 9, or if their sum or difference is 9. 
    """
    # Your Code Here
    if a == 9:
        return('True')
    elif b == 9:
        return('True')
    elif a + b == 9:
        return('True')
    elif a - b == 9:
        return('True')
    elif b - a == 9:
        return('True')
    else:
        return('False')
    #return Your Answer Here


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(crazy_about_9(2, 9))
# print(crazy_about_9(4, 5))
# print(crazy_about_9(3, 8))


"""
-----------------------------------------------------------------------
Question 2:
A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
"""

year = 1
def leap_year(year):
    """
    year(int): a year
    Returns True if year is a leap_year, False if year is not a leap_year.
    """
    # Your Code Here


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))


"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes The sum of all squares between
1 and n (inclusive).
"""

result = 1
def sum_squares(n):
    for i in range(n):
        result += result 
    # Your Code Here


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))