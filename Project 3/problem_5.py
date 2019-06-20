#!/usr/bin/python

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Keep track of positions
    position_zero = 0
    position_two  = len(input_list) - 1
    
    front_index   = 0
    


    while front_index <= position_two:
        
        if input_list[front_index] == 0:
            
            input_list[front_index] = input_list[position_zero]
            input_list[position_zero] = 0

            position_zero = position_zero + 1
            front_index = front_index + 1
            
        elif input_list [front_index] == 2:
            input_list[front_index] = input_list[position_two]
            input_list[position_two] = 2
            position_two = position_two -1

        else:
            front_index = front_index + 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
