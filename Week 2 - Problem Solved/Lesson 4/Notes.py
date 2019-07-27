
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

# Name        Big O
# ------------------------
# Constant    O(c)
# Linear      O(n) OR O(1)
# Quadratic   O(n^2)
# Cubic       O(n^3)
# Exponential O(2^n)
# Logarithmic O(log(n))
# Log Linear  O(nlog(n))

## Refer to hand notes 5/4/19

## Constant Complexity
## In the above script, irrespective of the input size, or the number of items in the input list items, the algorithm performs only 2 steps:
## Finding the square of the first element and printing the result on the screen.
## Hence, the complexity remains constant. If we were to plot this, this would be a straight line. 

def constant_algo(items):  
    result = items[0] * items[0]
    print ()

constant_algo([4, 5, 6, 8])  

## Linear Complexity
## since the number of iterations of the for-loop will be equal to the size of the input items array.
## For instance, if there are 4 items in the items list, the for-loop will be executed 4 times, and so on.

def linear_algo(items):  
    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])

## With linear complexity huge number of inputs the constants become insignificant,
## For instance, there are two for loops that iterate over the input items list
## the complexity of the algorithm becaomes O(2n)
## However in  case of inifinite items in the input list,
## the twice of inifinity is still equal to nifinity, thereforte we can ignore the constant 2
## Since it is ultimately insignificant and the complexity of the algorithm becomes O(n)
def linear_algo(items):  
    for item in items:
        print(item)

    for item in items:
        print(item)
linear_algo([4, 5, 6, 8])  


## Quadratic Complexity O(N^2
## The steps required to execute this algorithm is a quadratic function of the number of items in the input.
## We have an outer loop that iterates through all the items in the input list and then a nested inner loop
## which iterates through all the items in the list.
## the steps performed are n * n, where n is the number of items in the input array.
## This plots as a curve.
def linear_algo(items):  
    for item in items:
        print(item)

    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])  


## Finding complexity of complex Functions

def complex_algo(items):

    # The complexity of this part is O(5). Since five constant steps are being performed in this piece of code irrespective of the input.
    for i in range(5):
        print ("Python is awesome")

    # We know the complexity of this piece of code is O(n).    
    for item in items:
        print(item)

    # Similarly, the complexity of the following piece of code is also O(n)    
    for item in items:
        print(item)
        
    # Finally, in the following piece of code, a string is being printed three times, hence the complexity is O(3)    
    print("Big O")
    print("Big O")
    print("Big O")

    # To find the overall complexity we simply have to add these individual complexities.
    # O(5) + O(n) + O(n) + O(3)
    # =
    # O(8) + O(2n)

    # In this case 0(2n) is a constant and can be ignored. because inifinity times infiity is also infinity
    # the final time complexity for this function is O(n)
    
complex_algo([4, 5, 6, 8])  



## Worst vs Best Case Complexity
## When someone asks you about the complexity of the algorithm he is asking you about the worst case complexity.
## In this script we have a funciton that takes anumber and a list of numbers as input
## it returns true if the passed number is found in the list of numbers, otherwise it returns false.
#### if you search 2 in the list, it will be found in the firt comparison
#### this is the best case complexity of the algorithm that the searched item is found in the first index.
#### This best case complexity is 0(1)
#### on the other hand, if you search 10, it will be in the last index.
#### hence the algorithm will have to search through all the items in the list, hence the worse case complexity becoimes O(n)
def search_algo(num, items):  
    for item in items:
        if item == num:
            return True
        else:
            return False
nums = [2, 4, 6, 8, 10]

print(search_algo(2, nums))  

### Logarithmic  Time O(log n)
## its when an algorithm reduces time complexity when it reduces the size of the input data in each step.
## each step we are only viewing the index.

for index in range(0, len(data), 3):
    print(data[index])

## this is common in binary search and binary trees
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1

while left <= right:
        middle = (left + right) / 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle

raise ValueError('Value is not in the list')

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))
    

## Quasilinear Time O(n log n)
## an algorithm is said to have a quasilinear time complexity when each
## operation in the input data has a logarithm time Complexity
## it is commonly seen in sorting algorithms ( mergesort, timesort, heapsort)

## For example for each value in the data1 (O(n) use the binary search (O(logn)) to search the same value in data2
for value in data1:
    result.append(binary_search(data2, value))
