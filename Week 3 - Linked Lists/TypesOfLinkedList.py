#!/usr/bin/python

# Three types of list
# singly-linked, doubly-linked, cicular lists

# Usually you'll want to create a LinkedList class as a wrapper for the nodes themselves and to provide common methods that operate on the list. For example you can implement an append method that adds a value to the end of the list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

1        return out_list

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

#print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")


class DoubleNode:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.previous = None

# Make sure to track the tail and head of this linked list
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    if self.head is None:
      self.head = DoubleNode(value)
      self.tail = self.head

      return

        # Move to the tail (the last node)
    self.tail.next = DoubleNode(value)
    self.tail.next.previous = self.tail
    self.tail = self.tail.next

    return




linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
