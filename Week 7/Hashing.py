#!/usr/bin/python

#Hash functions grab a value and store them to be easily retrieved.
# Value ---> Hash function ----> Hash value ( index of array)

# A collision is when a hash function spits out two identicle hash values at an index.
# there are two main ways to fix this,
##  1) Change the value of the hash function
##  2) store a list that contains all values hashed at that spot. these are alled buckets.
### buckets store multiple values or a collection in each bucket.

## Are solutions 1 & 2 Helpful? keep in mind these have tradeoffs
## 1) you can maintain constant lookup time but using a bigger value for the has functions will require a bigger array
## and cause for more space to store these value. This will increase the complexity in terms of both size and time

## 2) storing values in everybucket and still iterating through a list, in worst case, it turns into O(m)
