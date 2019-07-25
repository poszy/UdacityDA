"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from operator import itemgetter

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.


Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during>
"""

# This function will get the total amount of time spent on a call with
# a corresponding number as a key
# Param 1: call record list. 
def getTimeSpent(calls):

    # Creating dictionary to keep track of phone numbers as keys
    finalTimeSpent = {}

    # loop through calls file
    for number in calls:
        
        # number[0] is the first col in calls.
        # number[-1] is the last col in calls.
        # if the first col is not in finalTimeSpentList append the last col
        # in secods to finalTimeSpent
        if number[0] not in finalTimeSpent.keys():
            finalTimeSpent[number[0]] = int(number[-1])
            
        # If the number already exists as a key in finalTimeSpent
        # Just add the last col (seconds) to the existsing value
        # This will allow me to get the total time of time on the phone
        else:
            finalTimeSpent[number[0]] = finalTimeSpent[number[0]] + int(number[-1])

        # Now I add the seconds from the answering numbers
        # number[1]  is the second col in calls
        # number[-1] is the last   col in calls
        # if the first col is not in finalTimeSpentList append the last col
        # in secods to finalTimeSpent
        if number[1] not in finalTimeSpent.keys():
             finalTimeSpent[number[1]] = int(number[-1])
             
        # If the number already exists as a key in finalTimeSpent
        # Just add the last col (seconds) to the existsing value
        
        else:
             finalTimeSpent[number[1]] = finalTimeSpent[number[1]] + int(number[-1])

    return finalTimeSpent

# Set var as a refference, this will be passed to a filter funciton
finalTimeSpent = getTimeSpent(calls)

# This function will taked in
# Param 1: the dictionary that has the number and seconds spent on the phone
def filterForLongestCall(finalTimeSpent):

    # Var to store the highest value in a corresponding dictionary key
    longestCallTime = max(finalTimeSpent.values())

    #Var to store the phonenumber associated with the highest value ( time on call)
    phoneNumber = [i for i, j in finalTimeSpent.items() if j == longestCallTime]

    # Print the results
    print(phoneNumber[0],"spent the longest time", longestCallTime, "seconds, on the phone during September 2016.")


filterForLongestCall(finalTimeSpent)
