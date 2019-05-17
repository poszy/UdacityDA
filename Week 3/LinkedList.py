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
# Create two new node obj with value = 2,1
#head = Node(2)
#new_node = Node(1)

# assign next value of head obj equal to new node (1) 
#head.next = new_node
## new_node will have its own "value" variable.
#new_node.value = head.next.value because head.next has its own class obj assigned, and that obj has its own variable of value. 
#print (head.value)
# head.next.NEW_NODE.VALUE
#print (head.next.value)

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
#print_linked_list(head)

#print (head.value)
#print (head.next.value)
#print (head.next.next.value)
#print (head.next.next.next.value)
#print (head.next.next.next.next.value)

## Create a linked list based off of iteration/traversing

def create_linked_list(input_list):
    head = None
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        

#input_list = [1, 2, 3, 4, 5, 6]
#head = create_linked_list(input_list)
#test_function(input_list, head)

#input_list = [1]
#head = create_linked_list(input_list)
#test_function(input_list, head)

#input_list = []
#head = create_linked_list(input_list)
#test_function(input_list, head)
