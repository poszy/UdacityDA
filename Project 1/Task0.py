"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('./texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# Prints first record of texts, I am not sure if there was a range of text (first ten records)
# So I am only printing out the first records
print ("First record of texts, "
       + str(texts[0][0])[1:-1]
       + " texts "
       + str(texts[0][1])[1:-1]
       + " at time "
       + str(texts[0][2])[1:-1] )

# Prints out the last record in calls. 
print ("Last Record of calls, "
       + str(calls[-1][0])[1:-1]
       + " calls "
       + str(calls[-1][1])[1:-1]
       + " at time, "
       + str(calls[-1][2])[1:-1]
       + " lasting "
       + str(calls[-1][3])[1:-1]
       + " seconds" )

# Also I am not sure if the list element  [] brackets are needed in the output so I just left them.
