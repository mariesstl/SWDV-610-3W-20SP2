# Implement a deque using linked lists
# Can add or remove from front or rear
# Will take data from the back of the list for the first time in these exercises.
# Base code for this was taken from Problem Solving with Algorithms
# and Data Structures using Python by By Brad Miller and David Ranum, Luther College
# 4.17. Implementing a Deque in Python. The code was written assuming a list object.
# I have modified the code to work with a linked list.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.previous = None
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous

    def setData(self,newdata):
        self.data = newdata
        
    def setPrevious(self,newprev):
        self.previous = newprev

    def setNext(self,newnext):
        self.next = newnext
        
class UnorderedListDeque:

    def __init__(self):
        self.head = None
        self.rear = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def addFront(self, item):
        if self.isEmpty():
            temp = Node(item)
            self.head = temp
            self.rear = temp
        else:
            temp = Node(item)
            temp.setNext(self.head)
            self.head.setPrevious(temp)
            self.head = temp
        
    def removeFront(self):
        if self.isEmpty():
            return None
        else:
            top = self.head
            self.head = top.getNext()
            if self.head == None: #If you are at the end of the list, set rear to none.
                self.rear = None
            else:
                self.head.setPrevious(None)
            return top.data
    
    def addRear(self,item):
        #add to the end of the list.
        if self.isEmpty():
            temp = Node(item)
            self.head = temp
            self.rear = temp
        else:
            temp = Node(item)
            self.rear.setNext(temp)
            temp.setPrevious(self.rear)
            self.rear = temp            
  
    def removeRear(self):
        if self.isEmpty():
            return None
        else:
            bottom = self.rear
            self.rear = bottom.getPrevious()
            if self.rear == None: #If you are at the end of the list, set head to none.
                self.head = None
            else:
                self.rear.setNext(None)
            return bottom.data
       
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found   
     
 
    def peekFront(self):
        if self.isEmpty():
            return None
        return self.head.data        

    def peekRear(self):
        if self.isEmpty():
            return None
        return self.rear.data
    
    #This was added only for testing purposes.        
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.getNext()
      
def main():
    myUnorderedList = UnorderedListDeque()
    print('Empty?: ', myUnorderedList.isEmpty()) #It is, you know. We just created it.
    print('try to remove front', myUnorderedList.removeFront()) #Test for remove front of empty list. Will return None.
    print("add rear 31")
    myUnorderedList.addRear(31)
    print('Peek Front',myUnorderedList.peekFront())
    print('Peek Rear', myUnorderedList.peekRear())    
    print('After add rear size?', myUnorderedList.size())
    print("add front 55")
    myUnorderedList.addFront(55)
    print('Peek Front',myUnorderedList.peekFront())
    print('Peek Rear', myUnorderedList.peekRear())
    print('Print List:')
    myUnorderedList.printList()
    print('Size?', myUnorderedList.size())
    print("add rear 17")
    myUnorderedList.addRear(17)
    print('Empty?: ', myUnorderedList.isEmpty())
    print('Peek Front',myUnorderedList.peekFront())
    print('Peek Rear', myUnorderedList.peekRear())
    print('Print List:')
    myUnorderedList.printList()
    print("add front 2")
    myUnorderedList.addFront(2)
    print("add front 29")
    myUnorderedList.addFront(29)
    print('Peek Front',myUnorderedList.peekFront())
    print('Peek Rear', myUnorderedList.peekRear())  
    print('Size?', myUnorderedList.size())
    print('55?', myUnorderedList.search(55))
    print('17?', myUnorderedList.search(17))
    print('Print List:')
    myUnorderedList.printList()
    print('100?',myUnorderedList.search(100))
    print("add rear 100")
    myUnorderedList.addRear(100)
    print('100?',myUnorderedList.search(100))
    print('Peek Front',myUnorderedList.peekFront())
    print('Peek Rear', myUnorderedList.peekRear())
    print('Print List:')
    myUnorderedList.printList()
    print('Remove Front')
    myUnorderedList.removeFront()    
    print('Print List:')
    myUnorderedList.printList()
    print('Remove Rear')
    myUnorderedList.removeRear()    
    print('Print List:')
    myUnorderedList.printList()
    print('Remove Front')
    myUnorderedList.removeFront()    
    print('Print List:')
    myUnorderedList.printList()
    print('Remove Rear')
    myUnorderedList.removeRear()    
    print('Print List:')
    myUnorderedList.printList()
    print('Remove Front')
    myUnorderedList.removeFront()    
    print('Print List:')
    myUnorderedList.printList()
#     print('Remove Front')
#     myUnorderedList.removeFront()    
    print('Remove Rear')
    myUnorderedList.removeRear()
    print('Print List:')
    myUnorderedList.printList() 
main()
