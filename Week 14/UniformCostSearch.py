#!/usr/bin/python

"""
This algorithm can also be called Cheapest First Search
is guaranteed to find the path with the cheapest total cost

Start off in the start state , pop that empty state off, move it from the frontier to the explored 
then add the first paths, in this case there is three

We then grab these three paths and chose the path with the cheapest costs, 
then keep adding the paths.

Now this gets tricky when we decide which path gets expanded next,
Even though we initial started off with a small path with the lowest costs, eventually this path added more paths that outweigh the total
cost of paths that were bigger than the first chosen path. so we go back and expand the cheapest path now that we have explored much more paths from our start. 

This process will always repreat, there is not straight forward path, we must keep going back and adding the least costs path every single time. 
When we add paths we take them from the frontier to the explored, when there are paths that intersect ( A-D b-D) we dont have to add them 

Even if we get to destination , we cant terminate the algorithm until all paths arrive at the destination. This is so we can compare them and
arrive at the path with the least costs. 
"""

"""
How does Uniform Cost search work? 

- we start at a start state, then we start expanding ou from there looking at different paths 
- Estimate of the distance from that start state to the goal 


"""
