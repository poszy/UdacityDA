"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number+
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

## Part A
def getCallers(recordType):

  # Callers list to be turned
  masterList = []
  # Find all numbers that begin with 080 
  for item in recordType:
    if item[0].startswith("(080)") and item[1] not in masterList:
        masterList.append(item[1])

  return masterList

callerList = getCallers(calls)

# 1) get mobile numbers
# Param 1: takes in callsList from getCallers function
def filterforNumbers(callList):
    
    # This will contain all numbers
    codes = []
    # Filter remaining numbers that start with 080
    for prefix in callList:

        # find numbers that start with parenthesis. and chop the paranthesis off.
        if prefix[0].startswith('('):
            prefix = prefix[1: prefix.find(')')]

            # add the prefix if its not in the codes list
            if prefix not in codes:
                codes.append(prefix)
                
        # Wash rinse and repeat for numbers that start with 7,8,9
        elif prefix[0].startswith('7') and prefix[:4] not in codes:
            codes.append(prefix[:4])

        elif prefix[0].startswith('8') and prefix[:4] not in codes:
            codes.append(prefix[:4])

        elif prefix[0].startswith('9') and prefix[:4] not in codes:
            codes.append(prefix[:4])

    return codes


codes = filterforNumbers(callerList)
def orderCodes(codes):

    sortedCodes = sorted(codes, key=str)
    i = 0
    for item in sortedCodes:
        print (sortedCodes[i])
        i = i + 1
    

print ("Part A: \nThe numbers called by people in Bangalore have codes:")
orderCodes(codes)
print ("***************************************************************")



#####
##### PART B
#####

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
print ("PART B: ")

def getBalgalorCalls(calls):

  # Set two variables as trackers
  numbers = 0
  callreceivers = 0

  #loop through calls
  for item in calls:
      # if a number starts with 080 add one to numbers
      if item[0].startswith("(080)"):
          numbers = numbers + 1
      # if both col start with 080 add to call recivers
      if item[0].startswith("(080)") and item[1].startswith("(080)"):
            callreceivers = callreceivers + 1
 
  # Divide call recievers that were made to (080) numbers by numbers that called with (080) prefix.
  # Multiple by 100 to get a solid percentage.
  callPercentage = (callreceivers / numbers) * 100

  # Round the percentage by 2
  callPercentageRounded = round(callPercentage,2)
  print( str(callPercentageRounded) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

  
getBalgalorCalls(calls)

