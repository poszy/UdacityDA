#!/usr/bin/python


class Node(object):

    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self,left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

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
