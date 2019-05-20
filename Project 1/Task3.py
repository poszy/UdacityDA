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
        print sortedCodes[i]
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


# Get numbers of callers or revcivers and filter for fixed 080 area codes
# Param 1: takes in calls list
# Takes in an index. 0 for callers and 1 for caller recievers
def getCallersOrReceivers(recordType, index):

  # List to hold callers from calls and iterator
  callers = []
  i = 0

  # Loop through and append each call
  for item in range (len (recordType)):
    callers.append(recordType[i][index])
    i = i + 1
    
  # Filter for numbers that start with 080
  list080 = [z for z in callers if z.startswith('(080)')]
  
  return list080

# Set Ref vars to the callers and call recivers final list numbers
finalCallers       = getCallersOrReceivers(calls,0)
finalCallRecievers = getCallersOrReceivers(calls,1)


# Get len of master list and divide that by total number of calls ( len of calls) & format two decimals
# Param 1: takes in callers list from getCallersOrReceivers function.
# Param 2: takes in call recievers list from getCallersOrReceivers function
def getCallPercentage(callers,recivers):
    
    #Get the total amount of calling and receicing and convert to float.
    callAmount = float(len(callers))
    recievingAmount = float(len(recivers))

    #Divide calls outgoing by calls incoming and multiple by 100 to get a solid percentage
    callPercentage = (callAmount / recievingAmount) * 100

    #round the percentage by 2 
    callPercentageRounded = round(callPercentage,2)
    print( str(callPercentageRounded)
           + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
    
print ("PART B: ")
getCallPercentage(finalCallers, finalCallRecievers)
    
    
