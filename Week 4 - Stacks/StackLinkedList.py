#!/usr/bin/python3


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class Stack:
    
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0

    def push(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head  = new_node
        else:
            # If there is already a head, push it to next
            new_node.next = self.head
            # set the head to the new node. 
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return
        value = self.head.value
        self.head = self.head.next
        self.num_elements = self.num_elements + 1

        return value 
        

    def size(self):
        
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 0) else "Fail")
        
        
        
