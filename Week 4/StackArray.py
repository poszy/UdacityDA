#!/usr/bin/python3

class Stack:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]

        # keeps track of where the top of the stack is
        # and what ever item I want to add next 
        self.next_index = 0

        # Keep track of how many elements are in the stack. 
        self.num_elements = 0

    def push(self,data):

        # check to see if the index is currently equal to the length of the array.
        if self.next_index == len (self.arr):
            print("Stack is full. increasing capacity")
            self._handle_stack_capacity_full()

        # get the position inside the array and assign it to the passed value of data
        # since the stack does not have any items at first, it will be assinged to the 0 index
        self.arr[self.next_index] = data

        # now once index 0 has a value, we want to increment the index by 1
        self.next_index = self.next_index + 1

        # and also keep track of the number of elements in the array. 
        self.num_elements = self.num_elements + 1

    def _handle_stack_capacity_full(self):

        # temp set array to old array
        old_arr = self.arr

        # increase the size of the array
        self.arr = [0 for _ in range(2* len(old_arr))]

        # enumurate will turn the list into a tuple and
        # grab the index and values from the old_arr
        for index, element in enumurate(old_arr):
            # add the values to the new double length array.
            self.arr[index] = element

foo = Stack()

foo.push('this')

print (foo.arr)
