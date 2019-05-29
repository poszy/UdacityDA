#!/usr/bin/python
## The factorial function is a mathematical function that multiplies a given number, n,
## and all of the whole numbers from n down to 1.
## This is often notated using an exclamation point, as in  4!  
## 4 ! = 4 * 3 * 2 * 1 
## or 4 * 3 * 2 * 1
## more generically,
### n! = n * (n-1) * (n-2) * (n-3)
## if you look at this more closely, you will find that the factorial of any number is the
## product of that number and the factorial of the next smallest number
### n! = n * (n-1)

# Notice that this is recursive, meaning that we can solve for the factorial of any given number by first solving for the factorial of the next smallest number,
# and the next smallest number, and the next smallest number, and so on, until we reach 1.

# If we convert this into a python function it would look like this

# factorial(n) = n * factorial(n-1)

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1
    # TODO: Write your recursive factorial function here

    
    return n * factorial(n-1)


print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
