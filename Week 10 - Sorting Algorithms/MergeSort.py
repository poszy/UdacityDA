#!/usr/bin/python

# Merge Sort, split an array down as much as possible
# This is called divid and conquer
# then we build it back up while we sort and compare along the way

# Merge sort efficiency
# m = size of the array
# the number of comparisions/steps is always one less than the size of m.
# so if m = 6 then the number of steps is 5
# O ((# of comparisons per step) * ( # of steps)
# we are doing roughly n comparisions for log(n) steps
# The complexity is way better than bubble sort
# O (n log(n))  >    O(n^2)
# But the space complexity is worse
# O(n) < O(1)


def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    # TODO
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    # TODO
    merged = []
    left_index  = 0
    right_index = 0

    # Move throught the lists until we have exhasuted one
    while left_index < len(left) and right_index < len(right):

        # If left's item is larger, append rights item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index = right_index + 1
        else: 
            merged.append(left[left_index])
            left_index = left_index + 1

    # Append any leftovers because weve broken from our while loop,
    # we know at least one is empty and the remaing:
    # a) already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered merged list
    return merged
        

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
