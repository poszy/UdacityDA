#!/usr/bin/python

import hashlib
import datetime

class BlockChainNode:
  def __init__(self, data, previous_hash):
    self.timestamp = self.calc_time()
    self.data = data
    self.previous_hash = previous_hash # NEXT
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = "We are going to encode this string of data!".encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

  def calc_time(self):

    #print  (datetime.datetime.now())
    return (datetime.datetime.now().time())

class LinkedList:

  def __init__(self):
    self.head = None

  def prepend(self, data, previous_hash):

    if self.head is None:
      self.head = BlockChainNode(data, previous_hash)
      print (self.head.previous_hash)
      return

    else:
      new_head = BlockChainNode( data, previous_hash)
      new_head.next = self.head
      self.head = new_head


  def append(self, data, previous_hash):
    if self.head is None:

      self.head = BlockChainNode(data, previous_hash)

      print(self.head.data)

      return

    node = self.head
    while node.next:
      node = node.next

    node.next = BlockChainNode(data, previous_hash)


  def to_list(self):
    output = []

    node = self.head
    while node:
      output.append(str(node.timestamp) + str(node.data) + str(node.previous_hash))
      node = node.next

    print (output)

ll = LinkedList()

a = "this is a hash"
b = "sadsadsa"
#b = ll.calc_hash("b")
#c = ll.calc_hash("c")
#d = ll.calc_hash("d")


ll.prepend(" my string " , a)
#ll.prepend("thissadsa",b,"b")
ll.append(" this string " , b )
#ll.append("thasdadsadsadadsadsadis",d,"d")

print(ll.to_list())

#assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
