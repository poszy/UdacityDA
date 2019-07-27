#!/usr/bin/python

from collections import deque

# this code makes the tree that we'll traverse
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
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self,new_value):
       new_node = Node(new_value)
       node = self.get_root()

       if node == None:
           self.root = new_node
           return

       while(True):
           # node = root
           # new_node = Node(VALUE_FROM_PARAMATER)
           # This will return
           # 0 if root value and value from paramater are equal
           # -1 if value from paramater is less that root value. ADD LEFT
           # 1 if value from paramater is greater than root value. ADD RIGHT
           comparison = self.compare(node,new_node)

           # Override the duplicate,
           # Set the node ( with root value) == value from node( with parameter value)
           if comparison == 0:
               node.set_value(new_node.get_value)
               break # override node and stop looping
           elif comparison == -1:
               # go left
               # if node has a left value (banana) set the node equal to this value
               if node.has_left_child():
                   node = node.get_left_child
               # if its empty, set the nodes value = value from paramater
               else:
                   node.set_left_child(new_node)

           else:
               # comparison == 1
               # if Cherry exists, set the node to cherry
               if node.has_right_child():
                   node = node.get_right_child()
                   
               # if its empty, set the value from the paramater
               else:
                   node.set_right_child(new_node)
                   break # insert node, soo stop looping

               
    """
    define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self,value):
        pass
                    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1


    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self, new_value):
       new_node = Node(new_value)
       node = self.get_root()

       if node == None:
           self.root = new_node
           return

       while(True):
           # node = root
           # new_node = Node(VALUE_FROM_PARAMATER)
           # This will return
           # 0 if root value and value from paramater are equal
           # -1 if value from paramater is less that root value. ADD LEFT
           # 1 if value from paramater is greater than root value. ADD RIGHT
           comparison = self.compare(node, new_node)

           # Override the duplicate,
           # Set the node ( with root value) == value from node( with parameter value)
           if comparison == 0:
               node.set_value(new_node.get_value())
               break # override node and stop looping
           elif comparison == -1:
               # go left
               # if node has a left value (banana) set the node equal to this value
               if node.has_left_child():
                   node = node.get_left_child()
               # if its empty, set the nodes value = value from paramater
               else:
                   node.set_left_child(new_node)

           else:
               # comparison == 1
               # if Cherry exists, set the node to cherry
               if node.has_right_child():
                   node = node.get_right_child()
                   
               # if its empty, set the value from the paramater
               else:
                   node.set_right_child(new_node)
                   break # insert node, soo stop looping

               
    """
    define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self, value):

        # If there is not a root value
        # set the parameter value to the root
        if self.get_root() == None:
            self.set_root(value)

            return
        #Otherwise, use recursion to insert the node
        self.insert_recursively(self.get_root(), Node(value))


    def insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)

        if comparison == 0:
            node.set_value(new_node.get_value())
            
        elif comparison == -1:
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else:
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)
    
    def insert(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
                    
    """
    implement search
    """
    def search(self,value):
        node = self.get_root()
        a_node = Node(value)

        while (True):
            comparison = self.compare(node, a_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
                    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s

tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)



tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)


tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)