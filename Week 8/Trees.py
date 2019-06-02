#!/usr/bin/python


class Node:
  def __init__(self, value):
    self.right = None
    self.left = None
    self.value = None

  def set_value(self, value):
    self.value = value

  def set_left_child(self, node):
    self.left = node

  def set_right_child(self, node):
    self.right = node

  def has_right_child(self):
    return self.right != None

  def has_left_child(self):
    return self.right != None
  def get_value():
    return self.value

  def get_left_child(self):
    return self.left

  def get_right_child(self):
    return self.right

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")
