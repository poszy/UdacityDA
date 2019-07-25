def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_number = ints[0]
    max_number = ints[0]

    if len(ints) > 10:
      print("List is too large")
      return None

    for index in ints:

      if ints[index] < 0 :
        print ("Enter a valid positive integer")
        break

      if ints[index] < min_number:
        min_number = ints[index]

      if ints[index] > max_number:
        max_number = ints[index]

    return(min_number,max_number)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

l2 = [-1,0,3,4,5,-1,4,6,-9,9]  # a list containing 0 - 9
random.shuffle(l2)

l3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # a list containing 0 - 9
random.shuffle(l3)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # shold print pass
print ("Pass" if ((0, 9) == get_min_max(l2)) else "Fail") # Should print Fail
print ("Pass" if ((0, 9) == get_min_max(l3)) else "Fail") # Should print Fail
