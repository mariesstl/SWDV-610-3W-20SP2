# Implement a queue using linked lists.
# Add to bottom and remove from top - FIFO
# enqueue = add, dequeue = remove
# Base code for this was taken from Problem Solving with Algorithms
# and Data Structures using Python by By Brad Miller and David Ranum, Luther College
# 4.12. Implementing a Queue in Python. The code was written assuming a list object.
# I have modified the code to work with a linked list.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class UnorderedListQueue:

    def __init__(self):
        self.head = None
        self.rear = None
        
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self,item):
        #add first item to the head. Add every other item to the bottom.
        if self.isEmpty():
            temp = Node(item)
            self.head = temp
            self.rear = temp
        else:
            temp = Node(item)
            self.rear.setNext(temp)
            self.rear = temp
       
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
    
           
    def dequeue(self):
        # remove an item from the top
        if self.isEmpty():
            return None
        else:
            top = self.head
            self.head = top.getNext()
            return top.data

    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data      

    #This was added only for testing purposes.
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.getNext() 

      
def main():
    myUnorderedList = UnorderedListQueue()
    print('Empty?: ', myUnorderedList.isEmpty()) #It is, you know. We just created it.
    print("dequeue", myUnorderedList.dequeue()) #Test for dequeue of empty list. Will return None.
    print("enqueue 31")
    myUnorderedList.enqueue(31)
    print('After enqueue size?', myUnorderedList.size())
    print('Head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print("enqueue 55")
    myUnorderedList.enqueue(55)
    print('Size?', myUnorderedList.size())
    print('Head?', myUnorderedList.peek())
    print("enqueue 17")
    myUnorderedList.enqueue(17)
    print('Print List:')
    myUnorderedList.printList()
    print('Empty?: ', myUnorderedList.isEmpty())
    print("enqueue 89")
    myUnorderedList.enqueue(89)
    print("enqueue 2")
    myUnorderedList.enqueue(2)
    print("enqueue 29")
    myUnorderedList.enqueue(29)
    print('Size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()    
    print('55?', myUnorderedList.search(55))
    print('17?', myUnorderedList.search(17))
    print('100?',myUnorderedList.search(100))
    print("enqueue 100")
    myUnorderedList.enqueue(100)
    print('100?',myUnorderedList.search(100))
    print('Print List:')
    myUnorderedList.printList()  
    print('head?', myUnorderedList.peek())
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()  
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we dequeue?',myUnorderedList.dequeue())
    print('After dequeue size?', myUnorderedList.size())
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList() 
main()