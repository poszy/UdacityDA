# In-place : an algorithm that sorts the data inside the data structure without having to copy over the data to a new datastructure
# Naive Approach: whatever comes to mind to solve the problem, there will always be a better way.
# ITs important to know the time complexity of sorting algorithms.



# Bubble sort
# Given a list, [7,3,1,,0,8]
# compare the first two elements, if the second element is lower, shift the two elements,
# keep doing this until the list is in order, this will take forever as there are a lot of iterations that must be completed.

# ITeration
# 1 , 2 , 3 ,4
#
# comparisons
# n-1, n-1, n-1, n-1 = (n-1)(n-1) = n2 -2n + 1
# Worst case = O(n^2)
# Average case = O(n^2)
# Best case = O(n)  (the array was already sorted)
# space = O(1) because the algorithm is IN-PLACE, no other datastructure was used, and the array was sorted in place


wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this

    
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

