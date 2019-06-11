#!/usr/bin/python
import sys

def huffman_frequency(string):

  frequency_holder = dict()
  frequency_sorted = []

  # Pull in string, check each char, and add to its value.
  for character in string:
      frequency_holder[character] = frequency_holder.get(character,0) + 1

  # Sort the frequency
  frequency_keys = frequency_holder.keys()
  for key in frequency_keys:
      frequency_sorted.append((frequency_holder[key],key))

  frequency_sorted.sort()

  return frequency_sorted

def huffman_build_tree(frequency_holder):

    while len(frequency_holder)>1:
        # Get the last two frequencies
        least_freq =  tuple(frequency_holder[0:2])

        # Get the remaining frequencies on the left
        remaining_freq = frequency_holder[2:]

        # combine the last two frequncies to a tree
        combined_freq = least_freq[0][0] + least_freq[1][0]

        # Get the remaining frequncies and combined them with the other frequncies
        frequency_holder = remaining_freq + [(combined_freq, least_freq)]

        # Sort the frequncies
        frequency_holder.sort(key=lambda t: t[0])

        #print(frequency_holder)
    return frequency_holder[0]


def huffman_trim_tree(huffman_build_tree):

    node_value = huffman_build_tree[1]

    if type(node_value) == type(""):

      return node_value

    else:
        return (huffman_trim_tree(node_value[0]),
                huffman_trim_tree(node_value[1]))

def huffman_set_codes(node, space =''):
    
    global codes
    
    if type(node) == type(""):
        codes[node] = space
    else:
        huffman_set_codes(node[0], space + "0")
        huffman_set_codes(node[1], space + "1")

def huffman_encode_helper(string):
  
    encoder = ""
    
    for character in string :
      
        encoder = encoder + codes[character]

    return encoder

def huffman_decode_helper(huffman_tree, string):
  
    decoder = ""
    node = huffman_tree
    
    for decimal in string :
      
        if decimal == '0' : 
            node = node[0]
            
        else: 
            node = node[1]
            
        if type(node) == type("") :  
            decoder = decoder + node              
            node = huffman_tree
            
    return decoder

def huffman_encoding(string):
    if string == None or string == "":

        return None

    nodes = huffman_frequency(string)
    tree  = huffman_build_tree(nodes)
    trimed_tree = huffman_trim_tree(tree)
    
    if len(trimed_tree) == 1:
        codes[trimed_tree] = "0"
        
    else:
        huffman_set_codes(trimed_tree)
        
    return (huffman_encode_helper(string),trimed_tree)
    

def huffman_decoding(string, huffman_tree):
    if string == None or string == "":
        return None

    return huffman_decode_helper(huffman_tree, string)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print ("________________________________________________________________________________")

    a_great_sentence = "The warriors blew a 3    to one lead"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print ("________________________________________________________________________________")
    a_great_sentence = "Your name is Thurman Merman?"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


