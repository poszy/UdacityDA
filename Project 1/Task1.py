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

# I am not sure if this question wants me to,
# 1) find unique records from lists indivudually, and append records.
# 2) do a direct comparison between both lists, record by record and filter for unique records
# So I added both lists and filtered through the records for unqiue elements.

# Creating two empty lists to append unique records.
combinedLists  = []
finalCallsList = []
finalTextsList = []

def trimListToNumber(uniqueList, recordType):

  i = 0
  x = 0
  for item in range (len (recordType)):

    uniqueList.append(recordType[i][0])
    uniqueList.append(recordType[x][1])
    i = i + 1
    x = x + 1

  return uniqueList


def combineLists(trimedCallsList, trimedTextsList):
  finalList = trimedCallsList + trimedTextsList
  return finalList

# This function will filter through the final combined list
# This filters for unique phone numbers
def filterNumbers(resultList,cList):
  for e in resultList:
    if e not in cList:
      cList.append(e)
  return cList

# Set vars equal to the results of trimming the lists down to numbers
a = trimListToNumber(finalCallsList,calls)
b = trimListToNumber(finalTextsList,texts)

# Set var equal to the result of combining previous lists that were trimmed down to numbers
c = combineLists(a,b)
f = []
# Total number in combined calls list is 10,426
#print (len(a))
# TotalNumber in combined text numbers is 18,144
#print (len(b))
#print (len(combineLists(a,b)))

# Finally print the result of the combined list filtered for unique numbers
print (filterNumbers(c,f))
