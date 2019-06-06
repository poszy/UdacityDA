#!/usr/bin/python
import sys


class Node:

  def __init__ (self, character, frequency):
    self.character = character
    self.frequency = frequency
    self.right = None
    self.left  = None

  def __str__(self):
    return str(self.character)
    return str(self.frequency)
    return str(self.right)
    return str(self.left)

    __repr__ = __str__




def huffman_frequency(string):

  frequency_holder = {}
  frequency_per_key = []


  for i in string:

    if i not in frequency_holder.keys():

      frequency_holder[i] = 1

    else:
      frequency_holder[i] = frequency_holder[i] + 1

  i = 0
  for character, frequency in frequency_holder.items():
    frequency_per_key.append(Node(character,frequency))
    print (frequency_per_key[i][i])
    i = i +1

  #return frequency_per_key



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

huffman_frequency("tthisss")
