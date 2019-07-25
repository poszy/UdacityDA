#!/usr/bin/python

import hashlib
import datetime
import time


class MainBlock:

  def __init__(self, data, previous_hash):
    self.timestamp = self.calc_time()
    self.data = data
    self.previous_hash = previous_hash # NEXT
    self.hash = self.calc_hash()

  def calc_hash(self):
    sha = hashlib.sha256()
    hashed_string = str(self.timestamp)
    hash_str = hashed_string.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

  def calc_time(self):
    return (datetime.datetime.now().time())

class BlockNode:
  def __init__(self, MainBlock):
    self.value = MainBlock
    self.next = None

class LinkedListBlock:

  def __init__(self):
    self.head = None
    self.tail = None

  def prepend(self, data):

    if self.head is None:
      createBlock = MainBlock(data, None)
      self.head = BlockNode(createBlock)
      self.tail = self.head

    else:
      createBlock = MainBlock( data, self.tail.value.hash)
      self.tail.next = BlockNode(createBlock)
      self.tail = self.tail.next

def create_block(BlockChainName):

  BlockChainName = LinkedListBlock()
  BlockChainName.prepend("According to my navi-computer, the--")
  BlockChainName.prepend("Shut up! Just shut up you idiot!")
  BlockChainName.prepend("Sheriff, this is no time to panic.")
  BlockChainName.prepend("This is the perfect time to panic! I'm lost, Andy is gone, they're gonna move into their house in two days and it's all your fault!")

  BlockChainName.prepend("MY-- my fault?! If you hadn't pushed me out of the window in the first place--")
  BlockChainName.prepend("OHH yeah?! Well if YOU hadn't shown up inside your stupid little cardboard spaceship and taken away everything that was important to me--")
  BlockChainName.prepend("Don't talk to me about importance! Because of you, the security of this entire universe is in jeopardy!")
  BlockChainName.prepend("WHAT?! What are you talking about?! ")
  BlockChainName.prepend("Right now, poised at the edge of the galaxy, Emperor Zurg has been secretly building a weapon with the destructive capacity to annihilate an entire planet! I alone have information that reveals this weapon's only weakness. And you my friend, are responsible for d2elayin' my rendezous with Star Command! ")
  BlockChainName.prepend("YOU-ARE-A-TOOOOOYY!!! You aren't the real Buzz Lightyear, you're-- oh, you're an action figure! You are a child's play thing!")
  BlockChainName.prepend("You are a sad, strange little man. And you have my pity. Farewell.")
  BlockChainName.prepend("Oh, yeah?! Well, good riddance, ya looney! [Muttering to himself] Rendezous with Star Command!")

  BlockNode = BlockChainName.head
  BlockIndexCount = 1

  while BlockNode is not None:
    blockNode = BlockNode.value
    print (BlockIndexCount)
    print (blockNode.previous_hash)
    print (blockNode.hash)
    print (blockNode.timestamp)
    print (blockNode.data)
    BlockNode  = BlockNode.next
    BlockIndexCount = BlockIndexCount + 1

# Test Case 1
create_block("BlockChainName")

# Test Case 2
create_block("SecondBlockChain")

# Test Case 3
create_block("BlockChainTheThird")

