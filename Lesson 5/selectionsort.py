# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# selection sort
# We will be filling the values at the end of the list with the largest value
# We go through the whole list and put the largest value at the right most slot -1 each time


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):#start at the end and go through for each slot
       positionOfMax=0 #variable for the largest value in the list. Initialize it to the first slot.
       for location in range(1,fillslot+1):# traverse the list to find where the largest value is
           if alist[location]>alist[positionOfMax]: #if value in current location > holding area for largest value
               positionOfMax = location #make this location the location of largest value
       temp = alist[fillslot] # Hold what is currently in the slot we are about to fill
       alist[fillslot] = alist[positionOfMax]#fill where we are right to left with the max value
       alist[positionOfMax] = temp #fill where we took the value with the temp value

alist = [1,9,3,4,8,10,7,5,2,6]
print('unsorted', alist)
selectionSort(alist)
print('sorted',alist)