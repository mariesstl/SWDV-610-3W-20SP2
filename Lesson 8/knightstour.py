# Knight's Tour
# Given a starting space, find a series of valid moves for the knight
# so that it can go to every space on the board once.
# Using a graph data structure
# Using a depth-first search in Knight's Tour function
# Using recursion in Knight's Tour function

#GRAPH
class vertex:
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
        self.vertexList = {}
        self.numvertices = 0

    def addvertex(self,key):
        self.numvertices = self.numvertices + 1
        newvertex = vertex(key)
        self.vertexList[key] = newvertex
        return newvertex

    def getvertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def __contains__(self,n):
#       custom class requires this to use in
        return n in self.vertexList

    def addEdge(self,f,t,weight=0): #from and to
        #add any new vertex
        if f not in self.vertexList: 
            nvertex = self.addvertex(f)
        if t not in self.vertexList:
            nvertex = self.addvertex(t)
#             from adds to as a neighbor with given weight
        self.vertexList[f].addNeighbor(self.vertexList[t], weight)

    def getvertices(self):
        return self.vertexList.keys()

    def __iter__(self):
#       makes our graph iterable
        return iter(self.vertexList.values())

def knightGraph(bdSize):
    myknGraph = Graph()
    for row in range(bdSize):
#         print("row: ",row)
        for col in range(bdSize):
#             print('column: ',col)
#             create each position on the board as a vertex
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMove(row,col,bdSize)
#             print (newPositions)
#             add legal new positions as edges
            for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               myknGraph.addEdge(nodeId,nid)
#                print(nodeId)
    return myknGraph

def posToNodeId(row, column, board_size):
#     print ('new positions:',(row * board_size) + column)
    return (row * board_size) + column

def genLegalMove(x,y,bdSize):
#   Generate all 8 possible moves for the knight
    newMoves = []
# 1 or 2 squares vertically, or 1 or 2 squares horizontally
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
#       if the move is on the board, add it to new moves
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    #Make sure a move is on the board
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
def knightTour(n,path,u,limit):
    #depth-first search
#     n is the depth we start at = 0 (number of steps taken)
#     path = where we have visited
#     u is vertex to explore (checking out or next move)
#     limit = how many spaces to visit
#         print("visiting vertex: ", u.getId())
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(orderByAvail(u))#get the list of neighbors ordered by those with the fewest avail moves after them
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
#                   if you have not already visited this one,
#                   recursively call knightsTour for this neighbor
                    done = knightTour(n+1, path, nbrList[i], limit)#every time we go into the recursion we are adding 1 to n.
                i = i + 1
            if not done:  # You can't complete Knight's Tour from this spot at this time. Go to the previous vertex. 
                path.pop()#remove from append
                u.setColor('white')#set color back to white
        else:
            done = True
        return done
    
def orderByAvail(n):
#     This orders our neighbors by how many avail moves they have
#     for the next move. It counterintuitively chooses the path with
#     the *least* number of moves. This is because we need to force
#     it to the edges first. If it goes to the middle it will backtrack
#     more often and later and take a longer time doing so. Failure at the edges is faster.
    resList = []
    for vertex in n.getConnections():
        if vertex.getColor() == 'white':
            c = 0# for each neighbor start over
#             for each of my neighbors' neighbors, if they haven't
#             been visited add 1 to c
#             this shows how many avail moves exist from our neighbor
            for w in vertex.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c,vertex))
    resList.sort(key=lambda x: x[0])#lambda function - sort by the 0 index
#     resList.reverse()
    return [y[1] for y in resList]

def main():
    boardSize = 8
    startingSquare = 3
    print("Board size = {}".format(boardSize))
    myGraph = knightGraph(boardSize)#create an 8x8 board
    kPath = []#create an empty string for the path
    print("Starting Square = {}".format(startingSquare))
    knightTour(0,kPath,myGraph.getvertex(startingSquare),63)
#     print(path)
    pathCount = 1
    while pathCount <=63 :
        print("Knight's path: step {}: {}".format(pathCount,kPath[pathCount].getId()))
        pathCount +=1
main()