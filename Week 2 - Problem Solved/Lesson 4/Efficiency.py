#!/usr/bin/python

#What is the run time analysis of the following code:
# O(1)

def main(x,y):
    if True:
        z = x + y
        for i in range(10):
            z = z + 1
    return z

# What is the run time analysis of the following code:
# O(N^2)
def main(list_1,list_2):

    count = 0

    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2:
                count+=1

    return count

# What is the simplification of this run time analysis: 4n^2 + 3n + 7 ?
# N^2
