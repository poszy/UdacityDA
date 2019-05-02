#!/usr/bin/python

# Expected output:
# If you were born 1 Jan 2012, and today is 2 jan 2012
# you are 1 day old.

# Requirements:
# Must account for leapdays.

# Define a procedure daysBetweenDates, that takes two dtes and inputs and returns
# the number of days between the first and second date
# each date is passed in as three numbers giving a valid year, mont and day
# in the gregorian calendar.
# the second date must ot be before the first.

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!

    return 0

def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

testDaysBetweenDates()
