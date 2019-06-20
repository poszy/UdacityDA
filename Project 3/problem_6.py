def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_number = ints[0]
    max_number = ints[0]

    for index in ints:
        if ints[index] < min_number:
            min_number = ints[index]

        if ints[index] > max_number:
            max_number = ints[index]

    return(min_number,max_number)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
