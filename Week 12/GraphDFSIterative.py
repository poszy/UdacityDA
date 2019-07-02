#!/usr/bin/python

class GraphNode():

  def __init__(self, val):
    self.value = val
    self.children = []

  def add_child(self, new_node):
    self.children.append(new_node)

  def remove_child(self, del_node):
    if del_node in self.children:
      self.children.remove(del_node)

class Graph:
  def __init__(self, node_list):
    self.nodes = node_list


  def add_edge(self, node1, node2):
    if (node1 in self.nodes and node2 in self.nodes):
      node1.add_child(node2)
      node2.add_child(node1)

  def del_edge(self, node1, node2):
    if(node1 in self.nodes and node2 in self.nodes):
      node1.remove_child(node2)
      node2.remove_child(node1)

# List with single elemenent
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

#  A List containing 6 individual Lists with a single element
graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )

# An edge is adding one list into another, inside the main graph list
# graph1[ list1[list2]]
# graph1 [nodeG[nodeR]]
# graph1 [nodeR[nodeG]]
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


def dfs_search(root_node, search_value):
  # List to keep track of visited nodes
  visited = []

  #pass in a node
  stack = [root_node]

  while len(stack) > 0:
    current_node = stack.pop()
    visited.append(current_node)

    if current_node.value == search_value:
      return current_node

    for child in current_node.children:
      if child not in visited:
        stack.append(child)



assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')
