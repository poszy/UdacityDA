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

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

## Part A
# 0) get all calling numbers
# 1) get mobile numbers, these always start with 7,8,9.
#   they have spaces
# 2) get telemarketers numbers, they have no spaces and start with 140.
# 3) get fixed numbers these start with paretheis ()
# 4) add number list and order them in lexicographic order


#0) get all calling numbers, tehse will be filtered out in the next step
callers = []
def getCallers(uniqueList, recordType):

  i = 0
  for item in range (len(recordType)):
    uniqueList.append(recordType[i][0])
    i = i + 1
  #print len(uniqueList)
  return uniqueList

callerList = getCallers(callers,calls)

# 1) get mobile numbers
def filterMobileNumbers(callList):
    #filteredList = [ s for s in callList if any (i in s for i in filters)]
    # Get mobile numbers that start with 7,8,9
    list7 = [i for i in callList if i.startswith('7')]
    list8 = [j for j in callList if j.startswith('8')]
    list9 = [x for x in callList if x.startswith('9')]
    combinedList = list7 + list8 + list9

    finalMobileAreaCodes = []
    mobileAreaCodes = []
    j = 0
    for i in range(len(combinedList)):
        mobileAreaCodes.append( combinedList[j][:4] )
        j = j + 1
    
    #print mobileAreaCode
    # only add unique area codes to final list
    finalMobileAreaCodes = []
    for e in mobileAreaCodes:
        if e not in finalMobileAreaCodes:
            finalMobileAreaCodes.append(e)
    return finalMobileAreaCodes


#2) get Telemarketers line number codes
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
    
    #print teleAreaCodes
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




