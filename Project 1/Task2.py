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

# Variables to hold the trimmed down versions of the columns. answeringNumber,
# timeAnswerd + timeSpend in seconds.
answeringNumber = []
timeAnswered = []
timeSpent = []

# This function pulls in the calls list and trims it down to a specific col
# answeringNumber,timeAnswerd + timeSpend in seconds.
# Param 1: this param takes in a list dedicated to answeringNumber,timeAnswerd + timeSpend in seconds
# Param 2: takes in the calls list
# Param 3: colNumber can be changed to parse the desired col fromansweringNumber,timeAnswerd + timeSpend in seconds
def trimListToCol(uniqueList, recordType, colNumber):

  # Iterator that increases on col index.
  i = 0
  # loop through calls list
  for item in range (len (recordType)):
    # add the index to list.  
    uniqueList.append(recordType[i][colNumber])
    i = i + 1

  return uniqueList


# I have no idea when and what constitutes the calls being "answered". is this a few seconds?
# How do I know how long it takes a person picking up a call based off of a timestamp?
# Because of this delema I will only parse the seconds from the timestamp and assume
# this is a reasonable amount of seconds it took someone to answer the phone.

# Param 1: takes the previously stripped timeAnswered list and will
# parse the seconds from the timestamp
def trimSecondsFromTimeAnswered(timeAnswered):

  # Var to hold seconds and iterator
  finalSeconds = []
  i = 0
   
  #parse the seconds and add them to a list
  for item in range(len(timeAnswered)):

      #Parse the seconds and add them to the finalSeconds list.
      seconds = timeAnswered[1].rsplit(':',1)[1]
      finalSeconds.append(seconds)
      i = i + 1
  return finalSeconds


# Adds the trimed seconds from trimSecondsFromTimeAnswered and what is already present
# inside the timeSpentList
# Param 1: seconds is the seconds list from the previous trimSecondsFromTimeAnswered function
# Param 2: timespent is the total time spent from the trimSecondsFromTimeAnswered funciton
def addSecondsToTimeSpent(seconds,timeSpent):

  # Vars to hold the lists
  finalTimeSpent = []
  convertedSeconds = []
  convertedTimeSpent = []

  # I need two iterators for secondsList and timeSpent
  i = 0
  j = 0
  
  # I must convert both lists to intergers before I can
  # add both coresponding indexes together to get final seconds.
  for item in range(len(seconds)):
    seconds[i] = int(seconds[i])
    convertedSeconds.append(seconds[i])
    i = i + 1

  for item in range(len(timeSpent)):
    timeSpent[j] = int(timeSpent[j])
    convertedTimeSpent.append(timeSpent[j])
    j = j + 1

  # Now that the lists are converted I can add their indexes safley
  # and add them to their own list.
  finalTimeSpent = [x + y for x, y in zip(convertedSeconds,convertedTimeSpent)]
  
  return finalTimeSpent


# Since the lists have not been altred in order it is safe to assume I can add
# the trimmed and added time list to the answering number list and have the values and indexes
# correlated correctly
# Param 1: takes in the answeringNumber list from trimSecondsFromTimeAnswered function.
# Param 2: takes in the finalTimeSpent list from addSecondsToTimeSpent
def organizeFilterFinalNumber(answeringNumber, finalTimeSpent):
  
  # Converting to Tuple for ease and do not have to worry about alterting any more data
  finalNumber = tuple(zip(answeringNumber, finalTimeSpent))
  
  # now I wil sort the list according to the second col (time) and highest value and
  # return the first row/col that is on top.
  last = max(finalNumber,key=itemgetter(1))
  
  print "Phone number %s spent the longest time %s seconds, on the phone during September 2016." % last
  

# Trim down each col and assign them to a ref var
fAnsweringNumber = trimListToCol(answeringNumber, calls, 1)
timeAnswered     = trimListToCol(timeAnswered, calls, 2)
timeSpent        = trimListToCol(timeSpent, calls, 3)

# Seconds trimmed fromtimeAnsweredList
seconds = trimSecondsFromTimeAnswered(timeAnswered)

# Fintal time spend based off of added trimmed seconds and seconds List
finalTimeSpent = addSecondsToTimeSpent(seconds,timeSpent)
organizeFilterFinalNumber(fAnsweringNumber, finalTimeSpent)
