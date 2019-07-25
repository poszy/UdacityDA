#!/usr/bin/python

def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index  = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index = right_index + 1
        else:
            merged.append(left[left_index])
            left_index = left_index + 1
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    a = mergesort(input_list)
    a.reverse()

    l1 = []
    l2 = []

    for i in range(len(a)):

        if i % 2 == 0:
            l1.append(a[i])

        else:
            l2.append(a[i])

    x = int("".join(map(str, l1)))
    y = int("".join(map(str, l2)))
    return  x , y


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
rearrange_digits([4, 6, 2, 5, 9, 8])
