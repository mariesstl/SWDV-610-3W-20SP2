# Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
# Show how this list is sorted by the following algorithms:
# insertion sort

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

    while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

    alist[position]=currentvalue

alist = [1,9,3,4,8,10,7,5,2,6]
insertionSort(alist)
print(alist)