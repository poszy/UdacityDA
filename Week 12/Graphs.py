#!/usr/bin/python

# Graph is to show how different things are connected with each other
# A graph is also called a network

# When a graph starts its known as a
# Node or Vertex(vertices)
# The end are called "edges"
# a "Tree" is a specific type of graph
# Graphs do not have root nodes
# Edges can store data, these edges are the lines that connected each "node"

# Nodes contain data about the node , such as a persons, persons age, height etc..
# Edges contain information about the streght of a connection between the nodes,
# eg, edge contains information that each node connected to each other have met or lived in the same city.

##### Additional properties of graphs
# Edges can have a direction
# - the relationship between two nodes only applies one way and not the other
# - This is called a "directed graph"

# Undirected graph
# an undirected graph has edges with no sense of direction.

## Cycles
# graphs can have cybcels but trees cant.
# a cycle is when you go from node A to node C and back from node C to node A
## graphs and cycles can be really dangerous when you are describing algorithms
## Cycles can cause infiinite loops
## Often you need to make sure the graph you are taking in as input is acyclic,
## meaning it does not have a cycle
# once common type of a asyclic is a DAG
## Directed -> Asyclic [x] -> Graph ( a directed graph with no cycles)

## Connectivity "Graph Theory"

## Disconected graph
## has some vertex that cant be reached by the other graph
## This could be a vertex off to the side with no edges,
## disconected "components" are two nodes that are connected but are off to the sides with no additional edges connected

## Connected graph has no disconnected vertices

# "connectivity" is a metric to drescribe the connections of a graph as a whole. 

## Graph representations
# if using OOP, you could create a vertex and edge objects and give them properties
# such as name, strength, id number.
# Operations that traverse graphs can be more inconvienint if you need to traverse through these objects

## Edge List
# a list of edges.
# the edges themselves are represented byu a list of two elements.
# this is also called a two dimensional array

# Adjecency list is anotehr way to represent tedges in a graph
# In an adjecency list, your vertices normally have an id number that corresponsds to an index an in array.

# in the array, each space is used to store a list of nodes


# Adjecency Matrix
# is a two d array the list inside are all the same length
# this can also be called a rectangular array. 


## Graph Traversal
# ! Graph traversal and graph search are basically the same thing.
# In a traversal you look at every element and in a search you just stop traversing when you fint he element you are looking for.
# Since there are not root nodes in a graph, you can start anywhere in teh graph. any node.

# DFS: looking at every element in the graph until there is not anymore nodes
# First, mark the ndoe you seleced as seen, commonly implemented with this is a stack.
# Next, pick another node and mark it as seen.
# pop the nodes off of the stack when you already seen the node, just go back to your origional stack

# Another common DFS implementation uses recursion and not a stack
# you visit every node until you reach the node you origionall started with,
# the run time complexity is O ( E + V )

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)
