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

class LinkedListNode:
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.next = None

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
    # bucket index is = to get_hash_code(key)
    bucket_index = self.get_bucket_index(key)

    # new_node has values passed in from parameters
    new_node = LinkedListNode(key,value)

    # head = this bucket_array with get_hash_code key value
    head = self.bucket_array[bucket_index]

    

    # check if key is already present in the map, and update it's value
    while head is not None:
      if head.key == key:
        head.value = value
        return
      head = head.next
    # key not found in the chain --> create a new entry and place it at the head of the chain
    head = self.bucket_array[bucket_index]
    new_node.next = head
    self.bucket_array[bucket_index] = new_node
    self.num_entries += 1

  def get(self,key):
    bucket_index = self.get_hash_code(key)
    head = self.bucket_array[bucket_index]
    while head is not None:
            if head.key == key:
                return head.value
            head = head.next
    return None

  def get_bucket_index(self,key):
    bucket_index = self.get_hash_code(key)
    return bucket_index

  ## Comporession Function
  # The values for unique objects are huge we cannot create such large arrays
  # So we use another function - compression, to compress these valuse to create arrays of reasonable size

  # A very simple, good and effective compression function can be mod(len(array). the modulo operator % returns the remainder
  # of one number when divided by other
  # if we have arrray of size 10, we can be sure that modulo of any number with 10 will be less that 10, allowing it to fit into our bucket array

  # Because of modulo operator, we can write the logic in get_hash_code() instead of writting a compress function.

  ## get_hash_code() function is satisfactory with the implementation of a compression function. but we are prone to collisions, because of compression
  ## We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095. Even though the hash codes are different in this case,
  ## the bucket index will be same because of the way we have implemented our compression function. Such scenarios where multiple entries want to go to the same bucket are very common.
  ## So, we introduce some logic to handle collisions

  ## There are two popular ways in which we can handle collisions.
  ## 1) closed addressing or separate chaining
  ## Closed addressing a is a clever technique where we use the same bucket to store multiple objects, the bucket in this case will store a linked list of key-value pairs.
  ## every bucket has its own separate chain of linked list nodes. 
  ## 2) open addressing
  ## in open addressing we do the following,
  ### if, after getting the bucket index, the bucket is empty, we store the object in that particular bucket.
  ### if the bucket is not empty, we find an alternate bucket index byu using another function which modifies the current hash code to gfive a new code. 
  
  def get_hash_code(self,key):
    key = str(key)
    num_buckets = len(self.bucket_array)
    current_coefficient = 1
    hash_code = 0

    for character in key:
      hash_code = hash_code + ord(character) * current_coefficient

      # Compress hash_code
      hash_code = hash_code % num_buckets
      current_coefficient = current_coefficient * self.p

      # Compress coefficient
      current_coefficient = current_coefficient % num_buckets

    # Compress before returning 
    return hash_code % num_buckets

  def size(self):
    return self.num_entries

hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))
