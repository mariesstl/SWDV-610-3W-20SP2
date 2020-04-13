# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# insertion sort

def insertionSort(alist):
   for index in range(1,len(alist)): #skip position 0. Move right and we assume a sorted sublist at 0
     currentvalue = alist[index] #Get current value and position.
     position = index #Get current position.
     while position>0 and alist[position-1]>currentvalue: #if not at beginning and value to left is greater than current value
         alist[position]=alist[position-1]#put that value here
         position = position-1 #move one position to the left
     alist[position]=currentvalue#put current value there

alist = [1,9,3,4,8,10,7,5,2,6]
print('unsorted', alist)
insertionSort(alist)
print('sorted',alist)