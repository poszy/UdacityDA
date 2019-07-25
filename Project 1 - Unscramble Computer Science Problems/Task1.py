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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# This function will get both phone numbers from
# outgoing/receiving calls and texts
# Param 1: takes in a record type of either calls or texts
def trimListToNumber(recordType):
    
  # This list will be appened the phone numbers
  uniqueList = []
  
  # Iterators that will run through the indexes of the senders
  # and recievers of callers or texts.
  i = 0
  x = 0

  # loop through the given recordType of either calls or texts
  for item in range (len (recordType)):

    # Add the outgoing, caller or texters number
    uniqueList.append(recordType[i][0])

    # Add the receiving, call or text receiver number
    uniqueList.append(recordType[x][1])

    # Increment to have the next iteration add the next index.
    i = i + 1
    x = x + 1

  # Return all numbers in one list.
  return uniqueList

# This function takes in two lists and combines them.
# Param #1:will take in the calls list that has both outgoing and receving numbers
# Param #2:will take in the texts list that has both outgoing and receving texts numbers
def combineLists(trimedCallsList, trimedTextsList):
    
  # Combine both list
  finalList = trimedCallsList + trimedTextsList

  # Return the list
  return finalList

# this function will filter the combinedLists
# Param #1: Takes in a combinedLists refference variables and
# will filter, by adding only unique numbers to a new list
def filterNumbers(combinedList):
    
  # Create a final list to add only the unique numbers
  finalList = []

  # Filter through combinedList
  for e in combinedList:
      
    # if a number does not already exists, add it to the finalList
    # if it is, do nothing.
    if e not in finalList:
      finalList.append(e)
      
  # return the final list    
  return finalList



# Set vars equal to the results of trimming the lists down to numbers
allCallNumbers = trimListToNumber(calls)
allTextNumbers = trimListToNumber(texts)

# Set var equal to the result of combining previous lists that were trimmed down to numbers
allCombinedNumbers = combineLists(allCallNumbers,allTextNumbers)

# Set var equal to final filtered List
masterList = filterNumbers(allCombinedNumbers)


# Finally print the result of the combined list filtered for unique numbers
print(
    "There are " 
    + str(len(masterList))
    + " different telephone numbers in the records."
    )
