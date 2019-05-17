#!/usr/bin/python

# Linked List
## differ from arrays

## Arrays have indexes for next elements and linked list store a refference( object in memory ) to the next element.
## When adding a new element,
## you must delete your reference to the previous reference element, it is good practice to reference the unassigned refference to the new element before assigning
## the first element the reference to the new element.

## Abstract Key Elements
## each linked list is comprised of nodes and each node has two things
## 1) Data or a value we want the node to hold
## 2) a reference to the next node in the list. the addresses in memory can be scattered all throughout memory, they dont need to be contigous ( next to each other) in arrays they are. 
## #) the last element in the list will reference to NONE

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

head = Node(2)
print (head.value)
