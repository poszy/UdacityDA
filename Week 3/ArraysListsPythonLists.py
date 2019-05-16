#!/usr/bin/python

## Arrays
# Arrays are the most common implementatin of lists.
# there is a collections of items
# The Items have an order to them
# Arrays of indexes and lists do not.
# adding elements to an array can be slow because one needs to

# Deleting is problematic as well because you need to search for the item, if the array is huge, it will be slow.
# deleting an array with a se
# 1) add the element to the desired position and then shove everything that was to the right or left of it 1 posistion
# This is linear time or big O N this can be problematic if the array is huge. 
# Deletion has a similar problem deleting element with size 0,1,2,3 will now contain an array size 0,1,2. you simply cant get the 5th element in the array


# Arrays are stored in memeory when an array is created it always given some initial size.
# 1) arrays are contiguous meaning that they are all next to one another in memory.
# 2) Another key characteristic of an array is that all of the elements are the same size.
### Because all of the elements are 1) next to one another and 2) the same size, this means that if we know the location of the first element, we can calculate the location of any other element.
### For example, if the first element in the array is at memory location 00 and the elements are 24 bytes,
### then the next element would be at location 00 + 24 = 24. And the one after that would be at 24 + 24 = 48, and so on.
### Since we can easily calculate the location of any item in the array, we can assign each item an index and use that index to quickly and directly access the item.

## List
# may or may not be next to one another in memory. ( linked list)
# beacause of this we easily cannot simply calculate the address in memoery and thus list to not have indexes.

# Python lists
my_list = ['a','b','c']
print my_list[0]
print my_list[1]
print my_list[2]

# Lists in python are implemented like arrays and have indexes.
# Python list is essentially implemented like an array (specifically, it behaves like a dynamic array, if you're curious). In particular,
# the elements of a Python list are contiguous in memory, and they can be accessed using an index
# Lists also have pop and append. but are high level and will not be covered in this course.
# Python lists are essentially arrays, but also include additional high-level functionality
