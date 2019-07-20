#!/usr/bin/python

"""
A* search works by always expanding the path that has a minimum value of the function f, which is defined
as the sum of the g and h components
f = g + h

the funciton g of a path is just the path cost

g(path) = path cost
h(path) = h(s) = the h value of the sate, which is the final state of the path || us equal to the estimate distance to the goal
h = hueristic : straight line distate between the state and the goal 


_------------- F---------------_
(S) ----g ---(X) ------h-------G


A* finds the lowest cost path if:

it depends on the h function

h(s) < true cost

h should never overestimate distance to goal
h is optimistic
h is admissible 
"""
