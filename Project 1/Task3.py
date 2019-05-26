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
# 0) get all calling numbers
# 1) get mobile numbers, these always start with 7,8,9.
#   they have spaces
# 2) get telemarketers numbers, they have no spaces and start with 140.
# 3) get fixed numbers these start with paretheis ()
# 4) add number list and order them in lexicographic order

# 0) Get all calling numbers, these will be filtered out in the next step
# Param 1: takes in calls
def getCallers(recordType):

  # Callers list to be turned
  callers = []
  i = 0
  for item in range (len(recordType)):
    callers.append(recordType[i][0])
    i = i + 1

  return callers

callerList = getCallers(calls)

# 1) get mobile numbers
# Param 1: takes in callsList from getCallers function
def filterMobileNumbers(callList):

    # Get mobile numbers that start with 7,8,9
    list7 = [i for i in callList if i.startswith('7')]
    list8 = [j for j in callList if j.startswith('8')]
    list9 = [x for x in callList if x.startswith('9')]

    # Combine all List
    combinedList = list7 + list8 + list9

    finalMobileAreaCodes = []
    mobileAreaCodes = []

    # I need to iterator over combined list index
    j = 0
    for i in range(len(combinedList)):
        mobileAreaCodes.append( combinedList[j][:4] )
        j = j + 1

    # only add unique area codes to final list
    finalMobileAreaCodes = []
    for e in mobileAreaCodes:
        if e not in finalMobileAreaCodes:
            finalMobileAreaCodes.append(e)
    return finalMobileAreaCodes


# 2) Get Telemarketers line number codes
# I didnt really need to do this, I could have just added + 140 to the end result
# but here is the filter helper function to find are code 140
def filterTelemarketerNumbers(callList):

    # get telemarketer numbers
    list140 = [y for y in callList if y.startswith('140')]

    finalTeleAreaCodes = []
    teleAreaCodes = []
    j = 0
    for i in range(len(list140)):
        teleAreaCodes.append( list140[j][:3] )
        j = j + 1

    # only add unique area codes to final list
    finalTeleAreaCodes = []
    for e in teleAreaCodes:
        if e not in finalTeleAreaCodes:
            finalTeleAreaCodes.append(e)
    return finalTeleAreaCodes

#3) get Fixed line numbers
def filterFixedNumbers(callList):

    # Get fixed line numbers
    list0 = [z for z in callList if z.startswith('(0')]

    # cut remainder of number and leave only area codes
    index = 0
    fixedAreaCode = []
    fixedAreaCodes = []
    for ind in range(len(list0)):
        fixedAreaCode = list0[index].split(')',1)[0]
        fixedAreaCodes.append(fixedAreaCode)
        index = index + 1

    # only add unique area codes to final list
    finalFixedAreaCode = []
    for e in fixedAreaCodes:
        if e not in finalFixedAreaCode:
            finalFixedAreaCode.append(e)
    return finalFixedAreaCode

# Set each function to a var
# that way I can pass them into the orderCodes function
fCodes = filterFixedNumbers(callerList)
mCodes = filterMobileNumbers(callerList)
tCodes  = filterTelemarketerNumbers(callerList)
finalCodes = fCodes + mCodes + tCodes

def orderCodes(codes):

    sortedCodes = sorted(codes, key=str)
    i = 0
    for item in range(len(sortedCodes)):
        print (sortedCodes[i])
        i = i + 1

print ("Part A: \nThe numbers called by people in Bangalore have codes:")
orderCodes(finalCodes)
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

  # List to keep track of (080) numbers calls to other (080) numbers.
  callTracker = []

  # Iterator
  i = 0
  
  # Loop through calls list
  for item in range (len (calls)):
      
      # Set two variables for each col index
      callers = calls[i][0]
      callRecievers = calls[i][1]

      # If both col index's of callers and call recivers start with 080
      # then add it to the callTracker list
      if callers.startswith('(080') and callRecievers.startswith('(080)'):

          # Since I already know only matching numbers will appear here
          # I can safely just append only one of the index's, as they come in pairs and cannot exist without another and
          # Adding both indexes is pointless because I am going to get the length of the list. 
          
          callTracker.append(callers)
      
      # Increment the index's, so that I can loop through the entire calls file.
      i = i + 1
      
  # Get the total amount of numbers calling from calls list
  # Get the total amount of calls made to (080) numbers in list length
  # Convert Both of these to floats for decimal formatting.
  callAmount = float(len(calls))
  recievingAmount = float(len(callTracker))

  # Divide total calls that were made to (080) numbers by the total amount of calls.
  # Multiple by 100 to get a solid percentage.
  callPercentage = (recievingAmount / callAmount) * 100

  # Round the percentage by 2
  callPercentageRounded = round(callPercentage,2)
  print( str(callPercentageRounded) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

getBalgalorCalls(calls)
