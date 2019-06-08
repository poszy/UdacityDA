#!/usr/bin/python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        print ("Removing next value in list = " + str(node.value))
        return(node.value)

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

def union(llist, llistt):
    # Your Solution Here
    l1 = llist.to_list()
    l2 = llistt.to_list()
    l3 = l1 + l2
    masterList = []
    print (sorted(l1))
    print (sorted(l2))
    print (sorted(l3))

    for character in l3:
        if character not in masterList:
            masterList.append(character)
    print("_________________________________________")
    return sorted(masterList)
    
    

    
    

def intersection(llist_1, llist_2):
    
    pass

    
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
#print (intersection(linked_list_3,linked_list_4))
