
#!/usr/bin/python
# Efficiency consists of space and time,
# When we refer to the efficiency of a program,
# we refer to the time it takes to run the program and how much space it takes up in the computers RAM
# there will be trade offs between the two where you can design a progfram that runs faster by slecting a data structure that takes up more space or vice versa

## QUIZ Question
# In thinking about the efficiency of a program, which is more important: The time the program will take to run, or the amount of space the program will require?
# This depends on what kind of problem we have.

# Algorithm
#An algorithm is essentially a series of steps for solving a problem.
# Usually, an algorithm takes some kind of input (such as an unsorted list) and then produces the desired output (such as a sorted list)

####
####
#### Quantifying efficiency
####
####

# This program will give 200 to the given input
def some_function(n):
    for i in range(2):
        n += 100
    return n

print (some_function(1))
print "******************"


# This program will  also give 200 to the given input
def other_function(n):
    for i in range(100):
        n += 2
    return n
print (other_function(1))
print "******************"


# Which function is "more efficient/ faster" ?
# some_function because the amount of operations is smaller
# some_function will run the for loop twice and will only run 5 lines of codeself.
# other_funciton will loop 100 times and run 103 lines of codeself.

# counting lines of code ran is not always accurate but for this case we can clearly see what function is more efficient.print (some_function(1))

####
####
#### Input size and efficiency
####
####

# If we take some_function and give it the input 100
# The same number of lines will run in any case
def some_function(n):
    for i in range(2): # 2 is staic and will only run twice regardless of the input.
        n += 100
    return n

print (some_function(1000))
print "******************"


# Now with a say_hello function
# say_hello(2) will require more lines of code to be ran. because the input
# is increasing. in the previous functions the input was static.
# when n goes up by 1, the number of lines run also goes up by 1
# this is a linear relationship
def say_hello(n):
    for i in range(n):
        print("Hello!")
print (say_hello(1))
print (say_hello(2))
print "******************"

# As the input to an algorithm increases, the time required to run the algorithm may also increase.

# for example, notice this fucnitno when the input goes up by a certain amount, the numbers
# of operations goes up by the square of that amountselfself.
# This is known as a quadratic rate.
def say_hello2(n):
    for i in range(n):
        for i in range(n):
            print("Hello2!")
print (say_hello2(2))

# As the input to an algorithm increase the time requried ot run the algorithm may also increase and different algorithm may increase at different rates.

####
####
#### ORDER
####
####

# NOTE: people refer to teh rate of increase of an algorithm, they will somtimes say ORDER.
# instead of saying "this relationship has a lineaer rate of increase"
# we say, "the order of this relationship is linear"

####
####
#### Big O Notation
####
####

## Refer to hand notes 5/4/19
