#!/usr/bin/python


"""
Red and Black Tree Rules:


    All nodes have a color
    All nodes have two children (use NULL nodes)
        All NULL nodes are colored black
    If a node is red, its children must be black
    The root node must be black (optional)
        We'll go ahead and implement without this for now
    Every path to its descendant NULL nodes must contain the same number of black nodes

"""


# Similar to our binary search tree implementation, we will define a class for nodes and a class for the tree itself.
# The Node class will need a couple new attributes. It is no longer enough to only know the children, because we need to ask questions during insertion like,
# "what color is my parent's sibling?". So we will add a parent link as well as the color.

class Node():

    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

class RedBlackTree():

    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):

        # Case 1
        # We have just inserted the root node
        # f we're enforcing that the root must be black, we change its
        # color. We are not enforcing this, so we are all done!
        if node.parent == None:
            return

        # Case 2
        # Thinking through this, we can observe the following: We inserted a red node beneath a black node.
        # The new children (the NULL nodes) are black by definition, and our red node replaced a black NULL node.
        # So the number of black nodes for any paths from parents is
        # unchanged. Nothing to do in this case, either
        if node.parent.color == 'black':
            return

        # Case 3
        # The parent and its sibling of the newly inserted node are both red
        # we can flip the color of the parent and its sibling. We know they're both red in this case, which means the grandparent is black.
        # It will also need to flip. At that point we will have a freshly painted red node at the grandparent.
        # At that point, we need to do the same evaluation! If the
        # grandparent turns red, and its sibling is also red, that's case 3
        # again. Guess what that means! Time for more recursion.
        if pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            self.rebalance(grandparent(node))

        # Case 4
        # The newly inserted node has a red parent, but that parent has a
        # black sibling_
        """
        These last cases get more interesting. The criteria above actually govern case 4 and 5. What separates them is if the newly inserted node is on the _inside_ or the _outside_ of the sub tree.
        We define _inside_ and _outside_ like this:

        * inside
        * _EITHER_
        * the new node is a left child of its parent, but its parent is a right child, or
        * the new node is a right child of its parent, but its parent is a left child
        * outside
        * the opposite of inside, the new node and its parent are on the same side of the grandparent

        Case 4 is to handle the _inside_ scenario. In this case, we need to rotate. As we will see, this will not finish balancing the tree, but will now qualify for Case 5.

        We rotate against the inside-ness of the new node. If the new node qualifies for case 4, it needs to move into its parent's spot. If it's on the right of the parent, that's a rotate left.
        If it's on the left of the parent, that's a rotate right.
        """
        gp = grandparent(node)
        if gp.left and node == gp.left.right:
            self.rotate_left(parent(node))
        elif gp.right and node == gp.right.left:
            self.rotate_right(parent(node))

        # Case 5


    def rotate_left(self, node):
                # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p


    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

def search(self, find_val):
    return False

def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)

tree.insert(13)
print_tree(tree.root)
