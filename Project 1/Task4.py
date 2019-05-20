"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.



"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during>


# 1) get the numbers that are making outgoing calls - calls (incoming) first col.

# 2) get numbers that do not send texts.
# -----------  get numbers that do send texts - if outgoing calls numbers appear in this list, delete them from list.


# 3) get numbers that do not get texts
--- get all numbers that do get texts if outgoing calls numbers appear in this list, delete fthem from list

# get numbers that do not get calls
-- get numbers that do get calls, -if they appear in in numbers list, delete them from the list.
-------

"""
# This function will strip calls or texts record type
# and add them to their own list
# Param 1: takes an index to parse the desired col.
# Param 2: takes in a list of calls or text
def getCallText(index, recordType):
    
  # I need a list add the desired col
  uniqueList = []
  i = 0

  # Loop through calls or text and add the col based of index
  # to the list
  for item in range (len (recordType)):
    uniqueList.append(recordType[i][index])
    i = i + 1

  return uniqueList

# Set variables equal to number lists I am stripping from calling or texting numbers.
CallingNumbers   = getCallText(0, calls)
CallRecievers    = getCallText(1,calls)

TextRecievers    = getCallText(0,texts)
TextingNumbers   = getCallText(1, texts)

# This function strips away non telemarketer numbers
# Param 1-4: takes in the list of CallingNumber,CallRecievers,TextRecivers,TextingNumbers
def StripNumbersFromCallingNumbers(tNumbers,cNumbers,tReceivers,cReceivers):
    
  # New list that will contain texting numbers removed from calling numbers
  # If calling numbers are not in Texting numbers
  # add them to a new list, cause if they are they do not belong to telemarketers
  strippedNumbers = [x for x in cNumbers if x not in tNumbers]


  # Wash rinse and repeat the process. Now I will strip
  # Numbers that are recieving text from my strippedNumbers list
  # because if any of these numbers are receiving texts, they are not telemarketers.
  nStrippedNumbers = [x for x in strippedNumbers if x not in tReceivers]
  n1StrippedNumbers = [x for x in nStrippedNumbers if x not in cReceivers]
  

  # Now to remove any duplicates from the stripped numbers
  rDuplicated = []
  for number in n1StrippedNumbers:
        if number not in rDuplicated:
            rDuplicated.append(number)

  # Return numbers in lexicographic order, using str as using int as a key will
  # not return since there are spaces in the numbers
  sortedNumbers = sorted(rDuplicated, key=str)

  i = 0
  for item in range(len(sortedNumbers)):
    print sortedNumbers[i]
    i = i + 1


print "These numbers could be telemarketers"
StripNumbersFromCallingNumbers(TextingNumbers,CallingNumbers,TextRecievers,CallRecievers)

"""
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
