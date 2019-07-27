#!/usr/bin/python

# A Heap is a specific type of tree
# With its own additional rules
## in a heap, elements are arranged in a increasing or decreasing order
## The root element will be the max or min value in the tree
## Binary tree must be a complete tree
## In a heap, 

# Worst: O(n)
# average O(n/2)

# Heapify
# stick the new element in the next open spot in the tree
# then we heapify, heapify is the operation in which we reorder the tree
# since a rule is that our parent elemen is bigger than its child,
# we just need to keep comparing our new elemen with its parent and swapping them when the child is bigger

# Extract operation
# When the root is removed from the tree
# we stick the right most leaf in the root spot
# The compare the root to its children and swap where necessary

# Run time of insert and delete of a heap
# Worst case O(log(n))
# Height of the tree

## Heap Implementation
# heaps are represented as trees, but they are ofter stored ass arrays
# This is possible beacuse each dhilder each parent has two and how many nodes will be at each level ( double each level)

"""
Thus, for a data structure to be called a Heap, it must satisfy both of the above properties.

    It must be a complete binary tree
    It must satisfy the heap order property. If it's a min heap, it must satisfy the heap order property for min heaps. If it's a max heap, it should satisfy the heap order property for max heaps.
    A heap is a data structure with the following two main properties:

    Complete Binary Tree
    Heap Order Property

    Arrays, hashmaps , binary search trees, LinkedList  all will have at least O(n). we are trying to achieve search and delete and insert at O(1).
    to do this we need a heap

"""

# When deleting and inserting a node to the tree of a heap,
# we must make sure it remains a complete binary tree ( tree with all levels having a parent and two childs, except the last level)
# Thus, we know which node to remove and where to insert a new node. Notice that both of these operations do not depend upon values of other nodes.
# Rather, both insert and remove operations on a complete binary tree depend upon the position of the last inserted node. 

"""
Now that we know about a complete binary, let's think about it in terms of Priority Queues. We talked about binary search trees where the complexity for insert and remove operation would be O(log(n)) if the BST is balanced.

In case of a complete binary tree we do not have to worry about whether the tree is balanced or not.

    Max number of nodes in 1st level = 1
    Max number of nodes in 2nd level = 2
    Max number of nodes in 3rd level = 4
    Max number of nodes in 4th level = 8

We see that there is a clear patter here. 

Max number of nodes in hth level = 2(h-1)
Also, we can calculate the max number of nodes from 1st level to hth level = 2^h -1

Similarly, we can calculate the min number of nodes from 1st level to hth level = 2(h-1)

Thus, in a complete binary tree of height h, we can be assured that the number of elements n would be between these two numbers
2^(h-1) <= n <= 2^h -1

We can rewrite the first inequalit in base-2 logarithmic format
log2 (2^(h1-)) <= log2^n
OR
h <= log2 n + 1

# we can do the same for the second equation
log2(n +1) <= log2 2^h
or
log2(n+1) <=h

thus the value of or heigh h is always
log2(n+1) <= h <= log2 n +1

we can see that the height of of our complete binary tree will aways be in the order of O(h) or O(log(n))

so instead of usinga binary search treee we use a complete binary tree, both insert and remove operation wil have time complexity log2N
"""



"""

Heaps for Priority Queues

Let's take a step back and reflect on what we have done.

    We have examined popular data structures and observed their time complexities.
    We have looked at a new data structure called Heap
    We know that Heaps have two properties -

     i. CBT 
     ii. Heap Order Property

    We have looked at what CBT is and what Heap Order Property is

By now, it must have been clear to you that we are going to use Heaps to create our Priority Queues. But are you convinced that heaps are a good structure to create Priority Queues?

Ans.

    Other than Binary Search trees, all other popular data structures seemed to have a time complexity of O(n) for both insertion and removal.

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Binary Search Trees seemed like an effective data structure with average case time complexity of O(log(n) (or O(h)) for both the operations. However, in the worst case, a Binary Search Tree may not be balanced and instead behave like a linked list. In such a case, the time complexity in terms of height would still be O(h) but because the height of the binary search tree will be equal to the number of elements in the tree, the actual time complexity in terms of number of elements n would be O(n).

    The CBT property of Heaps ensures that the tree is always balanced. Therefore, the height h of the tree will always be equal to log(n).

    The Heap Order Property ensures that there is some definite structure to our Complete Binary Tree with respect to the value of the elements. In case of a min-heap, the minimum element will always lie at the root node. Similarly, in case of a maxp-heap, the maximum element will always lie at the root node. In both the cases, every time we insert or remove an element, the time complexity remains O(log(n)).

Therefore, because of the time complexity being O(log(n)), we prefer heaps over other popular data structures to create our Priority Queues.

"""


# Although we call them complete binary trees, and we will always visualize them as binary trees, we never use binary trees to create them.
# Instead, we actually use arrays to create our complete binary trees. 

"""
We can visualize our array like a tree

    0
1      2
34     56
78

Lets think about it, does it satisy the CBT requirement for a heap?
in a complete binary tree, it is mandatory for all levels before the last level to be completely filled.

If we visualize our array in this manner, do we satisfy this property of a CBT? 
All we have to ensure is that we put elements in array indices sequenially i.e. the smaller index first and the larger index next. 
If we do that, we can be assured that all levels before the last level will be completely filled. 


In a CBT, if the last level is not completely filled, the nodes must be filled from left to right.

Again, if we put elements in the array indices sequentially, from smaller index to larger index, we can be assured that if the last level is not filled, it will certainly be filled from left to right.

Thus we can use an array to create our Completer Binary Tree. Although it's an array, we will always visualize it as complete binary tree when talking about heaps.
"""

 #Insert and remove operation in a heap. we will create our heap class with these two operations

"""
Insertion operation in a CBT is quite simple. Because we are using arrays to implement a CBT, we will always insert at the next_index. 
Also, after inserting, we will increment the value of next_index.
However, this isn't enough. We also have to maintain the heap order property. We know that for min-heaps, the parent node is supposed to be smaller than both the child nodes. 

Before talking about the implementation of insert, let's talk about the time complexity of the insert method.

    Putting an element at a particular index in an array takes O(1) time.
    However, in case of heapify, in the worst case we may have to travel from the node that we inserted right to the root node (placed at 0th index in the array). This would take O(h) time. In other words, this would be an O(log(n)) operation.

Thus the time complexity of insert would be O(log(n)).

##### To insert an index


We first inserted our element at the possible index.

Then we compared this element with the parent element and swapped them after finding that our child node was smaller than our parent node. 
And we did this process again. While writing code, we will continue this process until we find a parent which is smaller than the child node. 
Because we are travering the tree upwards while heapifying, this particular process is more accurately called up-heapify.

"""


"""
the time complexity for `remove` is also O(log(n))

""" 

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    
heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
    
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))
