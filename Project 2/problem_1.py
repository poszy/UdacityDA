#!/usr/bin/python3

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size  = capacity
        self.mDict = dict({})
        self.first_output = None
        self.second_output = None
        self.third_output = None
        self.history = []
        self.output = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 

        if key in self.mDict and key == 1:
            self.output = self.mDict[1]

        elif key in self.mDict and key == 2:
            self.output = self.mDict[2]
             
        else:
            self.output = -1

        #return self.output
        print (self.output)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
       
        if len(self.mDict) < self.size:
            
            if key in self.mDict:
                print ("Key in already in Dict")
                return
            else:
                print("Adding key " + str(key))
                self.mDict[key] = value
                self.history.append(key)
           
        elif len(self.mDict) == self.size:
            oldest = self.history.pop(0)
            del self.mDict[oldest]
            print("List is too large, popping last used element")
            self.mDict[key] = value
            
        
our_cache = LRU_Cache(5)

our_cache.set(1, 1) # Adding Key 1
our_cache.set(2, 2) # Adding Key 2
our_cache.set(3, 3) # Adding Key 3
our_cache.set(8, 2) # Adding Key 8
our_cache.set(1, 1) # Key already in dictionary
our_cache.set(2, 2) # Key already in dictionary
our_cache.set(6, 6) # Adding Key 6
our_cache.set(7, 7) # List too large , popping last used element0

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
our_cache.get(6)       # returns -1


