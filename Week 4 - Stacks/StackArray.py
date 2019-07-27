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

    def size(self):
      return self.num_elements
    
    def is_empty(self):
      return self.num_elements == 0

    def pop(self):

      #if the stack is empty, set the index to 0
      if self.is_empty():
        self.next_index = 0

        # then return none if there are no items in the stack to pop
        return None

      # if there are items in the stack
      # we need to decrement this, to get the value on top. because self.next_index has no value
      self.next_index = self.next_index -1

      # Decrease the amount of elements present. 
      self.num_elements = self.num_elements - 1

      # return the index that was popped
      return self.arr[self.next_index]

foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
