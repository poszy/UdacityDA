#!/usr/bin/python3


def power_of_2(n):

    ## Base case
    if n == 0:
        return 1

    ## If base case is not complete. do this.
    # This code is where it breaks the problem down into smaller instances.
    # Using the formula 2^n = 2*2(n-1)
    # this funcion calls itself to calculate 2(n-1)

    # Each function is waiting on the function it called to complete.
    # So, power_of_2(5) is waiting for power_of_2(4), power_of_2(4) is waiting for power_of_2(3)
    
    # power_of_2(5)
    #  power_of_2(4)
    #   power_of_2(3)
    #    power_of_2(1)
    #     power_of_2(1)
    #      power_of_2(0) ## this will return 1

    # In the end, after power_of_2(5) is returned, the final number returned is 2^5 which is 32
    return 2 * power_of_2(n - 1)


print(power_of_2(5))


def sum_integers(n):

  if n==1:
      return 1
  
  return n + sum_integers(n - 1)

print(sum_integers(3))

## Gotchas: When using recursion, there are a few things to look out for that you don't have to worry about when running a loop (iteratively).
##Let's go over a few of those items.

## Call Stack:
## python has a limit on the depth of recursion to prevent a stack overflow.
##However, some compilers will turn tail-recursive functions into an iterative loop to prevent recursion from using up the stack.
##Since Python's compiler doesn't do this, you'll have to watch out for this limit
## This call will cause a RecursionError: maximum recursion depth exceeded in comparison

######print(power_of_2(10000))


## Slicing
## Array slicing
## The list a can be sliced using the following operation: a[start:stop].
## This will return a new list from index start (inclusive) to index stop (exclusive).
## Let's look at an example of a recursive function that takes the sum of all numbers in an array.
## For example, the array of [5, 2, 9, 11] would sum to 27 (5 + 2 + 9 + 11).


def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr))

##Looking at this, you might think it has a running time of O(n), but that isn't correct due to the slice operation array[1:].
## This operation will take O(K) time to run where K is the number of elements to copy. So, this function is actually O( K * n) running time complexity and O(k*n) space complexity.


## Instead of slicing, we can pass the index for the element we want to use for addition
def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))

# sum_array is a polynomial and sum_array_index is linear as we predicted.
# However, in our pursuit to use recursion we actually made things worse. Let's look at an iterative solution to this problem:

def sum_array_iter(array):
    result = 0
    
    for x in array:
        result += x
    
    return result

arr = [1, 2, 3, 4]
print(sum_array_iter(arr))

# The sum_array_iter function is a lot more straightforward than the two recursive functions, which is important.
# Second, to help ensure an answer that is correct and bug free, you generally want to pick the solution that is more readable.
# In some cases recursion is more readable and in some cases iteration is more readable.
