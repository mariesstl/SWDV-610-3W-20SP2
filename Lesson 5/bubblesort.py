# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# bubble sort

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): #Start at the end of the list and go in by 1
        for i in range(passnum):
            if alist[i]>alist[i+1]: #if the number to the left > the number to the right
                temp = alist[i] #put it in a temp spot
                alist[i] = alist[i+1] #put the smaller number to the left
                alist[i+1] = temp #take the larger number from temp and put it the number to the right


alist = [1,9,3,4,8,10,7,5,2,6]
print('unsorted', alist)
bubbleSort(alist)
print('sorted',alist)
