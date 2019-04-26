#!/usr/bin/python

#Python functionsinvolves a function declaration def that takes one or more values,
# and a return that returns one or more values. no data type required

# If the function does not hae a return value or statement
# the fucntion will return None

# A pyhon GENERATOR is like a function, but instead of returning a values
# The GENERATOR uses a YIELD statement . The YIELD statement pauses the process
# GENERATORS are useful when using large collections of data without storing
# it all in memory, also with large or infinite SERIES.

# This generator will print even numbers. since printing all even numbers
# will take forever. but GENERATOR will stop the process and can be resumed when needed

# YIELD stops everyting and the value is returned. then calling next()
# will resume where it left offself.

def all_even():
    n = 0
    while True:
        yield n
        n = n + 3


myGen = all_even()

#Do this five times
for i in range(5):
    #run function myGen, as yield is called, next, will run it again.
    print (next(myGen))

doSomething = 4
doSomething = doSomething + 4
print ("******" + str (doSomething))

for i in range(100):
    print(next(myGen))
