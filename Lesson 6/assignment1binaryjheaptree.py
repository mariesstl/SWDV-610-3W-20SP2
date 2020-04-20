# Generate a random list of integers. 
# Show the binary heap tree resulting from inserting the integers on the list
# one at a time.

# The heap order property is as follows: In a heap,
# for every node x with parent p,
# the key in p is smaller than or equal to the key in x. 

# Binary Heap (Min Heap)
# Smallest value goes to the top
# For each node, parent is smallest
# Must fill out each leaf before moving on - left to right

from random import *  

class BinHeap:
    def __init__(self):
# Always begins with 0. Keeps track of list size.
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
# Percolates a new item as far up in the tree as it needs to go
# to maintain min heap properties of smallest as parent
        while i // 2 > 0:  #Uses floor division
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
# Appends a new item to the tree, increments list size and relies on percUp
# to fix any heap property violations
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
# If item is less than its parent,
# then we can swap the item with its parent.
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i) #find end or smallest child value
          if self.heapList[i] > self.heapList[mc]: #if parent is greater, swap.
              print('perDown compare',self.heapList[i] ,self.heapList[mc])
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
              print('percDown',self.heapList)
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize: #find last child to compare with
        print('minchild',self.heapList[i*2])
        return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              print('minchild compare',self.heapList[i*2] ,self.heapList[i*2+1])#compare and return index of smallest
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
# Delete the smalest value. Makes list smaller then uses MinChild and
# percDown to put list back in heap order
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
# Starting with an entire list allows us to build
# the whole heap in O(n) operations
      i = len(alist) // 2 #integer division
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      print('just appended to heap',self.heapList)
      while (i > 0):
          self.percDown(i)
          i = i - 1
   
def main():
    #Create a random list of six integers
    randList = [randrange(1,100) for x in range (0,6)]
    bh = BinHeap()
    print(randList) #print the list before putting in binary heap
    bh.buildHeap(randList)
    print(bh.heapList)#print a list output of the binary heap
    
main()


    