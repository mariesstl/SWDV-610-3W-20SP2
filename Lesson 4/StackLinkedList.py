# Implement a stack using linked lists
# Add to top and remove from top - LIFO
# push = add, pop = remove
# Base code for this was taken from Problem Solving with Algorithms
# and Data Structures using Python by By Brad Miller and David Ranum, Luther College
# Section 4.5. Implementing a Stack in Python. The code was written assuming a list object.
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
        
class UnorderedListStack:

    def __init__(self):
        self.head = None
        self.rear = None
        
    def isEmpty(self):
        return self.head == None
    
    def push(self,item):
        #add an item to the top.
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
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
            
    def pop(self):
        #remove an item from the top.
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
    myUnorderedList = UnorderedListStack()
    print('Empty?: ', myUnorderedList.isEmpty()) #It is, you know. We just created it.
    myUnorderedList.pop() #Test for pop of empty list. Will return None.
    print("Push 31")
    myUnorderedList.push(31)
    print('After pop size?', myUnorderedList.size())
    print('Head?', myUnorderedList.peek())
    print("Push 55")
    myUnorderedList.push(55)
    print('Size?', myUnorderedList.size())
    print('Head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print("Push 17")
    myUnorderedList.push(17)
    print('Print List:')
    myUnorderedList.printList()
    print('Empty?: ', myUnorderedList.isEmpty())
    print("Push 89")
    myUnorderedList.push(89)
    print('Print List:')
    myUnorderedList.printList()
    print('Size?', myUnorderedList.size())
    print('55?', myUnorderedList.search(55))
    print('17?', myUnorderedList.search(17))
    print('100?',myUnorderedList.search(100))
    print("Push 100")
    myUnorderedList.push(100)
    print('100?',myUnorderedList.search(100))
    print('head?', myUnorderedList.peek())
    print('Print List:')
    myUnorderedList.printList()
    print('What did we pop?',myUnorderedList.pop())
    print('After pop size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()
    print('head?', myUnorderedList.peek())    
    print('What did we pop?',myUnorderedList.pop())
    print('After pop size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()
    print('head?', myUnorderedList.peek())
    print('What did we pop?',myUnorderedList.pop())
    print('After pop size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()
    print('head?', myUnorderedList.peek())
    print('What did we pop?',myUnorderedList.pop())
    print('After pop size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()
    print('head?', myUnorderedList.peek())
    print('What did we pop?',myUnorderedList.pop())
    print('After pop size?', myUnorderedList.size())
    print('Print List:')
    myUnorderedList.printList()
    print('head?', myUnorderedList.peek())

  
main()