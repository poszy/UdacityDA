#!/usr/bin/python
import sys

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


def huffman_frequency(string):

  frequency_holder = {}
  frequency_key = []

  # Pull in string, check each char , if char does not exists
  # add key to dict
  for character in string:
    if character not in frequency_holder.keys():
      
      frequency_holder[character] = 1

  # Other wise, add +1 to its value
    else:
      frequency_holder[character] = frequency_holder[character] + 1


  # Sort the dictionary based on # of char appearances
  frequency_holder = sorted(frequency_holder.items(), key=lambda x: x[1])
  return frequency_holder
  

def huffman_build_tree(frequency_holder):
 
  while len(frequency_holder) > 1 :

    # Grab the least two occururing frequencies
    least_freq = tuple(frequency_holder[0:2])

    # Grab remaining frequecies
    remaining_freq = frequency_holder[2:]

    # combine the least two occurening frequencies
    # add them to a branch
    combined_freq = least_freq[0][0] + least_freq[1][0]

    # add the combined branced to the end
    frequency_holder = remaining_freq + [combined_freq, least_freq]
    frequency_holder.sort(key=lambda t: t[0])

  return False

    

  #print (remaining_freq)
   

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    #a_great_sentence = "The bird is the word"

    #print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #print ("The content of the data is: {}\n".format(a_great_sentence))

    #encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))

frequency_holder = huffman_frequency("tthisss")
huffman_build_tree(frequency_holder)
