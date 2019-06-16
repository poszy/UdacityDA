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

# we are sorting in place
# we want to iterate threought the items to the left of our pivot (left_items)
# when they are larger than piviot_value, we will not increment our position trhough  left_items, but isntead change pivot_index. well know were done this
# pass when pivot_index and left_items are index are equal. 

pivot_index = len(items) -1
pivot_value = items[pivot_index]

left_index = 0


while (pivot_index != left_index):
    item = items[left_index]

    # item = items[0]
    # pivot_value = 10
    if item <= pivot_value:
        left_index = left_index + 1
        continue

    # Place the item before the pivot at the left_index
    # left index becomes 0
    items[left_index] = items[pivot_index -1]

    # Shift Pivot one to the left
    items[pivot_index -1] = pivot_value

    # place item at pivots previous location
    items[pivot_index] = item

    # update pivot index
    pivot_index = pivot_index -1

print(items)

# When this loop terminates we know everything to the left of our pivot, is less than the pivot
# and everything in the right is greater than our pivot.

def sort_a_little_bit(items):
    left_index = 0
    pivot_index = len(items) -1
    pivot_value = items[pivot_index]

    while(pivot_index != left_index):
        item = items[left_index] # value is 0 index 0

        # if 0 is less than or equal to 10
        if item <= pivot_value: # first pivot value is 10
            # the index increments by 1
            
            left_index = left_index + 1
            # left index = 1
            continue
        # get the second element index in the list (3)
        # and assign it the value of the third second to last element (0)
        items[left_index] = items[pivot_index -1]

        # get the third index to last element in the array and shove it into
        # previously (0), shove in pivot value of 10, essentially moving 10 into the third to last element
        items[pivot_index -1] = pivot_value

        # set the second to last index and set the value equal to 0 
        items[pivot_index] = item
        pivot_index = pivot_index - 1
        
items = [8, 3, 1, 7, 0, 10, 2]
sort_a_little_bit(items)
print(items)

# We want our function to become recursive
# we want to take the value from our first iteration and act on it
# to do this, we need to communicate the final pivot_index value
# we take this value , and start to mark off segments of the list
# and have our function operate on less than the entire list.items
# so lets change the function to accept the indeices it should stay within, and return the pivot_index


def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

items = [8, 3, 1, 7, 0, 10, 2]
pivot_index = sort_a_little_bit(items, 0, len(items) - 1)
print(items)
print('pivot index %d' % pivot_index)

# Now we will make this recursive.
# we need to know a way to confirm we are done.
# we wil use the indices to see if they demark a list of more than one item.
# if the demarked sublist is 0 or 1 item, we know its already sorted.
def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)
