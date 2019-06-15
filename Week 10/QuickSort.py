#!/usr/bin/python

# In many cases quick sort is one of the most efficient sorting algorithms.

# 1) pick one element in the array at random
# 2) move all values larger than it above it, and all values below it, lower than it.
## The value that we pick is called a PIVOT
## We do this recursivley picking a pivot and sorthem them similalry
# The convention is the pick the element at the end of the list as the pivot

# Lets pick 2 as the pivot
# [8,3,1,7,0,10,2]
# Lets compare 2 > 8
# Lets switch 8 and 2
# to do this, we need to move 10 to the first element
# then we can place 8 at the last element and move 2 to the second to last element
# we get
# [10,3,1,7,0,2,8]

# Now we keep comparing with the pivot, which is 2.
# lets compare 10 > 2 ( the first element will always be on the left)
# to do this we need to move 0 to the first element.
# then we can place 10 to the second to last element
# and move 2 to the third to last element
# we get
# [0,3,1,7,2,10,8]
## Note the number infront of the pivot will always be sent to the front of the list.

## we always check if the first element is smaller than the pivot,
## if it is, then we start comparing against the second element
## lets compare 2 < 3
## shove 3 behind 2
## push the number 7 to the second element ( position of element being compared)
## and move the pivot 2 into the 7 position
## we get
## [0,7,1,2,3,10,8]

# compare 2 against the second element
# 2>7
# switch pivot with 7
# to do so, we need to make room
# push pivot forward
# push number in front of pivot forward
# we get 
# [0,1,2,7,3,10,8]


# Note we should always compare the pivot to both sides of the array before swapping element posisions
# once the piviot is greater than the element on the left and less than the element on the right
# we change pivot to the last element in the array again
# in this case it is 8
# we keep doing this until the list is sorted

# Quick sort efficienty is complicated
# Best case : O(n log(n))
# Worst case : O(n^2)
# average case is O(n log(n))
# Space complexity is O(1) as quick sort is an inplace

                                                                                                                                                   
items = [8, 3, 1, 7, 0, 10, 2]

pivot_index = len(items) -1
pivot_value = items[pivot_index]
