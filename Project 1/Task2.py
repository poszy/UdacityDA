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

# For the given dates/time format I am not sure if the format of time is HH/MM/SS or MM/SS/MS
# I am going to assume the format is HH/MM/SS. Also there is no clear indication how long
# someone takes answering the call, so I am just going to strip the seconds from the format
# and add them to the total time (number is col 4), which again is not specific if the time is in,
# Hours or minutes or seconds. I am going to assum these calls are ebing accounted for in Seconds.



# Variables to hold the trimmed down versions of the columns
answeringNumber = []
timeAnswered = []
timeSpent = []

def trimListToCol(uniqueList, recordType, colNumber):

  i = 0
  #x = 0
  for item in range (len (recordType)):

    uniqueList.append(recordType[i][colNumber])
    #uniqueList.append(recordType[x][1])
    i = i + 1
    #x = x + 1

  return uniqueList


# I have no idea when and what constitutes the calls being "answered". is this a few seconds?
# How do I know how long it takes a person picking up a call based off of a timestamp?
# Because of this delema I will only parse the seconds from the timestamp and assume
# this is a reasonable amount of seconds it took someone to answer the phone.

def trimSecondsFromTimeAnswered(timeAnsweredList):

  seconds = []
  i = 0
  fList = []
  #parse the seconds and add them to a list
  for item in range(len(timeAnsweredList)):
      secondss = timeAnsweredList[i]
      s = secondss.rsplit(':',1)[1]
      fList.append(s)
      i = i + 1
  return fList

# Adds the trimed time in seconds from trimSecondsFromTimeAnswered and what is already present
# inside the timeSpentList
def addSecondsToTimeSpent(secondsList,timeSpentList):

  finalTimeSpent = []
  convertedSecondsList = []
  convertedTimeSpentList = []
  i = 0
  j = 0
  # I must convert both lists to intergers before I can
  # add both coresponding indexes together to get final seconds.
  for item in range(len(secondsList)):
    #print ('hello')
    secondsList[i] = int(secondsList[i])
    convertedSecondsList.append(secondsList[i])
    i = i + 1

  for item in range(len(timeSpentList)):
    timeSpentList[j] = int(timeSpentList[j])
    convertedTimeSpentList.append(timeSpentList[j])
    j = j + 1

  # Now that the lists are converted I can add their indexes safley
  # and add them to their own list.

  finalTimeSpent = [x + y for x, y in zip(convertedSecondsList,convertedTimeSpentList)]
  
  #print convertedSecondsList[-1]
  #print convertedTimeSpentList[-1]
  #print finalTimeSpent[-1]
  return finalTimeSpent


# Since all list have not been altred in order it is safe to assume I can add
# the trimmed and added time list to the answering number list and have the values and indexes
# correlated correctly
def organizeFilterFinalNumber(answeringNumberList, finalTimeSpent):
  
  # Converting to Tuple for ease and do not have to worry about alterting any more data
  finalNumberTuple = tuple(zip(answeringNumberList, finalTimeSpent))
  # now I wil sort the list according to the second col (time) and highest value and
  # return the first row/col that is on top.
  
  
  last = max(finalNumberTuple,key=itemgetter(1))
  print "Phone number %s spent the longest time %s seconds, on the phone during September 2016." % last
##
##### Trim Down each col and assign them to a Var
###
fAnsweringNumberList = trimListToCol(answeringNumber, calls, 1)
timeAnsweredList = trimListToCol(timeAnswered, calls, 2)
timeSpentList    = trimListToCol(timeSpent, calls, 3)

# Seconds trimmed fromtimeAnsweredList
secondsList = trimSecondsFromTimeAnswered(timeAnsweredList)

# Fintal time spend based off of added trimmed seconds and seconds List
finalTimeSpent = addSecondsToTimeSpent(secondsList,timeSpentList)
organizeFilterFinalNumber(fAnsweringNumberList, finalTimeSpent)
