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

## Hash Maps:
## Hash maps are on eof the main places i will see hash functinos show up
## You can use keys as inputs to a has function then store the key value pair.
## Since map keys are unique,because they belong to a set. you could use a hash function to give them each
## their own uniqe buckets.
## you can also design a hash function to alllow for collisions.
## In an interview you will be asked to create a hash table to show you understand hashing.
### know the upsides and downsides of designing a hash function
## hash maps are very useful to intergrate into algorithms , because they are essentially constant time lookups

# This is not a good hash function because
# ord(bcda) will return the same value
# this will cause a collision.
# an ideal hash function must be immune from production collisions.
# Keep in mind: we should have different hash functions for differnt types
# keys, [strings, integers]
def hash_function(string):
  hash_code = 0
  for i in string:
    hash_code = hash_code + ord(i)
  return hash_code

hash_code_1 = hash_function("abcd")
print(hash_code_1)


# For string abcde, a very effective function is treating this as a number of prime number base p
# as an example, for number 578, we can represent this number in base 10
## a * p^4 + b * p^3 + c * p^2 + d * p^1 + e * p^0
# We replace each character with its corresponding ASCCI Value
# this is a very popular hash fucntion for strings
# we use prime numbers because they provide  a good distrobution.  the most common prime numbers use for this function are 31 and 27

#Using this algorithm, we can get a coresponding integer value for each string key and store it in the array.

## Note: an array used with this purpose and algorithm is called a bucket Array, there is nothing special about the array, thats just what it is called.
## each entry in this array is called a bucket and each index is called a bucket index.

# Lets do this to the class

class HashMap:

  def __init__(self, initial_size=10):
    self.bucket_array = [None for _ in range (initial_size)]
    self.p = 37
    self.num_entries = 0

  def put(self,key,value):
    pass

  def get(self,key):
    pass

  def get_bucket_index(self,key):
    return self.get_hash_code(key)

  def get_hash_code(self,key):
    key = str(key)
    num_buckets = len(self.bucket_array)
    current_coefficient = 1
    hash_code = 0

    for character in key:
      hash_code = hash_code + ord(character) * current_coefficient

      current_coefficient = current_coefficient * self.p
      current_coefficient = current_coefficient

    return hash_code


hash_map = HashMap()
bucket_index = hash_map.get_bucket_index("abcd")
print(bucket_index)
