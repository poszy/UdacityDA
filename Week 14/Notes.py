#!/usr/bin/python

"""
What is a problem?
How do we go from city to city ? from a shortest path perspective?


Problems can be broken down into several components

1) initial state ---> S0
- the initial state the agent was in being in a city of arad

2) Actions (s) -> {a1,a2,a3,...}
- a functions, actions that takes a state as input and returns a set of 
- possible actions {a1,a2,a3,...}

3) Result (s,a) -> s'
- a function called results which takes as input a state (s0) and an action 
- (action(s)) and delivers as its output a new state
- if an agen is in the city of of arad, that would be the state
- and takes the action of driving along route E671 torwards Timisora,
- then the result of applying that action in that state would be the new state (s')
- where the agent is in the city of timisoara  

4) GoalTest(s) --> True | False
- takes a state and returns a boolean value of true or false
- telling us if this is state is a goal or not 

5) Path Cost (Si -> si +1 -> si +2)
- takes a path , a sequence of state,actions and transitions and returns a number,
- which is the cost of the path


"""


"""
- Going form Arad to Bucharest is the only state that counts as a goal
- All of the states is known as the State Space
- We navigate the state space by applying Actions
- Actions are specific to each city (length)
- Path: sequences of actions 

- We want to separate the state into three parts
-- ends of the paths,
-- the farthest path that been explored, we call the frontier 
-- 

- States: at every point we want to separate the state out into three parts
-- Frontier
-- Unexplored
-- Explored

- Step Cost inbetween lines of cities 
- Path Cost is the sum of all step costs

"""
