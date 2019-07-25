from math import sqrt

def shortest_path(M, start, goal):
    
    frontier = set([start])
    front_dict = {}
    searched = set()
    
 
    current_position = M.intersections
    M = M.roads
    nodes = len(M)
    
    g_cost = [40 for _ in range(nodes)]
    g_cost[start] = 0.0
    
    f_cost = [40 for _ in range(nodes)]
    f_cost[start] = distance(start, goal, current_position)

    while frontier:
        
        current = searched_node(frontier, f_cost)
        
        if current == goal:
            return frontiers(front_dict, current, start) 

        frontier.remove(current)   
        searched.add(current)
        neighbor = M[current]

        for n in neighbor:
            current_g_cost = g_cost[current] + distance(current, n, current_position)
            if n not in searched or current_g_cost < g_cost[n]:
                g_cost[n] = current_g_cost
                f_cost[n] = current_g_cost + distance(goal, n, current_position)
                front_dict[n] = current
                frontier.add(n)
                searched.add(n)

    
    
def distance(start, goal, position):

    start_node1, start_node2 = position[start]

    goal_node1,goal_node2 = position[goal]

    return sqrt( (goal_node1 - start_node1) **2 + (goal_node2 - start_node2) **2 )



def frontiers(frontier, current, begining_start):

    current_path = []
    
    while current != begining_start:
        current_path.insert(0, current)
        current = frontier[current]
    
    current_path.insert(0, begining_start)
    return current_path


def searched_node(frontier, cost):
 
    index = None   
    min_cost = 999999  
    
    for i in frontier:
        f = cost[i]
        
        if f < min_cost:
            index = i
            min_cost = f
            
    return index