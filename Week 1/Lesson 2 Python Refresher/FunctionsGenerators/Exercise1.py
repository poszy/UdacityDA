#!/usr/bin/python


#Create a generator to generate factorials
# We usually say (for example) 5! as "5 factorial", but some people say "5 shriek" or "5 bang"
# 5! = 5 *4 *3 *2 *1 = 120
# https://www.mathsisfun.com/numbers/factorial.html


def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i) # this takes the value of i and n and then n sets it to itself
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i = i + 1 # starts off as 2
        n = output # n = i * n.... = 6

# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120
