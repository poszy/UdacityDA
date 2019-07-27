def binary_search(list, item):

    #low and high kep track of which
    # part of the list I am searching
    low = 0
    high = len(list) -1

    # While there is not 1 element
    # remaning, keep searching
    while low <= high:

        # Check the middle element
        mid = (low + high) // 2
        guess = list[mid]

        # Found the Item
        if guess == item:
            return mid

        # If the guess was too high
        if guess > item:
            high = mid -1

        #If the guess was to low
        else:
            low = mid + 1

    #If the item (digit in second parameter) does not exist
    return None
def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
