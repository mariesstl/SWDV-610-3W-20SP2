# Three missionaries and three cannibals come to a river and find a boat that holds
# two people. Everyone must get across the river to continue on the journey.
# However, if the cannibals ever outnumber the missionaries on either bank,
# the missionaries will be eaten. Find a series of crossings that will get everyone
# safely to the other side of the river.  Record your program running and
# submit your code and recording.
# I used the article cited below to get the valid crossing states and to confirm the answer.
# Fraley, R., Cooke, K., & Detrick, P. (1966). Graphical Solution of Difficult Crossing Puzzles.
# Mathematics Magazine, 39(3), 151-157. doi:10.2307/2689307

# Valid states(c,m):
#     (0,0)
#     (0,3)
#     (1,0)
#     (1,1)
#     (1,3)
#     (2,0)
#     (2,2)
#     (2,3)
#     (3,0)
#     (3,3)

# Crossings(c,m):
#     (3,3)
#     (1,3)
#     (2,3)
#     (0,3)
#     (1,3)
#     (1,1)
#     (2,2)
#     (2,2)
#     (2,0)
#     (1,0)
#     (3,0)
#     (1,0)
#     (2,0)
#     (0,0)
# 
# This solution uses a queue, a stack and a graph data structure:


#QUEUE
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

#STACK        
class Stack:

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


#GRAPH
class Vertex:
    def __init__(self,num, ):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = 0
        self.pred = None
        self.disc = 0
        self.fin = 0
   
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
   
    def getId(self):
        return self.id
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0): #from and to
        if f not in self.vertList: 
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = UnorderedListQueue() #using a queue for the vertices
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        print("CurrentVert: ",currentVert.getId())
        for nbr in currentVert.getConnections():
            print("Neighbor: ", nbr.getId())    
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
                currentVert.setColor('black')

def traverse(vertex):
    myStack = Stack()# using stack so that I can easily reverse the order of the output
    vertexCopy = vertex
    myStack.push(vertexCopy.getId())
    while (vertexCopy.getPred()):
#         print(vertexCopy.getId())
        vertexCopy = vertexCopy.getPred()
        myStack.push(vertexCopy.getId())
#     print(vertexCopy.getId())
    previous = myStack.pop()#first item is our starting state

    print('Starting State: ',previous)
    
    cannibal = int(previous[1])#extracting the amount of cannibals
    missionary = int(previous[3])#extracting the amount of missionaries
    
    print('We start with {} cannibals and {} missionaries on the left side of the river.'.format(cannibal, missionary))
 
    while (myStack.isEmpty() == False):#Keep popping off values until empty
        next = myStack.pop()#calling the next value next and extracting boat side
        boatSide = next[5]

        if boatSide == 'R':#if we are moving to the right
            side = 'right'
        else:#if we are moving to the left
            side = 'left'
            
        print('{}: {} cannibal(s) and {} missionaries were moved to the {}'.format(next, abs(cannibal - int(next[1])), abs(missionary - int(next[3])),side))

        cannibal = int(next[1])#extracting the amount of cannibals
        missionary = int(next[3])#extracting the amount of missionaries

def main():
    g = Graph()
    #adding all possible edges starting with the beginning state
    g.addEdge('C3M3BL', 'C1M3BR')
    g.addEdge('C3M3BL', 'C2M2BR')
    g.addEdge('C3M3BL', 'C2M3BR')

    g.addEdge('C1M3BR', 'C2M3BL')
    
    g.addEdge('C2M2BR', 'C2M3BL')

    g.addEdge('C2M3BR', 'C2M3BL')
    
    g.addEdge('C2M3BL', 'C0M3BR')
    g.addEdge('C2M3BL', 'C1M3BR')
    g.addEdge('C2M3BL', 'C2M2BR')
    
    g.addEdge('C0M3BR', 'C1M3BL')
    g.addEdge('C0M3BR', 'C2M3BL')

    g.addEdge('C1M3BL', 'C1M1BR')
    g.addEdge('C1M3BL', 'C0M3BR')
    g.addEdge('C1M3BL', 'C2M3BR')

    g.addEdge('C1M1BR', 'C1M3BL')
    g.addEdge('C1M1BR', 'C2M2BL')

    g.addEdge('C2M2BL', 'C1M1BR')
    g.addEdge('C2M2BL', 'C2M0BR')
    
    g.addEdge('C2M0BR', 'C3M0BL')

    g.addEdge('C3M0BL', 'C2M0BR')
    g.addEdge('C3M0BL', 'C1M0BR')

    g.addEdge('C1M0BR', 'C3M0BL')
    g.addEdge('C1M0BR', 'C2M0BL')
    
    g.addEdge('C2M0BL', 'C1M0BR')
    g.addEdge('C2M0BL', 'C0M0BR')
    
    bfs(g,g.getVertex('C3M3BL'))
    traverse(g.getVertex('C0M0BR'))
    
main()

