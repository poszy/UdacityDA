#!/usr/bin/python

# String practice.
# In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.


def string_reverser(our_string):
    reversed_string = ''
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    for x in range(len(our_string)):
       reversed_string += our_string[(len(our_string)-1) -x]
       
    return reversed_string
    # TODO: Write your solution here

string_reverser('water')
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
