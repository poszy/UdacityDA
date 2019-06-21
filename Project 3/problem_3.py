#!/usr/bin/python

def recursive_binary_search(number_list, left, right, number):

  if left > right:
    return -1

  mid = (left + right) // 2

  if number_list[mid] == number:
    return mid

  if number_list[left] <= number_list[mid]:

    if number >= number_list[left] and number <= number_list[mid]:
      return recursive_binary_search(number_list, left, mid -1, number)
    return recursive_binary_search(number_list, mid + 1, right, number)

  if number >= number_list[mid] and number <= number_list[right]:
    return recursive_binary_search(number_list, mid + 1, right, number)
  return recursive_binary_search(number_list, left, mid - 1, number)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    return recursive_binary_search(input_list, 0, len(input_list)-1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


#multiple = [6, 7, 8, 9, 10, 1, 2, 3, 4]
#print(recursive_binary_search(multiple,0, len(multiple)-1 ,6))

#multiple = [6, 7, 8, 9, 10, 1, 2, 3, 4]
#print(recursive_binary_search(multiple,0,len(multiple)-1 , 3))
