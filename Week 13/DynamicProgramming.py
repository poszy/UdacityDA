#!/usr/bin/python

# Dynamic Programming, a concept in where you break a huge problem down and solve it in smaller problems
# Memoization: store already computed variables or functions and store them (table) to resuse the computated values, that way you dont have to re-compute them

"""

This simple optimization reduces time complexities from exponential to polynomial.
For example, if we write simple recursive solution for Fibonacci Numbers,
we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

"""

## Recursion has an exponential time complexity,
# which becomes worse over time

def fib(n):
  if n<0:
    print("Incorrect Input")

  elif n ==1:
    return 0

  elif n == 2:
    return 1

  else:

    return fib(n-1) + fib(n-2)

print(fib(9))


FibArray = [0,1]
def fib_dynamic(n):

  if n < 0:
    print ("Incorrect input")

  elif n<= len(FibArray):
    return FibArray[n-1]

  else:
    temp_fib = fib_dynamic(n-1) + fib_dynamic(n-2)
    FibArray.append(temp_fib)
    return temp_fib


print(fib_dynamic(9))
