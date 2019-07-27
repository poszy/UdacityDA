#!/usr/bin/python

# we have four integers x,y,z, answer  and therefore
# the space complexity will be 4 * 4 = 16 Bytes
# This is a constant space complexity, the amount of space used does not chagne with its input size.
def our_constant_function():

    x = 3 # Type int
    y = 345 # Type int
    z = 11 # Type int

    answer = x+y+z

    return answer


# in this example we have two integers n and counter, an expanding list and therefore our space complexity will be
#  4 * n + 4
# since we have an expanding integer list and two integer data types. This is an example of linear space complexity
def our_linear_function(n):

    n = n # Type int
    counter = 0 # Type int
    list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

    while counter < n:
        list_[counter] = counter
        counter = counter + 1

    return list_

print (our_constant_function())
print "**********"
print (our_linear_function(1))
